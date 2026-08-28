#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TỰ ĐỘNG TÁCH VÀ KHỞI TẠO 10 REPO GITHUB RIÊNG BIỆT CHO 10 SIÊU VỆ TINH
"""

import os
import sys
import io
import subprocess
import time

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SATELLITES_DIR = os.path.join(SCRIPT_DIR, "satellites")

REPOS = [
    {"folder": "01-github-batdongsan-sapa", "repo_name": "batdongsan-sapa-review", "desc": "Review BĐS Đất Nền Sa Pa"},
    {"folder": "02-cloudflare-matbang-sapa", "repo_name": "matbang-sapa-review", "desc": "Cẩm Nang Thuê Mặt Bằng Kinh Doanh Sa Pa"},
    {"folder": "03-vercel-vieclam-sapa", "repo_name": "vieclam-sapa-review", "desc": "Cẩm Nang Nghề Nghiệp & Mức Lương Sa Pa"},
    {"folder": "04-netlify-homestay-sapa", "repo_name": "homestay-sapa-review", "desc": "Top Homestay Săn Mây Sa Pa"},
    {"folder": "05-render-anuong-sapa", "repo_name": "anuong-sapa-review", "desc": "Cẩm Nang Ẩm Thực & Quán Ngon Sa Pa"},
    {"folder": "06-gitlab-nhadat-laocai", "repo_name": "nhadat-laocai-review", "desc": "Đánh Giá Mua Bán Nhà Đất TP Lào Cai"},
    {"folder": "07-amplify-dautu-sapa", "repo_name": "dautu-sapa-review", "desc": "Kinh Nghiệm Đầu Tư BĐS & Homestay Sa Pa"},
    {"folder": "08-azure-bietthu-sapa", "repo_name": "bietthu-sapa-review", "desc": "Top Biệt Thự & Shophouse Sa Pa"},
    {"folder": "09-digitalocean-sangnhuong-sapa", "repo_name": "sangnhuong-sapa-review", "desc": "Cẩm Nang Sang Nhượng Khách Sạn Sa Pa"},
    {"folder": "10-firebase-camnang-laocai", "repo_name": "camnang-laocai-review", "desc": "Cẩm Nang Dịch Vụ Du Lịch Sa Pa"}
]

def create_individual_repos():
    print("=" * 70)
    print("🚀 BẮT ĐẦU TẠO 10 REPO GITHUB ĐỘC LẬP CHO TỪNG VỆ TINH")
    print("=" * 70)

    for idx, item in enumerate(REPOS, start=1):
        target_path = os.path.join(SATELLITES_DIR, item["folder"])
        repo_name = item["repo_name"]
        print(f"\n[{idx}/10] 📦 Đang xử lý Repo: {repo_name}...")

        # 1. Init git if not exists
        git_dir = os.path.join(target_path, ".git")
        if not os.path.exists(git_dir):
            subprocess.run(["git", "-C", target_path, "init"], capture_output=True, text=True)
            subprocess.run(["git", "-C", target_path, "config", "user.name", "bacnguyen0106"], capture_output=True)
            subprocess.run(["git", "-C", target_path, "config", "user.email", "bacnguyen0106@users.noreply.github.com"], capture_output=True)
            subprocess.run(["git", "-C", target_path, "branch", "-M", "main"], capture_output=True)

        # 2. Add and commit
        subprocess.run(["git", "-C", target_path, "add", "."], capture_output=True)
        subprocess.run(["git", "-C", target_path, "commit", "-m", f"feat: init satellite site {repo_name}"], capture_output=True)

        # 3. Create GH repo and push
        create_cmd = ["gh", "repo", "create", repo_name, "--public", f"--source={target_path}", "--remote=origin", "--push"]
        res = subprocess.run(create_cmd, capture_output=True, text=True)
        if res.returncode == 0:
            print(f"  ✅ Đã tạo & push thành công: https://github.com/bacnguyen0106/{repo_name}")
        else:
            # If repo already exists on GH, just push
            push_res = subprocess.run(["git", "-C", target_path, "push", "-u", "origin", "main"], capture_output=True, text=True)
            print(f"  ℹ️ Repo đã có sẵn trên GH, đã push cập nhật: https://github.com/bacnguyen0106/{repo_name}")

    print("\n" + "=" * 70)
    print("🎉 HOÀN TẤT TẠO TOÀN BỘ 10 REPO GITHUB RIÊNG BIỆT!")
    print("=" * 70)

if __name__ == "__main__":
    create_individual_repos()
