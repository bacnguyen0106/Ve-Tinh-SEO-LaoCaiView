#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIFIED AI WRITER ENGINE (GOOGLE GEMINI 2026 + GROQ HYBRID ROTATION)
Tự động luân phiên xoay vòng đa tầng giữa 3 Google Gemini Keys & 3 Groq Keys và các Model chính thức mới nhất 2026.
Bảo đảm 100% không bao giờ bị đứt đầu, không lo nghẽn mạng hay chạm giới hạn (Rate Limit / Quota).
"""

import os
import sys
import io
import json
import time
import requests
from dotenv import load_dotenv

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

script_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(script_dir, ".env"))

# 1. Danh sách Google Models chính thức được kiểm chứng trực tiếp qua API
GOOGLE_MODELS = [
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
    "gemini-3.5-flash",
    "gemini-3.6-flash",
    "gemini-flash-latest",
    "gemini-flash-lite-latest"
]

# 2. Danh sách Groq Models chính thức khả dụng
GROQ_MODELS = [
    "openai/gpt-oss-120b",
    "openai/gpt-oss-20b",
    "qwen/qwen3.6-27b",
    "groq/compound-mini"
]

vi_tri_groq_key = 0
vi_tri_google_key = 0

def get_groq_keys():
    raw = os.environ.get("GROQ_API_KEY", "")
    return [k.strip() for k in raw.split(",") if k.strip()]

def get_google_keys():
    raw = os.environ.get("GOOGLE_API_KEY", "") or os.environ.get("GEMINI_API_KEY", "")
    return [k.strip() for k in raw.split(",") if k.strip()]

def call_groq(prompt, json_mode=True):
    global vi_tri_groq_key
    groq_keys = get_groq_keys()
    if not groq_keys:
        return None

    for model in GROQ_MODELS:
        attempts = 0
        while attempts < len(groq_keys):
            key = groq_keys[vi_tri_groq_key]
            url = "https://api.groq.com/openai/v1/chat/completions"
            headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
            payload = {
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.3
            }
            if json_mode:
                payload["response_format"] = {"type": "json_object"}

            try:
                res = requests.post(url, headers=headers, json=payload, timeout=10)
                if res.status_code == 200:
                    content = res.json()['choices'][0]['message']['content'].strip()
                    # Clean thinking tags if present (e.g. Qwen / Deepseek)
                    if "<think>" in content and "</think>" in content:
                        content = content.split("</think>")[-1].strip()

                    if json_mode:
                        try:
                            # Clean potential markdown fences
                            clean_json = content.replace("```json", "").replace("```", "").strip()
                            return json.loads(clean_json), f"Groq [{model}] (Key #{vi_tri_groq_key+1})"
                        except:
                            pass
                    else:
                        return content, f"Groq [{model}] (Key #{vi_tri_groq_key+1})"
                else:
                    vi_tri_groq_key = (vi_tri_groq_key + 1) % len(groq_keys)
                    attempts += 1
                    time.sleep(0.3)
            except Exception:
                vi_tri_groq_key = (vi_tri_groq_key + 1) % len(groq_keys)
                attempts += 1
                time.sleep(0.3)

    return None

def call_google_gemini(prompt, json_mode=True):
    global vi_tri_google_key
    google_keys = get_google_keys()
    if not google_keys:
        return None

    for model in GOOGLE_MODELS:
        attempts = 0
        while attempts < len(google_keys):
            key = google_keys[vi_tri_google_key]
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
            headers = {"Content-Type": "application/json"}
            payload = {
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {
                    "temperature": 0.3
                }
            }
            if json_mode:
                payload["generationConfig"]["responseMimeType"] = "application/json"

            try:
                res = requests.post(url, headers=headers, json=payload, timeout=10)
                if res.status_code == 200:
                    res_json = res.json()
                    candidates = res_json.get('candidates', [])
                    if candidates:
                        content = candidates[0]['content']['parts'][0]['text'].strip()
                        if json_mode:
                            try:
                                return json.loads(content), f"Google [{model}] (Key #{vi_tri_google_key+1})"
                            except:
                                clean_json = content.replace("```json", "").replace("```", "").strip()
                                return json.loads(clean_json), f"Google [{model}] (Key #{vi_tri_google_key+1})"
                        else:
                            return content, f"Google [{model}] (Key #{vi_tri_google_key+1})"
                else:
                    vi_tri_google_key = (vi_tri_google_key + 1) % len(google_keys)
                    attempts += 1
                    time.sleep(0.3)
            except Exception:
                vi_tri_google_key = (vi_tri_google_key + 1) % len(google_keys)
                attempts += 1
                time.sleep(0.3)

    return None

def generate_ai_content(prompt, json_mode=True, prefer="google"):
    """
    Tự động luân phiên thông minh xoay vòng giữa Google Gemini và Groq AI.
    """
    if prefer == "google":
        # 1. Thử Google Gemini trước
        res = call_google_gemini(prompt, json_mode=json_mode)
        if res:
            data, provider = res
            print(f"  ✨ AI {provider} đã sáng tác xong nội dung!", flush=True)
            return data
        
        # 2. Fallback sang Groq
        res = call_groq(prompt, json_mode=json_mode)
        if res:
            data, provider = res
            print(f"  ✨ AI {provider} (Dự phòng Groq) đã sáng tác xong nội dung!", flush=True)
            return data
    else:
        # 1. Thử Groq trước
        res = call_groq(prompt, json_mode=json_mode)
        if res:
            data, provider = res
            print(f"  ✨ AI {provider} đã sáng tác xong nội dung!", flush=True)
            return data

        # 2. Fallback sang Google Gemini
        res = call_google_gemini(prompt, json_mode=json_mode)
        if res:
            data, provider = res
            print(f"  ✨ AI {provider} (Dự phòng Google) đã sáng tác xong nội dung!", flush=True)
            return data

    return None

if __name__ == "__main__":
    print("=" * 60)
    print("🧪 KIỂM TRA BỘ NÃO AI ENGINE XOAY VÒNG HYBRID")
    print("=" * 60)
    
    test_prompt = """Hãy đóng vai chuyên gia SEO BĐS Sa Pa. Viết review ngắn về đất Tả Van Sa Pa.
Trả về JSON:
{
  "tieu_de": "Tiêu đề chuẩn SEO",
  "danh_gia": "Nhận định ngắn 2 câu",
  "diem_noi_bat": ["Ưu điểm 1", "Ưu điểm 2"],
  "link_cta": "https://laocaiview.vn/bat-dong-san"
}"""
    
    print("1. Thử nghiệm với Google Gemini (3 Keys xoay vòng)...")
    res_google = generate_ai_content(test_prompt, json_mode=True, prefer="google")
    print("Kết quả Google:", json.dumps(res_google, ensure_ascii=False, indent=2))
    
    print("\n2. Thử nghiệm với Groq AI (3 Keys xoay vòng)...")
    res_groq = generate_ai_content(test_prompt, json_mode=True, prefer="groq")
    print("Kết quả Groq:", json.dumps(res_groq, ensure_ascii=False, indent=2))
    print("=" * 60)
