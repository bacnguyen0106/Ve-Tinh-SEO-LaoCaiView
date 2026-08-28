#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KẾT NỐI HỆ THỐNG MẠNG LƯỚI BACKLINK DOFOLLOW 10 NỀN TẢNG ĐA ĐÁM MÂY
VÀ ĐỒNG BỘ MẠNG LƯỚI TIER-1 TRỎ VỀ TOÀN DIỆN HỆ SINH THÁI LAOCAIVIEW.VN
ÁP DỤNG ĐỒNG LOẠT TRÊN TOÀN BỘ 40 REPO VỆ TINH
"""

import os
import sys
import io
import re
import subprocess
from datetime import datetime

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SATELLITES_DIR = os.path.join(SCRIPT_DIR, "satellites")

# 10 Nền tảng Đám mây Vệ tinh Trụ cột
PLATFORMS_10 = [
    {"name": "GitHub Pages", "symbol": "🐙", "domain": "github.io", "url": "https://bacnguyen0106.github.io/dat-trungtam-sapa/", "tag": "DA 98 • Code Repo"},
    {"name": "Cloudflare Pages", "symbol": "⚡", "domain": "pages.dev", "url": "https://matbangsapa-review.pages.dev/", "tag": "DA 96 • Global Edge CDN"},
    {"name": "Vercel Cloud", "symbol": "▲", "domain": "vercel.app", "url": "https://vieclamsapa-review.vercel.app/", "tag": "DA 92 • Serverless Speed"},
    {"name": "Netlify Cloud", "symbol": "💎", "domain": "netlify.app", "url": "https://homestaysapa-review.netlify.app/", "tag": "DA 94 • Edge Network"},
    {"name": "Render Cloud", "symbol": "🚀", "domain": "onrender.com", "url": "https://anuongsapa-review.onrender.com/", "tag": "DA 85 • Cloud Hosting"},
    {"name": "GitLab Pages", "symbol": "🦊", "domain": "gitlab.io", "url": "https://nhadatlaocai-review.gitlab.io/", "tag": "DA 93 • Independent IP"},
    {"name": "AWS Amplify", "symbol": "☁️", "domain": "amplifyapp.com", "url": "https://dautusapa-review.amplifyapp.com/", "tag": "DA 96 • Amazon Cloud"},
    {"name": "Azure Static Apps", "symbol": "🔷", "domain": "azurewebsites.net", "url": "https://bietthusapa-review.azurewebsites.net/", "tag": "DA 97 • Microsoft Edge"},
    {"name": "DigitalOcean", "symbol": "🌊", "domain": "ondigitalocean.app", "url": "https://sangnhuongsapa-review.ondigitalocean.app/", "tag": "DA 89 • High Performance"},
    {"name": "Firebase Google", "symbol": "🔥", "domain": "web.app", "url": "https://camnanglaocai-review.web.app/", "tag": "DA 96 • Google Cloud DB"}
]

# 12 Trang Đích Chiến Lược Của LaoCaiView.vn
LAOCAIVIEW_TARGETS = [
    {"name": "Trang Chủ LaoCaiView", "url": "https://laocaiview.vn", "desc": "Cổng thông tin & dịch vụ giám tuyển Lào Cai"},
    {"name": "Mua Bán Bất Động Sản", "url": "https://laocaiview.vn/bat-dong-san", "desc": "Sàn giao dịch nhà đất & BĐS Sa Pa"},
    {"name": "Dự Án 83ha Alphora Mường Hoa", "url": "https://laocaiview.vn/bat-dong-san/du-an-alphora-muong-hoa-sa-pa", "desc": "Đại đô thị nghỉ dưỡng quốc tế Sa Pa"},
    {"name": "31 Căn Shophouse Làng Ẩm Thực", "url": "https://laocaiview.vn/bat-dong-san/mat-bang-shophouse-lang-am-thuc-alphora-muong-hoa", "desc": "Mặt bằng kinh doanh F&B Tỉnh lộ 152"},
    {"name": "79 Dinh Thự InterContinental", "url": "https://laocaiview.vn/bat-dong-san/mat-bang-biet-thu-intercontinental-sapa-resort", "desc": "Biệt thự 5 sao The Residences"},
    {"name": "Tin Tức Làng Ẩm Thực", "url": "https://laocaiview.vn/tin-tuc/lang-am-thuc-quoc-te-alphora-muong-hoa-mot-diem-den-van-trai-nghiem", "desc": "Một điểm đến vạn trải nghiệm"},
    {"name": "Cẩm Nang & Tin Tức Thị Trường", "url": "https://laocaiview.vn/tin-tuc", "desc": "Tin tức thời sự & kinh nghiệm du lịch"},
    {"name": "Lưu Trú & Đặt Phòng Khách Sạn", "url": "https://laocaiview.vn/dat-phong", "desc": "Villa, homestay & khách sạn Sa Pa"},
    {"name": "Ẩm Thực & Nhà Hàng Tuyển Chọn", "url": "https://laocaiview.vn/an-uong", "desc": "Top nhà hàng lẩu cá tầm, thắng cố Sa Pa"},
    {"name": "Mặt Bằng Kinh Doanh Sa Pa", "url": "https://laocaiview.vn/mat-bang", "desc": "Cho thuê mặt bằng phố du lịch Cầu Mây"},
    {"name": "Ký Gửi & Thẩm Định Bất Động Sản", "url": "https://laocaiview.vn/ky-gui", "desc": "Dịch vụ ký gửi nhà đất minh bạch"},
    {"name": "Cơ Hội Việc Làm & Tuyển Dụng", "url": "https://laocaiview.vn/viec-lam", "desc": "Việc làm F&B, khách sạn, hướng dẫn viên"}
]

def build_10_platforms_html():
    platforms_cards = ""
    for p in PLATFORMS_10:
        platforms_cards += f"""
        <a href="{p['url']}" target="_blank" rel="dofollow" class="p-3 rounded-xl bg-slate-900/80 hover:bg-slate-800 border border-slate-700/60 hover:border-[#B3905D] text-slate-300 hover:text-white transition flex flex-col justify-between group shadow-sm">
            <div class="flex items-center justify-between">
                <span class="text-lg">{p['symbol']}</span>
                <span class="text-[9px] font-bold px-1.5 py-0.5 rounded bg-slate-800 text-[#e5c285] border border-[#B3905D]/20">{p['domain']}</span>
            </div>
            <span class="font-bold text-xs text-white mt-1 group-hover:text-[#e5c285]">{p['name']}</span>
            <span class="text-[10px] text-slate-400 mt-0.5">{p['tag']}</span>
        </a>
        """
        
    targets_cards = ""
    for t in LAOCAIVIEW_TARGETS:
        targets_cards += f"""
        <a href="{t['url']}" target="_blank" rel="dofollow" class="p-3 rounded-xl bg-slate-900/60 hover:bg-slate-900 border border-slate-800 hover:border-[#B3905D]/60 text-slate-300 hover:text-[#e5c285] transition flex flex-col justify-between">
            <span class="font-bold text-xs text-white flex items-center justify-between">
                <span>{t['name']}</span>
                <span class="text-[10px] text-[#e5c285]">↗</span>
            </span>
            <span class="text-[10px] text-slate-400 mt-1">{t['desc']}</span>
        </a>
        """

    return f"""
    <!-- MULTI-PLATFORM & TIER-1 BACKLINK MATRIX SECTION -->
    <section class="glass rounded-3xl p-6 md:p-8 space-y-6 border border-[#B3905D]/30 my-8">
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-[#B3905D]/20 pb-4">
            <div>
                <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-[11px] font-bold bg-[#B3905D]/20 text-[#e5c285] border border-[#B3905D]/40 mb-2">
                    <span>🌐</span>
                    <span>MẠNG LƯỚI LIÊN KẾT ĐA ĐÁM MÂY TIER-1</span>
                </div>
                <h3 class="text-lg md:text-xl font-extrabold text-white">
                    Hệ Thống 10 Nền Tảng Vệ Tinh Đám Mây & Trung Tâm Dữ Liệu LaoCaiView
                </h3>
            </div>
            <div class="flex items-center gap-3">
                <a href="tel:0918153986" class="px-4 py-2 rounded-xl bg-slate-900 text-[#e5c285] border border-[#B3905D]/50 text-xs font-bold hover:bg-slate-800 transition flex items-center gap-1.5">
                    <span>📞 0918.153.986</span>
                </a>
            </div>
        </div>

        <!-- 10 Platforms Cloud Grid -->
        <div class="space-y-2">
            <h4 class="text-xs font-bold text-[#e5c285] uppercase tracking-wider flex items-center gap-1.5">
                <span>⚡</span> 10 Nền Tảng Đám Mây Độc Lập (Multi-Cloud Node Mesh):
            </h4>
            <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-2.5">
                {platforms_cards}
            </div>
        </div>

        <!-- 12 Core Targets Grid -->
        <div class="space-y-2 pt-2 border-t border-slate-800">
            <h4 class="text-xs font-bold text-[#e5c285] uppercase tracking-wider flex items-center gap-1.5">
                <span>🎯</span> Danh Mục Trọng Điểm Trên LaoCaiView.vn:
            </h4>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-2.5">
                {targets_cards}
            </div>
        </div>
    </section>
    """

def update_all_satellites():
    matrix_html = build_10_platforms_html()
    all_dirs = [d for d in os.listdir(SATELLITES_DIR) if os.path.isdir(os.path.join(SATELLITES_DIR, d))]
    all_dirs.sort()
    
    print(f"Bắt đầu kết nối mạng lưới Dofollow 10 nền tảng cho {len(all_dirs)} vệ tinh...")
    
    updated_count = 0
    for d in all_dirs:
        repo_path = os.path.join(SATELLITES_DIR, d)
        index_file = os.path.join(repo_path, "index.html")
        
        if not os.path.exists(index_file):
            continue
            
        with open(index_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Check if already has matrix
        if "MẠNG LƯỚI LIÊN KẾT ĐA ĐÁM MÂY TIER-1" in content:
            # Replace existing section
            pattern = r'<!-- MULTI-PLATFORM & TIER-1 BACKLINK MATRIX SECTION -->.*?<!-- /MULTI-PLATFORM & TIER-1 BACKLINK MATRIX SECTION -->'
            if re.search(pattern, content, flags=re.DOTALL):
                new_content = re.sub(pattern, matrix_html, content, flags=re.DOTALL)
            else:
                # Replace the old section
                new_content = content
        else:
            # Inject before </main>
            if "</main>" in content:
                new_content = content.replace("</main>", f"{matrix_html}\n    </main>")
            else:
                new_content = content.replace("</body>", f"{matrix_html}\n</body>")
                
        with open(index_file, "w", encoding="utf-8") as f:
            f.write(new_content)
            
        # Git commit and push
        subprocess.run("git add .", cwd=repo_path, shell=True, capture_output=True)
        commit_res = subprocess.run('git commit -m "feat(mesh): connect 10-platform dofollow backlink matrix with LaoCaiView.vn"', cwd=repo_path, shell=True, capture_output=True, text=True)
        if "nothing to commit" not in commit_res.stdout:
            subprocess.run("git push origin main", cwd=repo_path, shell=True, capture_output=True)
            print(f"[{d}] ✅ Đã cập nhật ma trận Dofollow & đẩy lên GitHub!")
            updated_count += 1
        else:
            print(f"[{d}] Đã đồng bộ mới nhất.")
            
    print(f"\n--- HOÀN TẤT KẾT NỐI TOÀN DIỆN {len(all_dirs)} VỆ TINH ---")

if __name__ == "__main__":
    update_all_satellites()
