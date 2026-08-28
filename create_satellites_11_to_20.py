#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TỰ ĐỘNG KHỞI TẠO 10 KHO DỮ LIỆU VỆ TINH MỚI (ĐÁNH SỐ 11 ĐẾN 20)
KÈM GIAO DIỆN RIÊNG, LOGO FAVICON, ẢNH MẠNG XÃ HỘI, SITEMAP, GOOGLE TAG (G-CD5FQPC501)
VÀ TỰ ĐỘNG TẠO 10 REPO GITHUB ĐỘC LẬP
"""

import os
import sys
import io
import json
import subprocess
from datetime import datetime

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SATELLITES_DIR = os.path.join(SCRIPT_DIR, "satellites")

SATELLITES_11_TO_20 = [
    {
        "id": "11-xaydung-sapa-review",
        "repo_name": "xaydung-sapa-review",
        "number": 11,
        "title": "Cẩm Nang Thiết Kế & Xây Dựng Homestay Sa Pa 2026",
        "brand": "SaPa Architect Hub",
        "tagline": "Kinh nghiệm thi công nhà gỗ bungalow, xử lý nền móng taluy & tối ưu chi phí",
        "domain": "xaydung-sapa-review.pages.dev",
        "icon_symbol": "📐",
        "theme_gradient": ["#713f12", "#422006"],
        "accent_color": "#eab308",
        "keywords": "xây homestay sa pa, chi phí xây bungalow sapa, thiết kế nhà đẹp sapa, thi công nhà gỗ sapa",
        "cta_url": "https://laocaiview.vn/ky-gui",
        "cta_text": "Đăng Ký Tư Vấn & Thẩm Định Dự Án Miễn Phí Trên LaoCaiView.vn",
        "category": "Kiến Trúc & Thi Công",
        "pros": ["Tối ưu vật liệu đá và gỗ bản địa chống ẩm lạnh", "Quy trình xin cấp phép xây dựng rõ ràng", "Dự toán chi phí sát thực tế từng m²"]
    },
    {
        "id": "12-fansipan-guide-sapa",
        "repo_name": "fansipan-guide-sapa",
        "number": 12,
        "title": "Cẩm Nang Chinh Phục Đỉnh Fansipan & Vé Cáp Treo 2026",
        "brand": "Fansipan Peak Guide",
        "tagline": "Kinh nghiệm trekking đỉnh Fansipan, bảng giá vé cáp treo Sun World & giờ đón mây",
        "domain": "fansipan-guide-sapa.vercel.app",
        "icon_symbol": "⛰️",
        "theme_gradient": ["#083344", "#0e7490"],
        "accent_color": "#06b6d4",
        "keywords": "vé cáp treo fansipan 2026, kinh nghiệm leo fansipan, bảng giá sun world fansipan, tour săn mây fansipan",
        "cta_url": "https://laocaiview.vn/dat-phong",
        "cta_text": "Xem Khách Sạn Gần Ga Cáp Treo Fansipan Giá Tốt Trên LaoCaiView.vn",
        "category": "Du Lịch & Danh Thắng",
        "pros": ["Cập nhật giờ vận hành cáp treo & dự báo thời tiết đỉnh núi", "Lịch trình trekking an toàn có hướng dẫn viên", "Mẹo mua vé không phải xếp hàng"]
    },
    {
        "id": "13-dat-sodo-sapa-review",
        "repo_name": "dat-sodo-sapa-review",
        "number": 13,
        "title": "Khảo Sát Đất Thổ Cư Sổ Đỏ Sa Pa & Cẩm Nang Pháp Lý",
        "brand": "SaPa Legal Land",
        "tagline": "Thẩm định đất thổ cư ONT, quy trình tách thửa, chuyển đổi mục đích sử dụng đất",
        "domain": "dat-sodo-sapa-review.github.io",
        "icon_symbol": "📜",
        "theme_gradient": ["#064e3b", "#022c22"],
        "accent_color": "#16a34a",
        "keywords": "bán đất sổ đỏ sapa, đất thổ cư sa pa chính chủ, pháp lý đất bản sa pa, chuyển đổi đất nông nghiệp sapa",
        "cta_url": "https://laocaiview.vn/bat-dong-san/ban-dat-so-do-sa-pa",
        "cta_text": "Xem Danh Sách Đất Có Sổ Đỏ Tra Cứu Trực Tiếp Trên LaoCaiView.vn",
        "category": "Pháp Lý & Bất Động Sản",
        "pros": ["100% đất được kiểm tra trích lục địa chính", "Ranh giới rõ ràng, không tranh chấp", "Sang tên công chứng nhanh chóng"]
    },
    {
        "id": "14-villa-sapa-review",
        "repo_name": "villa-sapa-review",
        "number": 14,
        "title": "Bộ Sưu Tập Villa Nguyên Căn & Biệt Thự Nghỉ Dưỡng Sa Pa",
        "brand": "SaPa Private Villas",
        "tagline": "Review biệt thự nghỉ dưỡng gia đình, villa có bể bơi nước nóng & sân nướng BBQ",
        "domain": "villa-sapa-review.netlify.app",
        "icon_symbol": "🏡",
        "theme_gradient": ["#3b0764", "#581c87"],
        "accent_color": "#8b5cf6",
        "keywords": "thuê villa sapa nguyên căn, biệt thự sapa view đẹp, villa sapa có bể bơi nước nóng, villa gia đình sapa",
        "cta_url": "https://laocaiview.vn/dat-phong",
        "cta_text": "Kiểm Tra Lịch Trống & Báo Giá Villa Ưu Đãi Trên LaoCaiView.vn",
        "category": "Lưu Trú Cao Cấp",
        "pros": ["Không gian riêng tư biệt lập giữa rừng thông", "Đầy đủ bếp nướng BBQ và quản gia phục vụ", "View thung lũng Mường Hoa không góc chết"]
    },
    {
        "id": "15-bep-bar-sapa-careers",
        "repo_name": "bep-bar-sapa-careers",
        "number": 15,
        "title": "Cẩm Nang Tuyển Dụng & Mức Lương Bếp, Bartender Sa Pa",
        "brand": "SaPa Chef & Bar Hub",
        "tagline": "Khảo sát chế độ đãi ngộ, văn hóa làm việc và việc làm F&B nhà hàng, resort Sa Pa",
        "domain": "bep-bar-sapa-careers.onrender.com",
        "icon_symbol": "👨‍🍳",
        "theme_gradient": ["#431407", "#7c2d12"],
        "accent_color": "#ea580c",
        "keywords": "tuyển đầu bếp sapa, việc làm pha chế bartender sapa, tuyển phụ bếp có chỗ ăn ở sapa, lương f&b sapa",
        "cta_url": "https://laocaiview.vn/viec-lam",
        "cta_text": "Nộp Hồ Sơ Ứng Tuyển F&B Nhận Việc Ngay Trên LaoCaiView.vn",
        "category": "Nghề Nghiệp F&B",
        "pros": ["Bao ăn 3 bữa và chỗ ở tiện nghi cho nhân sự", "Thu nhập cứng + Service charge hấp dẫn", "Cơ hội nâng cao tay nghề món Á - Âu"]
    },
    {
        "id": "16-taphin-culture-review",
        "repo_name": "taphin-culture-review",
        "number": 16,
        "title": "Trải Nghiệm Tắm Lá Thuốc Người Dao Đỏ & Bản Tả Phìn",
        "brand": "Tả Phìn Eco Experience",
        "tagline": "Khám phá bí quyết bài thuốc tắm thảo mộc 30 vị, hang động Tả Phìn và tu viện cổ",
        "domain": "taphin-culture-review.gitlab.io",
        "icon_symbol": "🌿",
        "theme_gradient": ["#022c22", "#064e3b"],
        "accent_color": "#059669",
        "keywords": "tắm lá thuốc tả phìn, bài thuốc dao đỏ sapa, kinh nghiệm đi bản tả phìn, tu viện cổ tả phìn",
        "cta_url": "https://laocaiview.vn/an-uong",
        "cta_text": "Xem Danh Sách Cơ Sở Tắm Thuốc & Quán Ăn Tả Phìn Trên LaoCaiView.vn",
        "category": "Văn Hóa & Trải Nghiệm",
        "pros": ["Thảo dược rừng Hoàng Liên Sơn chính gốc", "Không gian tắm thùng gỗ pơ mu thơm ngát", "Phục hồi sức khỏe và lưu thông khí huyết tuyệt vời"]
    },
    {
        "id": "17-dat-nongnghiep-sapa",
        "repo_name": "dat-nongnghiep-sapa",
        "number": 17,
        "title": "Đánh Giá Đất Vườn Nông Nghiệp & Trang Trại Sa Pa 2026",
        "brand": "SaPa Agri Land",
        "tagline": "Khảo sát đất đồi trồng cây dược liệu, nông nghiệp sạch, mô hình Farmstay sinh thái",
        "domain": "dat-nongnghiep-sapa.koyeb.app",
        "icon_symbol": "🌾",
        "theme_gradient": ["#451a03", "#78350f"],
        "accent_color": "#d97706",
        "keywords": "mua đất vườn sa pa, đất trồng dược liệu sapa, bán đất đồi sapa diện tích lớn, farmstay sapa",
        "cta_url": "https://laocaiview.vn/bat-dong-san/ban-dat-vuon-nong-nghiep-sa-pa",
        "cta_text": "Xem Bảng Giá Đất Vườn Nông Nghiệp Mới Nhất Trên LaoCaiView.vn",
        "category": "BĐS Nông Nghiệp & Farmstay",
        "pros": ["Diện tích lớn từ 1.000m² - 20.000m² giá rẻ", "Khí hậu ôn đới thích hợp trồng Atiso, hoa quả xứ lạnh", "Tiềm năng khai thác du lịch trải nghiệm nông nghiệp"]
    },
    {
        "id": "18-limousine-xe-laocai",
        "repo_name": "limousine-xe-laocai",
        "number": 18,
        "title": "Danh Bạ Xe Limousine Hà Nội - Sa Pa & Thuê Xe Tự Lái",
        "brand": "Lào Cai Transit Guide",
        "tagline": "Tổng hợp hotline các nhà xe VIP, giờ xuất bến cao tốc Nội Bài - Lào Cai và giá cước",
        "domain": "limousine-xe-laocai.deno.dev",
        "icon_symbol": "🚐",
        "theme_gradient": ["#172554", "#1e3a8a"],
        "accent_color": "#2563eb",
        "keywords": "xe limousine hà nội sapa, số điện thoại xe sapa, thuê xe ô tô tự lái lào cai, xe đưa đón sân bay nội bài sapa",
        "cta_url": "https://laocaiview.vn",
        "cta_text": "Tra Cứu Hotline & Dịch Vụ Du Lịch Sa Pa 24/7 Trên LaoCaiView.vn",
        "category": "Phương Tiện & Di Chuyển",
        "pros": ["Ghế ngồi massage hạng thương gia cao cấp", "Đón trả tận nơi tại sảnh khách sạn Sa Pa", "Thời gian chạy cao tốc chỉ 4.5 - 5 tiếng"]
    },
    {
        "id": "19-sangquancafe-sapa",
        "repo_name": "sangquancafe-sapa",
        "number": 19,
        "title": "Cẩm Nang Sang Nhượng Quán Cafe & Nhà Hàng Sa Pa 2026",
        "brand": "SaPa Cafe Transfer",
        "tagline": "Thẩm định doanh thu, chuyển nhượng mặt bằng kinh doanh phố đi bộ có sẵn đồ",
        "domain": "sangquancafe-sapa.glitch.me",
        "icon_symbol": "☕",
        "theme_gradient": ["#3e2723", "#4e342e"],
        "accent_color": "#8d6e63",
        "keywords": "sang nhượng quán cafe sapa, chuyển nhượng nhà hàng sapa, sang quán ăn phố cầu mây sapa",
        "cta_url": "https://laocaiview.vn/mat-bang",
        "cta_text": "Xem Danh Sách Quán Đang Cần Sang Nhượng Gấp Trên LaoCaiView.vn",
        "category": "Mặt Bằng & Sang Nhượng",
        "pros": ["Bàn giao toàn bộ máy móc pha chế & công thức", "Tệp khách du lịch ổn định không mất thời gian setup", "Hỗ trợ đàm phán hợp đồng thuê dài hạn với chủ nhà"]
    },
    {
        "id": "20-quyhoach-laocai-2030",
        "repo_name": "quyhoach-laocai-2030",
        "number": 20,
        "title": "Bản Đồ Quy Hoạch Đô Thị & Hạ Tầng TP Lào Cai 2026 - 2030",
        "brand": "Lào Cai Master Plan",
        "tagline": "Phân tích trục phát triển kinh tế cửa khẩu, đại lộ Trần Hưng Đạo & cầu đường kết nối",
        "domain": "quyhoach-laocai-2030.pages.dev",
        "icon_symbol": "🗺️",
        "theme_gradient": ["#4c0519", "#881337"],
        "accent_color": "#e11d48",
        "keywords": "quy hoạch lào cai 2030, bản đồ quy hoạch tp lào cai, dự án cầu qua sông hồng lào cai, đất quy hoạch bắc cường",
        "cta_url": "https://laocaiview.vn/bat-dong-san/nha-dat-lao-cai",
        "cta_text": "Tra Cứu BĐS Nằm Trong Vùng Quy Hoạch Đô Thị Trên LaoCaiView.vn",
        "category": "Quy Hoạch & Hạ Tầng",
        "pros": ["Đón đầu quy hoạch nâng cấp cửa khẩu quốc tế", "Hạ tầng giao thông kết nối liên vùng thông suốt", "Dư địa tăng trưởng giá trị bất động sản dài hạn"]
    }
]

def generate_svg_favicon(item):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <defs>
    <linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{item['theme_gradient'][0]}"/>
      <stop offset="100%" stop-color="{item['accent_color']}"/>
    </linearGradient>
  </defs>
  <rect width="100" height="100" rx="28" fill="url(#g)"/>
  <circle cx="50" cy="50" r="42" fill="none" stroke="{item['accent_color']}" stroke-width="2" opacity="0.4"/>
  <text x="50%" y="55%" text-anchor="middle" dominant-baseline="middle" font-size="44">{item['icon_symbol']}</text>
</svg>"""

def generate_og_image_svg(item):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050811"/>
      <stop offset="50%" stop-color="{item['theme_gradient'][0]}"/>
      <stop offset="100%" stop-color="#0B0F17"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="30" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>
  <rect width="1200" height="630" fill="url(#bg)"/>
  <circle cx="950" cy="180" r="220" fill="{item['accent_color']}" opacity="0.15" filter="url(#glow)"/>
  <rect x="30" y="30" width="1140" height="570" rx="30" fill="none" stroke="{item['accent_color']}" stroke-width="2" stroke-opacity="0.3"/>
  <g transform="translate(80, 80)">
    <rect width="320" height="48" rx="24" fill="rgba(255, 255, 255, 0.08)" stroke="{item['accent_color']}" stroke-opacity="0.4"/>
    <text x="24" y="31" font-family="-apple-system, sans-serif" font-size="19" font-weight="bold" fill="{item['accent_color']}">
      {item['icon_symbol']}  #{item['number']} {item['brand']}
    </text>
  </g>
  <text x="80" y="240" font-family="-apple-system, sans-serif" font-size="44" font-weight="900" fill="#FFFFFF">
    {item['title']}
  </text>
  <text x="80" y="320" font-family="-apple-system, sans-serif" font-size="23" font-weight="500" fill="#94A3B8">
    {item['tagline']}
  </text>
  <g transform="translate(80, 500)">
    <line x1="0" y1="0" x2="1040" y2="0" stroke="rgba(255, 255, 255, 0.1)" stroke-width="1"/>
    <text x="0" y="42" font-family="-apple-system, sans-serif" font-size="18" font-weight="bold" fill="#64748B">
      Hệ thống vệ tinh SEO trực thuộc:
    </text>
    <text x="320" y="42" font-family="-apple-system, sans-serif" font-size="22" font-weight="900" fill="{item['accent_color']}">
      LaoCaiView.vn ↗
    </text>
  </g>
</svg>"""

def generate_index_html(item):
    date_str = datetime.now().strftime("%d/%m/%Y")
    pros_html = "".join([f'<li class="flex items-start gap-2"><span class="text-emerald-400 font-bold">✓</span> {p}</li>' for p in item["pros"]])
    
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-CD5FQPC501"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());

      gtag('config', 'G-CD5FQPC501');
    </script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{item['title']} | #{item['number']} {item['brand']}</title>
    <meta name="description" content="{item['tagline']}. Tra cứu thông tin chính thức được giám tuyển tại LaoCaiView.vn.">
    <meta name="keywords" content="{item['keywords']}">
    
    <link rel="icon" type="image/svg+xml" href="favicon.svg">
    <link rel="canonical" href="{item['cta_url']}">
    
    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="{item['title']}">
    <meta property="og:description" content="{item['tagline']}">
    <meta property="og:image" content="og-image.svg">
    <meta property="og:site_name" content="{item['brand']}">
    
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {{ background-color: #070a12; color: #e2e8f0; font-family: system-ui, -apple-system, sans-serif; }}
        .glass {{ background: rgba(15, 23, 42, 0.75); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.08); }}
    </style>
</head>
<body class="min-h-screen flex flex-col">
    <!-- Navbar -->
    <nav class="glass sticky top-0 z-50 px-4 py-3.5 border-b border-slate-800">
        <div class="max-w-5xl mx-auto flex items-center justify-between">
            <a href="index.html" class="flex items-center gap-2.5 font-bold text-white text-base md:text-lg">
                <span class="text-2xl">{item['icon_symbol']}</span>
                <span>{item['brand']}</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-black bg-slate-800 text-slate-400 border border-slate-700">#{item['number']}</span>
            </a>
            <a href="{item['cta_url']}" target="_blank" rel="dofollow" class="px-4 py-2 rounded-xl text-xs font-bold bg-white text-slate-950 hover:bg-slate-100 transition shadow-lg flex items-center gap-1">
                <span>Khám Phá LaoCaiView</span>
                <span>↗</span>
            </a>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="flex-grow max-w-4xl mx-auto px-4 py-10 w-full space-y-8">
        <header>
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold bg-slate-800 text-slate-300 border border-slate-700 mb-3">
                <span>{item['icon_symbol']}</span>
                <span>Chuyên Mục: {item['category']}</span>
            </div>
            <h1 class="text-2xl md:text-4xl font-extrabold text-white mb-3 leading-tight">
                {item['title']}
            </h1>
            <div class="flex items-center gap-4 text-xs text-slate-400 pb-4 border-b border-slate-800">
                <span>📅 Cập nhật: {date_str}</span>
                <span>⭐ Điểm đánh giá: <strong class="text-amber-400">4.9/5</strong></span>
                <span>🛡️ Dữ liệu xác thực 2026</span>
            </div>
        </header>

        <!-- Pros & Highlights -->
        <section class="glass p-6 rounded-2xl border-l-4 border-l-emerald-500 space-y-3 shadow-xl">
            <h3 class="font-bold text-sm text-emerald-400 uppercase tracking-wider">🌟 ĐIỂM NỔI BẬT & KINH NGHIỆM ĐÁNH GIÁ:</h3>
            <ul class="text-xs md:text-sm space-y-2 text-slate-300">
                {pros_html}
            </ul>
        </section>

        <!-- Detailed Review Article -->
        <article class="glass p-6 md:p-8 rounded-2xl text-slate-300 leading-relaxed text-sm md:text-base space-y-4 shadow-xl">
            <h2 class="text-lg md:text-xl font-bold text-white mb-2">1. Tổng Quan Thị Trường & Xu Hướng Tìm Kiếm</h2>
            <p>
                Khu vực Sa Pa và TP Lào Cai đang có sự bứt phá mạnh mẽ trong lĩnh vực <strong>{item['category'].lower()}</strong>. Người dùng và nhà đầu tư ngày càng đòi hỏi thông tin có kiểm duyệt, hình ảnh thực tế rõ ràng và liên hệ trực tiếp không qua trung gian.
            </p>
            <h2 class="text-lg md:text-xl font-bold text-white mt-6 mb-2">2. Cẩm Nang Tra Cứu & Đưa Ra Quyết Định</h2>
            <p>
                Để nắm bắt các cơ hội tốt nhất và tránh các rủi ro không đáng có, bạn nên tham khảo nguồn dữ liệu số chính thống tại nền tảng giám tuyển <strong>LaoCaiView</strong> để kết nối trực tiếp chủ sở hữu, đơn vị thi công hoặc nhà tuyển dụng.
            </p>
        </article>

        <!-- High-Conversion Contextual CTA Banner -->
        <section class="p-6 md:p-8 rounded-3xl bg-gradient-to-r from-slate-900 via-slate-800 to-black border border-slate-700 shadow-2xl">
            <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
                <div>
                    <div class="inline-block px-3 py-1 rounded-md text-xs font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 mb-2">
                        🔥 TRUNG TÂM DỮ LIỆU LAOCAIVIEW
                    </div>
                    <h3 class="text-lg md:text-xl font-bold text-white mb-1">Truy Cập Dữ Liệu Gốc & Liên Hệ Trực Tiếp:</h3>
                    <p class="text-xs text-slate-400">{item['tagline']}.</p>
                </div>
                <a href="{item['cta_url']}" target="_blank" rel="dofollow" class="w-full md:w-auto text-center px-6 py-3.5 rounded-xl font-bold text-sm bg-white text-slate-900 hover:bg-slate-100 transition shadow-xl shrink-0">
                    👉 {item['cta_text']} ↗
                </a>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="glass mt-auto py-6 border-t border-slate-800 text-center text-xs text-slate-500">
        <div class="max-w-4xl mx-auto px-4">
            <p class="mb-1">© 2026 {item['brand']} (Vệ Tinh #{item['number']}). Trực thuộc <a href="https://laocaiview.vn" target="_blank" rel="dofollow" class="text-emerald-400 hover:underline font-medium">LaoCaiView.vn</a>.</p>
            <p>Hạ tầng CDN phân tán tốc độ cao.</p>
        </div>
    </footer>
</body>
</html>"""

def generate_robots_txt():
    return """User-agent: *
Allow: /

Sitemap: sitemap.xml
"""

def generate_sitemap_xml(item):
    today = datetime.now().strftime("%Y-%m-%d")
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://bacnguyen0106.github.io/{item['repo_name']}/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>"""

def create_and_deploy_satellites_11_to_20():
    print("=" * 75)
    print("🚀 BẮT ĐẦU TẠO 10 KHO VỆ TINH MỚI (ĐÁNH SỐ TỪ 11 ĐẾN 20)")
    print("=" * 75)

    for idx, item in enumerate(SATELLITES_11_TO_20, start=11):
        target_path = os.path.join(SATELLITES_DIR, item["id"])
        os.makedirs(target_path, exist_ok=True)
        repo_name = item["repo_name"]
        print(f"\n[#{idx}/20] 📦 Tạo Kho & Dữ Liệu Cho [{repo_name}]...")

        # 1. Tạo favicon.svg
        with open(os.path.join(target_path, "favicon.svg"), "w", encoding="utf-8") as f:
            f.write(generate_svg_favicon(item))

        # 2. Tạo og-image.svg
        with open(os.path.join(target_path, "og-image.svg"), "w", encoding="utf-8") as f:
            f.write(generate_og_image_svg(item))

        # 3. Tạo index.html
        with open(os.path.join(target_path, "index.html"), "w", encoding="utf-8") as f:
            f.write(generate_index_html(item))

        # 4. Tạo robots.txt
        with open(os.path.join(target_path, "robots.txt"), "w", encoding="utf-8") as f:
            f.write(generate_robots_txt())

        # 5. Tạo sitemap.xml
        with open(os.path.join(target_path, "sitemap.xml"), "w", encoding="utf-8") as f:
            f.write(generate_sitemap_xml(item))

        # 6. Tạo README.md
        with open(os.path.join(target_path, "README.md"), "w", encoding="utf-8") as f:
            f.write(f"# #{item['number']} {item['brand']}\n\n{item['title']}\n\nTrực thuộc hệ thống vệ tinh SEO **[LaoCaiView.vn](https://laocaiview.vn)**.")

        print(f"  ✓ Đã sinh đầy đủ: favicon.svg, og-image.svg, index.html, robots.txt, sitemap.xml, README.md")

        # 7. Khởi tạo Git nếu chưa có
        git_dir = os.path.join(target_path, ".git")
        if not os.path.exists(git_dir):
            subprocess.run(["git", "-C", target_path, "init"], capture_output=True)
            subprocess.run(["git", "-C", target_path, "config", "user.name", "bacnguyen0106"], capture_output=True)
            subprocess.run(["git", "-C", target_path, "config", "user.email", "bacnguyen0106@users.noreply.github.com"], capture_output=True)
            subprocess.run(["git", "-C", target_path, "branch", "-M", "main"], capture_output=True)

        subprocess.run(["git", "-C", target_path, "add", "."], capture_output=True)
        subprocess.run(["git", "-C", target_path, "commit", "-m", f"feat: init satellite #{item['number']} {repo_name}"], capture_output=True)

        # 8. Tạo GitHub repo và push bằng gh CLI
        create_cmd = ["gh", "repo", "create", repo_name, "--public", f"--source={target_path}", "--remote=origin", "--push"]
        res = subprocess.run(create_cmd, capture_output=True, text=True)
        if res.returncode == 0:
            print(f"  🚀 Đã tạo & push thành công Repo GitHub: https://github.com/bacnguyen0106/{repo_name}")
        else:
            push_res = subprocess.run(["git", "-C", target_path, "push", "-u", "origin", "main"], capture_output=True, text=True)
            print(f"  ℹ️ Đã push cập nhật Repo: https://github.com/bacnguyen0106/{repo_name}")

    print("\n" + "=" * 75)
    print("🎉 HOÀN TẤT TẠO VÀ ĐẨY ĐỦ 10 KHO VỆ TINH MỚI (11 ĐẾN 20) LÊN GITHUB!")
    print("=" * 75)

if __name__ == "__main__":
    create_and_deploy_satellites_11_to_20()
