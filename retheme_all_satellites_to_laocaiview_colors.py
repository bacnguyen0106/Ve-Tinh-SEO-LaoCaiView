#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHUYỂN TOÀN BỘ MÀU SẮC CỦA HỆ THỐNG VỆ TINH VỀ ĐÚNG BẢNG MÀU CHÍNH THỨC CỦA LAOCAIVIEW.VN:
- Nền chính: Xanh Navy Đêm Thượng Lưu (#030b20 & #020818)
- Màu nhấn chủ đạo (Brand Gold): #B3905D (Vàng ánh kim sang trọng)
- Màu nhấn bổ trợ (Forest Green): #1A3622 (Xanh rừng Tây Bắc)
- Màu chữ & Viền: Trắng tuyết (#f5f6f7), Vàng kim nhạt (#c4a676), Viền glass (#B3905D/30)
- Font chữ: Inter & system-ui
"""

import os
import sys
import io
import re
import subprocess

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SATELLITES_DIR = os.path.join(SCRIPT_DIR, "satellites")

# LaoCaiView Standard CSS Styles
LCV_COLOR_RULES = """
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
      tailwind.config = {
        theme: {
          extend: {
            colors: {
              lcv: {
                navy: '#030b20',
                dark: '#020818',
                gold: '#B3905D',
                'gold-light': '#c4a676',
                green: '#1A3622',
                'green-light': '#254d30'
              }
            }
          }
        }
      }
    </script>
    <style>
      body { background-color: #030b20; color: #f5f6f7; font-family: 'Inter', system-ui, -apple-system, sans-serif; }
      .lcv-glass { background: rgba(3, 11, 32, 0.85); backdrop-filter: blur(16px); border: 1px solid rgba(179, 144, 93, 0.25); }
      .lcv-card { background: rgba(15, 23, 42, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(179, 144, 93, 0.2); }
      .lcv-gold-btn { background: linear-gradient(135deg, #B3905D 0%, #c4a676 100%); color: #030b20; font-weight: 800; }
      .lcv-gold-btn:hover { background: #B3905D; color: #020818; }
      .lcv-gold-text { color: #B3905D; }
      .lcv-badge { background: rgba(179, 144, 93, 0.15); color: #c4a676; border: 1px solid rgba(179, 144, 93, 0.35); }
    </style>
"""

# Apply to all satellite repositories
def retheme_all_html_files():
    print("=" * 75)
    print("🎨 BẮT ĐẦU ĐỒNG BỘ BẢNG MÀU LAOCAIVIEW (#030b20 & #B3905D) CHO TOÀN BỘ VỆ TINH")
    print("=" * 75)

    satellite_folders = [f for f in os.listdir(SATELLITES_DIR) if os.path.isdir(os.path.join(SATELLITES_DIR, f))]

    for folder in sorted(satellite_folders):
        folder_path = os.path.join(SATELLITES_DIR, folder)
        html_files = [f for f in os.listdir(folder_path) if f.endswith(".html")]

        print(f"\n📦 Xử lý kho: [{folder}] ({len(html_files)} files HTML)...")

        for hf in html_files:
            file_path = os.path.join(folder_path, hf)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # 1. Thay thế background & style cũ bằng chuẩn LaoCaiView
            content = re.sub(r'body\s*\{[^}]*background[^}]*\}', "body { background-color: #030b20; color: #f5f6f7; font-family: 'Inter', system-ui, sans-serif; }", content)
            content = re.sub(r'background-color:\s*#[0-9a-fA-F]{6};?', "background-color: #030b20;", content)
            content = re.sub(r'background:\s*#[0-9a-fA-F]{6};?', "background: #030b20;", content)

            # 2. Thay thế màu xanh lá / cam / tím / cyan rực thành màu Vàng Gold #B3905D & Xanh Navy #030b20
            content = content.replace("text-emerald-400", "text-[#B3905D]")
            content = content.replace("text-emerald-300", "text-[#c4a676]")
            content = content.replace("text-amber-400", "text-[#B3905D]")
            content = content.replace("text-amber-300", "text-[#c4a676]")
            content = content.replace("text-cyan-400", "text-[#B3905D]")
            content = content.replace("text-indigo-400", "text-[#B3905D]")
            content = content.replace("text-teal-400", "text-[#B3905D]")
            content = content.replace("text-orange-400", "text-[#B3905D]")
            content = content.replace("text-rose-400", "text-[#B3905D]")
            content = content.replace("text-violet-400", "text-[#B3905D]")
            content = content.replace("text-sky-400", "text-[#B3905D]")

            # Nút bấm
            content = content.replace("bg-emerald-500", "bg-[#B3905D] text-[#030b20]")
            content = content.replace("bg-emerald-400", "bg-[#B3905D] text-[#030b20]")
            content = content.replace("bg-amber-500", "bg-[#B3905D] text-[#030b20]")
            content = content.replace("bg-cyan-500", "bg-[#B3905D] text-[#030b20]")
            content = content.replace("bg-indigo-500", "bg-[#B3905D] text-[#030b20]")
            content = content.replace("bg-teal-500", "bg-[#B3905D] text-[#030b20]")
            content = content.replace("bg-orange-500", "bg-[#B3905D] text-[#030b20]")
            content = content.replace("bg-rose-500", "bg-[#B3905D] text-[#030b20]")
            content = content.replace("bg-violet-500", "bg-[#B3905D] text-[#030b20]")
            content = content.replace("bg-sky-500", "bg-[#B3905D] text-[#030b20]")

            # Viền & Badges
            content = content.replace("border-emerald-500", "border-[#B3905D]")
            content = content.replace("border-amber-500", "border-[#B3905D]")
            content = content.replace("border-cyan-500", "border-[#B3905D]")
            content = content.replace("border-indigo-500", "border-[#B3905D]")
            content = content.replace("border-teal-500", "border-[#B3905D]")
            content = content.replace("border-emerald-800", "border-[#1A3622]")
            content = content.replace("border-emerald-900", "border-[#1A3622]")
            content = content.replace("border-amber-900", "border-[#1A3622]")
            content = content.replace("bg-emerald-950", "bg-[#030b20]")
            content = content.replace("bg-amber-950", "bg-[#030b20]")
            content = content.replace("bg-slate-900", "bg-[#020818]/90")
            content = content.replace("bg-slate-950", "bg-[#020818]")

            # Khung Footer
            content = content.replace("border-t border-emerald-900/40", "border-t border-[#1A3622] bg-[#020818]")
            content = content.replace("border-t border-amber-950", "border-t border-[#1A3622] bg-[#020818]")
            content = content.replace("border-t border-teal-950", "border-t border-[#1A3622] bg-[#020818]")
            content = content.replace("border-t border-indigo-950", "border-t border-[#1A3622] bg-[#020818]")
            content = content.replace("border-t border-cyan-950", "border-t border-[#1A3622] bg-[#020818]")
            content = content.replace("text-emerald-600/80", "text-[#c4a676]/80")
            content = content.replace("text-amber-700", "text-[#c4a676]/80")
            content = content.replace("text-teal-800", "text-[#c4a676]/80")
            content = content.replace("text-indigo-800", "text-[#c4a676]/80")
            content = content.replace("text-cyan-800", "text-[#c4a676]/80")

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ Đã chuyển màu LaoCaiView cho: {hf}")

        # Commit and push
        subprocess.run(["git", "-C", folder_path, "add", "."], capture_output=True)
        subprocess.run(["git", "-C", folder_path, "commit", "-m", "style: rebrand color palette to match LaoCaiView signature Navy (#030b20) and Gold (#B3905D)"], capture_output=True)
        push_res = subprocess.run(["git", "-C", folder_path, "push", "origin", "main"], capture_output=True, text=True)
        if push_res.returncode == 0:
            print(f"  🚀 Đã đẩy cập nhật màu LaoCaiView lên GitHub!")
        else:
            print(f"  ℹ️ Git push: {push_res.stderr.strip() or 'OK'}")

    print("\n" + "=" * 75)
    print("🎉 HOÀN TẤT ĐỒNG BỘ BẢNG MÀU CHÍNH THỨC CỦA LAOCAIVIEW CHO TOÀN BỘ VỆ TINH!")
    print("=" * 75)

if __name__ == "__main__":
    retheme_all_html_files()
