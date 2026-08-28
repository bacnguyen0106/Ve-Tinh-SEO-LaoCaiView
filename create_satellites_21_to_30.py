#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TỰ ĐỘNG KHỞI TẠO 10 KHO DỮ LIỆU VỆ TINH MỚI (#21 ĐẾN #30)
GIAO DIỆN LUXURY LAOCAIVIEW, SITEMAP, GOOGLE TAG (G-CD5FQPC501), HOTLINE 0918.153.986
VÀ ĐẨY THẲNG LÊN GITHUB PAGES TỰ ĐỘNG
"""

import os
import sys
import io
import json
import subprocess
import time
from datetime import datetime

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SATELLITES_DIR = os.path.join(SCRIPT_DIR, "satellites")

SATELLITES_21_TO_30 = [
    {
        "id": "21-glamping-sapa-review",
        "repo_name": "glamping-sapa-review",
        "number": 21,
        "title": "Top Địa Điểm Glamping & Cắm Trại Săn Mây Sa Pa 2026",
        "brand": "SaPa Glamping Hub",
        "tagline": "Khảo sát khu lều trại sang trọng, săn mây thung lũng & dịch vụ tiệc nướng ngoài trời",
        "domain": "glamping-sapa-review.github.io",
        "icon_symbol": "⛺",
        "keywords": "glamping sapa, camping sapa săn mây, thuê lều trại sapa, địa điểm cắm trại sapa đẹp",
        "cta_url": "https://laocaiview.vn/dat-phong",
        "cta_text": "Xem Danh Sách Homestay & Glamping View Đẹp Trên LaoCaiView.vn",
        "category": "Cắm Trại & Trải Nghiệm",
        "pros": ["View trọn biển mây Mường Hoa và đèo Ô Quý Hồ", "Trang bị lò sưởi ấm cúng và set BBQ cao cấp", "Dễ dàng check-in sống ảo cực chill"]
    },
    {
        "id": "22-batxat-yty-travel",
        "repo_name": "batxat-yty-travel",
        "number": 22,
        "title": "Cẩm Nang Khám Phá Bát Xát & Thiên Đường Săn Mây Y Tý",
        "brand": "Y Tý - Bát Xát Discovery",
        "tagline": "Kinh nghiệm du lịch Y Tý, săn mây Ngải Thầu, mùa lúa chín A Lù & cột cờ Lũng Pô",
        "domain": "batxat-yty-travel.github.io",
        "icon_symbol": "🌾",
        "keywords": "du lịch y tý bát xát, săn mây ngải thầu, ruộng bậc thang y tý, cột cờ lũng pô lào cai",
        "cta_url": "https://laocaiview.vn/tin-tuc",
        "cta_text": "Xem Cẩm Nang Du Lịch Tây Bắc Toàn Diện Tại LaoCaiView.vn",
        "category": "Khám Phá & Săn Mây",
        "pros": ["Hướng dẫn cung đường phượt Y Tý an toàn", "Thời điểm vàng ngắm biển mây và lúa chín vàng", "Danh sách homestay nhà trình tường bản địa"]
    },
    {
        "id": "23-nightlife-bar-sapa",
        "repo_name": "nightlife-bar-sapa",
        "number": 23,
        "title": "Top Quán Bar, Pub & Cafe Acoustic Đêm Sa Pa 2026",
        "brand": "SaPa Nightlife & Lounge",
        "tagline": "Khám phá đời sống về đêm, không gian thưởng thức cocktail & âm nhạc acoustic ấm cúng",
        "domain": "nightlife-bar-sapa.github.io",
        "icon_symbol": "🍸",
        "keywords": "quán bar sapa, pub đêm sapa, cafe acoustic sapa, quán pub bờ hồ sapa",
        "cta_url": "https://laocaiview.vn/an-uong",
        "cta_text": "Khám Phá Địa Điểm Ẩm Thực & Giải Trí Đêm Trên LaoCaiView.vn",
        "category": "Ẩm Thực & Giải Trí Đêm",
        "pros": ["Không gian lounge sang trọng ngắm sương mù đêm", "Đồ uống sáng tạo từ thảo mộc Tây Bắc", "Giao lưu âm nhạc mộc acoustic hàng đêm"]
    },
    {
        "id": "24-cuakhau-laocai-trade",
        "repo_name": "cuakhau-laocai-trade",
        "number": 24,
        "title": "Cẩm Nang Cửa Khẩu Quốc Tế Lào Cai & BĐS Thương Mại",
        "brand": "Lào Cai Border Trade",
        "tagline": "Hướng dẫn thủ tục xuất nhập cảnh Hà Khẩu, logistics cửa khẩu Kim Thành & quỹ đất thương mại",
        "domain": "cuakhau-laocai-trade.github.io",
        "icon_symbol": "🛂",
        "keywords": "cửa khẩu quốc tế lào cai, du lịch hà khẩu trung quốc, đất cửa khẩu kim thành, thủ tục thông quan lào cai",
        "cta_url": "https://laocaiview.vn/bat-dong-san/nha-dat-lao-cai",
        "cta_text": "Xem Quỹ Đất Thương Mại Dịch Vụ Cửa Khẩu Trên LaoCaiView.vn",
        "category": "Cửa Khẩu & Giao Thương",
        "pros": ["Cập nhật quy định sổ thông hành xuất nhập cảnh mới nhất", "Vị trí kho bãi logistic trọng điểm cửa khẩu", "Phân tích giá trị bất động sản biên giới"]
    },
    {
        "id": "25-wedding-event-sapa",
        "repo_name": "wedding-event-sapa",
        "number": 25,
        "title": "Tổ Chức Tiệc Cưới Ngoài Trời & Sự Kiện MICE Tại Sa Pa",
        "brand": "SaPa Wedding & Events",
        "tagline": "Top resort tổ chức đám cưới trong mây, sự kiện hội nghị doanh nghiệp & chụp ảnh cưới đẹp",
        "domain": "wedding-event-sapa.github.io",
        "icon_symbol": "💍",
        "keywords": "đám cưới ngoài trời sapa, chụp ảnh cưới sapa, tổ chức sự kiện mice sapa, resort hội nghị sapa",
        "cta_url": "https://laocaiview.vn/ky-gui",
        "cta_text": "Liên Hệ Ký Gửi & Kết Nối Địa Điểm Sự Kiện Trên LaoCaiView.vn",
        "category": "Sự Kiện & Cưới Hỏi",
        "pros": ["Không gian tiệc cưới lãng mạn giữa mây ngàn Fansipan", "Dịch vụ trọn gói chuẩn 5 sao quốc tế", "Kịch bản sự kiện gắn liền văn hóa Tây Bắc độc đáo"]
    },
    {
        "id": "26-dacsan-laocai-review",
        "repo_name": "dacsan-laocai-review",
        "number": 26,
        "title": "Đặc Sản Lào Cai & Quà Tặng Tây Bắc Tuyển Chọn 2026",
        "brand": "Lào Cai Specialties Hub",
        "tagline": "Đánh giá thịt trâu gác bếp, cá hồi Sa Pa, nấm hương rừng, rượu ngô Bắc Hà chính gốc",
        "domain": "dacsan-laocai-review.github.io",
        "icon_symbol": "🎁",
        "keywords": "đặc sản lào cai làm quà, thịt trâu gác bếp sapa, nấm hương rừng sapa, rượu ngô bản phố bắc hà",
        "cta_url": "https://laocaiview.vn/an-uong",
        "cta_text": "Tìm Địa Chỉ Mua Đặc Sản Lào Cai Uy Tín Trên LaoCaiView.vn",
        "category": "Đặc Sản & Quà Tặng",
        "pros": ["Nguồn gốc xuất xứ rõ ràng từ các hộ nông sản bản địa", "Bí quyết nhận biết thịt trâu hun khói chuẩn", "Hướng dẫn đóng gói hút chân không mang về"]
    },
    {
        "id": "27-bacha-tourism-guide",
        "repo_name": "bacha-tourism-guide",
        "number": 27,
        "title": "Cẩm Nang Du Lịch Bắc Hà: Cao Nguyên Trắng Mộng Mơ",
        "brand": "Bắc Hà Highlands Guide",
        "tagline": "Khám phá Chợ phiên Bắc Hà sáng Chủ Nhật, Dinh thự Hoàng A Tưởng, thung lũng mận Tam Hoa",
        "domain": "bacha-tourism-guide.github.io",
        "icon_symbol": "🐎",
        "keywords": "du lịch bắc hà lào cai, chợ phiên bắc hà, dinh hoàng a tưởng, lễ hội đua ngựa bắc hà, homestay bắc hà",
        "cta_url": "https://laocaiview.vn",
        "cta_text": "Xem Bản Đồ Du Lịch & Nghỉ Dưỡng Toàn Tỉnh Trên LaoCaiView.vn",
        "category": "Văn Hóa & Chợ Phiên",
        "pros": ["Lịch trình khám phá chợ phiên lớn nhất Tây Bắc", "Tìm hiểu kiến trúc độc đáo Dinh Hoàng A Tưởng", "Thưởng thức thắng cố và rượu ngô nồng nàn"]
    },
    {
        "id": "28-spa-massage-sapa",
        "repo_name": "spa-massage-sapa",
        "number": 28,
        "title": "Địa Chỉ Tắm Lá Thuốc Dao Đỏ & Massage Trị Liệu Sa Pa",
        "brand": "SaPa Herbal & Wellness",
        "tagline": "Trải nghiệm ngâm bồn gỗ pơ mu thuốc lá Dao đỏ, massage bấm huyệt đá nóng phục hồi sức khỏe",
        "domain": "spa-massage-sapa.github.io",
        "icon_symbol": "🌿",
        "keywords": "tắm lá thuốc dao đỏ sapa, massage sapa giá rẻ, spa thảo dược sapa, trị liệu bấm huyệt sapa",
        "cta_url": "https://laocaiview.vn/dat-phong",
        "cta_text": "Đặt Khách Sạn & Spa Nghỉ Dưỡng Trị Liệu Trên LaoCaiView.vn",
        "category": "Sức Khỏe & Trị Liệu",
        "pros": ["Hơn 30 vị thảo mộc tự nhiên từ rừng Hoàng Liên", "Không gian thư giãn nhìn ra ruộng bậc thang", "Đội ngũ kỹ thuật viên người bản địa dày dặn kinh nghiệm"]
    },
    {
        "id": "29-trekking-trail-sapa",
        "repo_name": "trekking-trail-sapa",
        "number": 29,
        "title": "Cẩm Nang Trekking Lảo Thẩn, Ngũ Chỉ Sơn & Trail Sa Pa",
        "brand": "SaPa Trek & Trail Hub",
        "tagline": "Review các cung đường leo núi săn mây huyền thoại, giải chạy vượt núi VMM & kinh nghiệm chuẩn bị đồ",
        "domain": "trekking-trail-sapa.github.io",
        "icon_symbol": "🥾",
        "keywords": "trekking sapa, leo núi lảo thẩn y tý, ngũ chỉ sơn sapa, giải chạy vmm sapa trail, kinh nghiệm trekking",
        "cta_url": "https://laocaiview.vn/tin-tuc",
        "cta_text": "Xem Kinh Nghiệm & Tin Tức Du Lịch Mạo Hiểm Trên LaoCaiView.vn",
        "category": "Trekking & Mạo Hiểm",
        "pros": ["Cập nhật độ khó và cao độ từng đỉnh núi", "Kết nối đội ngũ Porter bản địa nhiệt tình", "Danh sách trang thiết bị leo núi thiết yếu"]
    },
    {
        "id": "30-shophouse-kdt-sapa",
        "repo_name": "shophouse-kdt-sapa",
        "number": 30,
        "title": "Đánh Giá Các Dự Án Shophouse & Khu Đô Thị Sa Pa 2026",
        "brand": "SaPa Urban & Shophouse",
        "tagline": "Phân tích quy hoạch Alphora Mường Hoa, Sa Pa City Hub, tiềm năng kinh doanh shophouse phố du lịch",
        "domain": "shophouse-kdt-sapa.github.io",
        "icon_symbol": "🏢",
        "keywords": "shophouse sapa 2026, dự án alphora mường hoa, khu đô thị sa pa, bán nhà phố thương mại sapa",
        "cta_url": "https://laocaiview.vn/bat-dong-san",
        "cta_text": "Tra Cứu Bảng Giá & Mặt Bằng Shophouse Sa Pa Mới Nhất Tại LaoCaiView.vn",
        "category": "Dự Án & Đô Thị",
        "pros": ["100% dự án có quy hoạch 1/500 minh bạch", "Khảo sát thực địa lưu lượng khách từng tuyến phố", "Đánh giá mô hình dòng tiền F&B và lưu trú"]
    }
]

HTML_TEMPLATE = """<!DOCTYPE html>
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
    <title>{title} | #{number} {brand}</title>
    <meta name="description" content="{tagline}. Dữ liệu kiểm định chính thức từ hệ sinh thái LaoCaiView.vn.">
    <meta name="keywords" content="{keywords}">
    
    <link rel="icon" type="image/svg+xml" href="favicon.svg">
    <link rel="canonical" href="{cta_url}">
    
    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{tagline}">
    <meta property="og:image" content="og-image.svg">
    <meta property="og:site_name" content="{brand}">
    
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {{ background-color: #030b20; color: #f5f6f7; font-family: 'Inter', system-ui, sans-serif; }}
        .glass {{ background: rgba(8, 19, 48, 0.85); backdrop-filter: blur(16px); border: 1px solid rgba(179, 144, 93, 0.25); }}
        .gold-gradient {{ background: linear-gradient(135deg, #e5c285 0%, #B3905D 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .btn-gold {{ background: linear-gradient(135deg, #B3905D 0%, #d4b47d 100%); color: #020818; font-weight: 800; }}
        .btn-gold:hover {{ background: #B3905D; transform: translateY(-2px); }}
    </style>
</head>
<body class="min-h-screen flex flex-col selection:bg-[#B3905D] selection:text-slate-950">
    <!-- Navbar -->
    <nav class="glass sticky top-0 z-50 px-4 py-3.5 border-b border-[#B3905D]/20">
        <div class="max-w-6xl mx-auto flex items-center justify-between">
            <a href="index.html" class="flex items-center gap-2.5 font-bold text-white text-base md:text-lg">
                <span class="text-2xl">{icon_symbol}</span>
                <span class="gold-gradient">{brand}</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-black bg-slate-900 text-[#e5c285] border border-[#B3905D]/30">#{number}</span>
            </a>
            <div class="flex items-center gap-3">
                <a href="tel:0918153986" class="hidden sm:flex items-center gap-1.5 text-xs font-bold text-[#e5c285] bg-slate-900/80 px-3.5 py-2 rounded-xl border border-[#B3905D]/30 hover:border-[#B3905D] transition">
                    <span>📞 0918.153.986</span>
                </a>
                <a href="{cta_url}" target="_blank" rel="dofollow" class="btn-gold px-4 py-2 rounded-xl text-xs transition shadow-lg flex items-center gap-1">
                    <span>Khám Phá LaoCaiView</span>
                    <span>↗</span>
                </a>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="flex-grow max-w-5xl mx-auto px-4 py-10 w-full space-y-8">
        <header class="space-y-4">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold bg-[#B3905D]/20 text-[#e5c285] border border-[#B3905D]/40">
                <span>{icon_symbol}</span>
                <span>Chuyên Mục: {category}</span>
            </div>
            <h1 class="text-2xl md:text-4xl lg:text-5xl font-black text-white leading-tight">
                {title}
            </h1>
            <p class="text-base md:text-lg text-slate-300 max-w-3xl leading-relaxed">
                {tagline}
            </p>
        </header>

        <!-- Key Features Cards -->
        <section class="grid grid-cols-1 md:grid-cols-3 gap-4">
            {pros_html}
        </section>

        <!-- In-depth Guide Section -->
        <section class="glass rounded-3xl p-6 md:p-8 space-y-6 border border-[#B3905D]/30">
            <h2 class="text-xl md:text-2xl font-bold text-white flex items-center gap-2 border-l-4 border-l-[#B3905D] pl-3">
                <span>🎯 TỔNG QUAN & LỢI THẾ CẠNH TRANH TẠI LÀO CAI - SA PA</span>
            </h2>
            <div class="prose prose-invert max-w-none text-slate-300 text-sm md:text-base leading-relaxed space-y-4">
                <p>
                    Khu vực Sa Pa và tỉnh Lào Cai đang bước vào giai đoạn bứt phá hạ tầng toàn diện với sự xuất hiện của các đại dự án nghìn tỷ, tuyến đường nối cao tốc Nội Bài - Lào Cai đi Sa Pa và sân bay quốc tế Sa Pa tương lai. Nhu cầu tìm kiếm thông tin về <strong>{keywords}</strong> ngày càng gia tăng mạnh mẽ từ cả du khách lẫn nhà đầu tư.
                </p>
                <p>
                    Trang chuyên đề <strong>{brand}</strong> tổng hợp dữ liệu thực địa, khảo sát thị trường chuẩn xác và liên kết trực tiếp với nền tảng thông tin số <strong>LaoCaiView.vn</strong> nhằm mang đến cho bạn góc nhìn minh bạch, đa chiều nhất.
                </p>
            </div>

            <!-- CTA Box -->
            <div class="p-6 rounded-2xl bg-gradient-to-r from-[#0c1c44] to-[#030b20] border-2 border-[#B3905D]/50 flex flex-col md:flex-row items-center justify-between gap-6">
                <div class="space-y-1 text-center md:text-left">
                    <span class="text-xs font-bold text-[#e5c285] uppercase tracking-wider">HỆ SINH THÁI LAOCAIVIEW.VN</span>
                    <h3 class="text-lg md:text-xl font-bold text-white">Tra Cứu Dữ Liệu Thực Địa Độc Quyền</h3>
                    <p class="text-xs text-slate-300">Hotline tư vấn trực tiếp: <a href="tel:0918153986" class="text-amber-300 font-bold hover:underline">0918.153.986</a></p>
                </div>
                <div class="flex flex-wrap gap-3">
                    <a href="tel:0918153986" class="px-5 py-3 rounded-xl bg-slate-900 border border-[#B3905D]/50 text-[#e5c285] text-xs font-bold hover:bg-slate-800 transition flex items-center gap-1.5">
                        <span>📞 Gọi 0918.153.986</span>
                    </a>
                    <a href="{cta_url}" target="_blank" rel="dofollow" class="btn-gold px-6 py-3 rounded-xl text-xs font-black transition flex items-center gap-1">
                        <span>{cta_text}</span>
                        <span>↗</span>
                    </a>
                </div>
            </div>
        </section>

        <!-- Recommended Real Estate & Travel Links -->
        <section class="glass rounded-3xl p-6 md:p-8 space-y-4 border border-[#B3905D]/20">
            <h3 class="text-lg font-bold text-white flex items-center gap-2">
                <span>🔗 LIÊN KẾT TRỌNG ĐIỂM HỆ SINH THÁI LAOCAIVIEW</span>
            </h3>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-3 text-xs">
                <a href="https://laocaiview.vn/bat-dong-san/du-an-alphora-muong-hoa-sa-pa" target="_blank" rel="dofollow" class="p-3.5 rounded-xl bg-slate-900/60 hover:bg-slate-900 border border-slate-800 text-slate-300 hover:text-[#e5c285] transition flex flex-col justify-between">
                    <span class="font-bold text-white">Dự Án 83ha Alphora Mường Hoa</span>
                    <span class="text-[10px] text-slate-400 mt-1">Đại đô thị nghỉ dưỡng Sa Pa</span>
                </a>
                <a href="https://laocaiview.vn/bat-dong-san/mat-bang-shophouse-lang-am-thuc-alphora-muong-hoa" target="_blank" rel="dofollow" class="p-3.5 rounded-xl bg-slate-900/60 hover:bg-slate-900 border border-slate-800 text-slate-300 hover:text-[#e5c285] transition flex flex-col justify-between">
                    <span class="font-bold text-white">31 Căn Shophouse Làng Ẩm Thực</span>
                    <span class="text-[10px] text-slate-400 mt-1">Mặt bằng kinh doanh F&B</span>
                </a>
                <a href="https://laocaiview.vn/bat-dong-san/mat-bang-biet-thu-intercontinental-sapa-resort" target="_blank" rel="dofollow" class="p-3.5 rounded-xl bg-slate-900/60 hover:bg-slate-900 border border-slate-800 text-slate-300 hover:text-[#e5c285] transition flex flex-col justify-between">
                    <span class="font-bold text-white">79 Biệt Thự InterContinental</span>
                    <span class="text-[10px] text-slate-400 mt-1">Dinh thự 5 sao IHG</span>
                </a>
                <a href="https://laocaiview.vn/tin-tuc/lang-am-thuc-quoc-te-alphora-muong-hoa-mot-diem-den-van-trai-nghiem" target="_blank" rel="dofollow" class="p-3.5 rounded-xl bg-slate-900/60 hover:bg-slate-900 border border-slate-800 text-slate-300 hover:text-[#e5c285] transition flex flex-col justify-between">
                    <span class="font-bold text-white">Tin Tức Làng Ẩm Thực</span>
                    <span class="text-[10px] text-slate-400 mt-1">Một điểm đến vạn trải nghiệm</span>
                </a>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="border-t border-[#B3905D]/20 bg-[#020818] py-8 text-center text-xs text-slate-400 space-y-3">
        <div class="max-w-5xl mx-auto px-4 flex flex-wrap items-center justify-between gap-4">
            <div class="flex items-center gap-2">
                <span class="text-xl">{icon_symbol}</span>
                <span class="font-bold text-white">{brand}</span>
                <span class="text-slate-400">• Vệ tinh #{number}</span>
            </div>
            <div class="flex gap-4 text-xs">
                <a href="{cta_url}" target="_blank" rel="dofollow" class="hover:text-[#e5c285] transition">LaoCaiView.vn</a>
                <a href="tel:0918153986" class="hover:text-[#e5c285] transition">Hotline: 0918.153.986</a>
                <a href="https://zalo.me/0918153986" target="_blank" class="hover:text-[#e5c285] transition">Zalo</a>
            </div>
        </div>
        <p class="text-[11px] text-slate-400">© 2026 {brand} - Một website thành viên trong mạng lưới giám tuyển dữ liệu Lào Cai & Sa Pa.</p>
    </footer>
</body>
</html>
"""

def generate_svg_favicon(symbol):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <rect width="100" height="100" rx="20" fill="#030b20"/>
  <circle cx="50" cy="50" r="44" stroke="#B3905D" stroke-width="3" fill="none"/>
  <text x="50%" y="55%" font-size="52" text-anchor="middle" dominant-baseline="central">{symbol}</text>
</svg>"""

def generate_og_image(brand, title, symbol):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">
  <rect width="1200" height="630" fill="#030b20"/>
  <rect x="20" y="20" width="1160" height="590" rx="24" fill="#081330" stroke="#B3905D" stroke-width="4"/>
  <text x="600" y="200" font-size="120" text-anchor="middle">{symbol}</text>
  <text x="600" y="320" font-size="44" font-weight="bold" fill="#e5c285" text-anchor="middle" font-family="sans-serif">{brand}</text>
  <text x="600" y="400" font-size="30" fill="#ffffff" text-anchor="middle" font-family="sans-serif">{title[:50]}</text>
  <text x="600" y="520" font-size="22" fill="#94a3b8" text-anchor="middle" font-family="sans-serif">Mạng Lưới Vệ Tinh SEO LaoCaiView.vn • Hotline: 0918.153.986</text>
</svg>"""

def create_and_deploy_satellites():
    created_list = []
    
    for item in SATELLITES_21_TO_30:
        dir_name = item["id"]
        repo_name = item["repo_name"]
        full_dir = os.path.join(SATELLITES_DIR, dir_name)
        os.makedirs(full_dir, exist_ok=True)
        
        # Build pros HTML
        pros_html = ""
        for p in item["pros"]:
            pros_html += f"""
            <div class="glass p-5 rounded-2xl border border-[#B3905D]/30 space-y-2">
                <div class="text-[#e5c285] font-bold text-sm flex items-center gap-1.5">
                    <span>✨</span> Lợi Thế Nổi Bật
                </div>
                <p class="text-xs text-slate-300 leading-relaxed">{p}</p>
            </div>
            """
            
        html_content = HTML_TEMPLATE.format(
            title=item["title"],
            brand=item["brand"],
            tagline=item["tagline"],
            number=item["number"],
            icon_symbol=item["icon_symbol"],
            category=item["category"],
            keywords=item["keywords"],
            cta_url=item["cta_url"],
            cta_text=item["cta_text"],
            pros_html=pros_html
        )
        
        # Write index.html
        with open(os.path.join(full_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_content)
            
        # Write favicon.svg
        with open(os.path.join(full_dir, "favicon.svg"), "w", encoding="utf-8") as f:
            f.write(generate_svg_favicon(item["icon_symbol"]))
            
        # Write og-image.svg
        with open(os.path.join(full_dir, "og-image.svg"), "w", encoding="utf-8") as f:
            f.write(generate_og_image(item["brand"], item["title"], item["icon_symbol"]))
            
        # Write robots.txt
        with open(os.path.join(full_dir, "robots.txt"), "w", encoding="utf-8") as f:
            f.write("User-agent: *\nAllow: /\nSitemap: sitemap.xml\n")
            
        # Write sitemap.xml
        with open(os.path.join(full_dir, "sitemap.xml"), "w", encoding="utf-8") as f:
            f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://bacnguyen0106.github.io/{repo_name}/</loc>
    <lastmod>{datetime.utcnow().strftime('%Y-%m-%d')}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>""")
            
        # Write README.md
        with open(os.path.join(full_dir, "README.md"), "w", encoding="utf-8") as f:
            f.write(f"# #{item['number']} - {item['brand']}\n\nWebsite vệ tinh chính thức: {item['title']}\nBacklink đích: {item['cta_url']}\nHotline: 0918.153.986\n")

        print(f"[{item['number']}] Initializing git for {repo_name}...")
        
        # Git operations
        git_dir = os.path.join(full_dir, ".git")
        if not os.path.exists(git_dir):
            subprocess.run("git init", cwd=full_dir, shell=True, capture_output=True)
            subprocess.run("git config user.name 'bacnguyen0106'", cwd=full_dir, shell=True, capture_output=True)
            subprocess.run("git config user.email 'bacnguyen0106@gmail.com'", cwd=full_dir, shell=True, capture_output=True)
            subprocess.run("git branch -M main", cwd=full_dir, shell=True, capture_output=True)
            
        subprocess.run("git add .", cwd=full_dir, shell=True, capture_output=True)
        subprocess.run('git commit -m "feat: init luxury LaoCaiView satellite website with hotline 0918153986"', cwd=full_dir, shell=True, capture_output=True)
        
        # Check if remote repo exists, create if not
        check_repo = subprocess.run(f"gh repo view bacnguyen0106/{repo_name}", shell=True, capture_output=True, text=True)
        if check_repo.returncode != 0:
            print(f"Creating GitHub repo bacnguyen0106/{repo_name}...")
            create_cmd = f"gh repo create bacnguyen0106/{repo_name} --public --source=. --remote=origin --push"
            subprocess.run(create_cmd, cwd=full_dir, shell=True, capture_output=True)
        else:
            print(f"Repo bacnguyen0106/{repo_name} already exists, pushing changes...")
            subprocess.run(f"git remote set-url origin https://github.com/bacnguyen0106/{repo_name}.git", cwd=full_dir, shell=True, capture_output=True)
            subprocess.run("git push -u origin main --force", cwd=full_dir, shell=True, capture_output=True)
            
        # Enable GitHub Pages
        print(f"Enabling GitHub Pages for bacnguyen0106/{repo_name}...")
        enable_pages_cmd = f'gh api repos/bacnguyen0106/{repo_name}/pages -X POST -f source[branch]=main -f source[path]=/'
        subprocess.run(enable_pages_cmd, shell=True, capture_output=True)
        
        live_url = f"https://bacnguyen0106.github.io/{repo_name}/"
        repo_url = f"https://github.com/bacnguyen0106/{repo_name}"
        created_list.append({
            "number": item["number"],
            "brand": item["brand"],
            "title": item["title"],
            "live_url": live_url,
            "repo_url": repo_url,
            "cta_url": item["cta_url"]
        })
        print(f"-> SUCCESS: #{item['number']} {item['brand']} => {live_url}")
        
    print("\n--- ALL 10 SATELLITES CREATED & DEPLOYED SUCCESSFULLY ---")
    return created_list

if __name__ == "__main__":
    create_and_deploy_satellites()
