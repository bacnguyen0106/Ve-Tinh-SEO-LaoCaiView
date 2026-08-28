#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHÈN THẺ GOOGLE TAG (G-CD5FQPC501) VÀO NGAY SAU <head> CHO TẤT CẢ 10 WEBSITE VỆ TINH
VÀ TỰ ĐỘNG ĐẨY LÊN TẤT CẢ REPOSITORY GITHUB
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

GOOGLE_TAG_SNIPPET = """    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-CD5FQPC501"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-CD5FQPC501');
    </script>"""

REPOS = [
    {"folder": "01-github-batdongsan-sapa", "repo_name": "batdongsan-sapa-review"},
    {"folder": "02-cloudflare-matbang-sapa", "repo_name": "matbang-sapa-review"},
    {"folder": "03-vercel-vieclam-sapa", "repo_name": "vieclam-sapa-review"},
    {"folder": "04-netlify-homestay-sapa", "repo_name": "homestay-sapa-review"},
    {"folder": "05-render-anuong-sapa", "repo_name": "anuong-sapa-review"},
    {"folder": "06-gitlab-nhadat-laocai", "repo_name": "nhadat-laocai-review"},
    {"folder": "07-amplify-dautu-sapa", "repo_name": "dautu-sapa-review"},
    {"folder": "08-azure-bietthu-sapa", "repo_name": "bietthu-sapa-review"},
    {"folder": "09-digitalocean-sangnhuong-sapa", "repo_name": "sangnhuong-sapa-review"},
    {"folder": "10-firebase-camnang-laocai", "repo_name": "camnang-laocai-review"}
]

def add_google_tag():
    print("=" * 70)
    print("🏷️  BẮT ĐẦU CHÈN THẺ GOOGLE TAG (G-CD5FQPC501) VÀO 10 WEBSITE VỆ TINH")
    print("=" * 70)

    for idx, item in enumerate(REPOS, start=1):
        target_path = os.path.join(SATELLITES_DIR, item["folder"])
        html_file = os.path.join(target_path, "index.html")
        repo_name = item["repo_name"]

        if not os.path.exists(html_file):
            print(f"[{idx}/10] ⚠️ Không tìm thấy file: {html_file}")
            continue

        with open(html_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Xoá thẻ Google cũ nếu có để tránh trùng lặp
        content = re.sub(r'<!-- Google tag \(gtag\.js\) -->.*?gtag\(\'config\', \'[^\']+\'\);\s*</script>', '', content, flags=re.DOTALL)

        # Chèn thẻ mới ngay sau <head>
        if "<head>" in content:
            new_content = content.replace("<head>", f"<head>\n{GOOGLE_TAG_SNIPPET}", 1)
        elif "<head " in content:
            new_content = re.sub(r'(<head[^>]*>)', r'\1\n' + GOOGLE_TAG_SNIPPET, content, count=1)
        else:
            new_content = content

        with open(html_file, "w", encoding="utf-8") as f:
            f.write(new_content)

        print(f"[{idx}/10] ✅ Đã chèn Google tag vào [{repo_name}]/index.html")

        # Push to GitHub
        subprocess.run(["git", "-C", target_path, "add", "."], capture_output=True)
        subprocess.run(["git", "-C", target_path, "commit", "-m", "feat: add Google Tag G-CD5FQPC501 right after <head>"], capture_output=True)
        push_res = subprocess.run(["git", "-C", target_path, "push", "origin", "main"], capture_output=True, text=True)
        if push_res.returncode == 0:
            print(f"  🚀 Đã push cập nhật lên GitHub: https://github.com/bacnguyen0106/{repo_name}")
        else:
            print(f"  ℹ️ Push: {push_res.stderr.strip() or 'OK'}")

    print("\n" + "=" * 70)
    print("🎉 HOÀN TẤT ĐỒNG BỘ THẺ GOOGLE TAG CHO CẢ 10 WEBSITE VỆ TINH!")
    print("=" * 70)

if __name__ == "__main__":
    add_google_tag()
