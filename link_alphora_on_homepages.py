#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
THÊM BANNER / THẺ BÀI VIẾT NỔI BẬT ALPHORA MƯỜNG HOA VÀO TRANG CHỦ INDEX.HTML CỦA 5 TRANG VỆ TINH
"""

import os
import sys
import io
import subprocess

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SATELLITES_DIR = os.path.join(SCRIPT_DIR, "satellites")

LINKS = [
    {
        "folder": "01-github-batdongsan-sapa",
        "repo_name": "batdongsan-sapa-review",
        "file": "alphora-muong-hoa-sapa-tong-quan.html",
        "badge": "💎 DỰ ÁN NGHỈ DƯỠNG 83HA SỔ ĐỎ",
        "title": "Đánh Giá Tổng Quan Dự Án Alphora Mường Hoa Sa Pa 2026",
        "desc": "Khảo sát vị trí Tỉnh lộ 152, pháp lý đất ở đô thị sở hữu lâu dài và uy tín CĐT Alphanam Group."
    },
    {
        "folder": "02-cloudflare-matbang-sapa",
        "repo_name": "matbang-sapa-review",
        "file": "shophouse-alphora-muong-hoa-kinh-doanh.html",
        "badge": "🏪 SHOPHOUSE THƯƠNG MẠI F&B",
        "title": "Tiềm Năng Kinh Doanh Shophouse Phố Thương Mại Alphora Mường Hoa",
        "desc": "Phân tích lưu lượng triệu lượt khách du lịch thung lũng Mường Hoa và bài toán cho thuê F&B, Spa."
    },
    {
        "folder": "08-azure-bietthu-sapa",
        "repo_name": "bietthu-sapa-review",
        "file": "biet-thu-intercontinental-alphora-muong-hoa.html",
        "badge": "🏰 DINH THỰ 5 SAO QUỐC TẾ IHG",
        "title": "Review Biệt Thự The Residences at InterContinental Sapa",
        "desc": "Tuyệt tác biệt thự nghỉ dưỡng đồi view Fansipan và thung lũng Mường Hoa, dịch vụ quản gia 24/7."
    },
    {
        "folder": "07-amplify-dautu-sapa",
        "repo_name": "dautu-sapa-review",
        "file": "co-hoi-dau-tu-alphora-muong-hoa-sapa.html",
        "badge": "📈 BÀI TOÁN DÒNG TIỀN 2026 - 2030",
        "title": "Phân Tích Suất Sinh Lời & Pháp Lý Sở Hữu Lâu Dài Alphora Mường Hoa",
        "desc": "Đòn bẩy hạ tầng cao tốc, sân bay Sa Pa và cơ hội đầu tư tích sản an toàn bền vững."
    },
    {
        "folder": "04-netlify-homestay-sapa",
        "repo_name": "homestay-sapa-review",
        "file": "trai-nghiem-nghi-duong-alphora-muong-hoa.html",
        "badge": "🌿 NGHỈ DƯỠNG & CÔNG VIÊN VĂN HÓA",
        "title": "Trải Nghiệm Nghỉ Dưỡng & Khám Phá Công Viên Văn Hóa Alphora Mường Hoa",
        "desc": "Thiên đường nghỉ dưỡng giữa thung lũng ruộng bậc thang kỳ vĩ và liệu pháp wellness tắm thuốc Dao đỏ."
    }
]

def add_spotlight_cards():
    for item in LINKS:
        target_dir = os.path.join(SATELLITES_DIR, item["folder"])
        index_file = os.path.join(target_dir, "index.html")
        
        if not os.path.exists(index_file):
            continue
            
        with open(index_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        card_html = f"""
        <!-- Spotlight Alphora Muong Hoa Card -->
        <section class="p-6 md:p-8 rounded-3xl bg-gradient-to-r from-slate-900 via-slate-800 to-black border-2 border-emerald-500/40 shadow-2xl my-8">
            <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
                <div class="space-y-2">
                    <span class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
                        {item['badge']}
                    </span>
                    <h3 class="text-xl md:text-2xl font-black text-white">
                        <a href="{item['file']}" class="hover:text-emerald-400 transition">
                            {item['title']} ↗
                        </a>
                    </h3>
                    <p class="text-xs md:text-sm text-slate-300 max-w-2xl leading-relaxed">
                        {item['desc']}
                    </p>
                </div>
                <a href="{item['file']}" class="px-6 py-3.5 rounded-2xl bg-white text-slate-950 hover:bg-slate-100 font-bold text-xs transition shadow-xl shrink-0">
                    Đọc Bài Đánh Giá ↗
                </a>
            </div>
        </section>
"""
        if item['file'] not in content:
            if "</main>" in content:
                content = content.replace("</main>", f"{card_html}\n    </main>")
            elif "</section>" in content:
                content = content.replace("</section>", f"</section>\n{card_html}", 1)
                
            with open(index_file, "w", encoding="utf-8") as f:
                f.write(content)
                
            subprocess.run(["git", "-C", target_dir, "add", "index.html"], capture_output=True)
            subprocess.run(["git", "-C", target_dir, "commit", "-m", f"feat: link Alphora Muong Hoa article on homepage"], capture_output=True)
            subprocess.run(["git", "-C", target_dir, "push", "origin", "main"], capture_output=True)
            print(f"✅ Đã gắn bài viết nổi bật vào index.html của [{item['repo_name']}]")

if __name__ == "__main__":
    add_spotlight_cards()
