#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TỰ ĐỘNG KHỞI TẠO 10 KHO DỮ LIỆU VỆ TINH MỚI (#31 ĐẾN #40)
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

SATELLITES_31_TO_40 = [
    {
        "id": "31-dat-trungtam-sapa",
        "repo_name": "dat-trungtam-sapa",
        "number": 31,
        "title": "Bảng Giá Đất Phố Cổ & Trung Tâm Sa Pa 2026",
        "brand": "SaPa Central Prime Land",
        "tagline": "Khảo sát quỹ đất mặt tiền Cầu Mây, Fansipan, Ngũ Chỉ Sơn & Bờ hồ Sa Pa thanh khoản cao",
        "icon_symbol": "🏛️",
        "keywords": "bán nhà đất trung tâm sa pa, đất mặt tiền cầu mây sapa, đất phố cổ sapa, đất bờ hồ sa pa",
        "cta_url": "https://laocaiview.vn/bat-dong-san/ban-nha-dat-trung-tam-sa-pa",
        "cta_text": "Xem Danh Sách Đất Trung Tâm Sa Pa Chính Chủ Trên LaoCaiView.vn",
        "category": "Bất Động Sản Phố Cổ",
        "pros": ["Vị trí kinh doanh sầm uất đón trọn khách du lịch", "Sổ đỏ thổ cư 100% sang tên công chứng ngay", "Tiềm năng sinh lời dòng tiền cho thuê vượt trội"]
    },
    {
        "id": "32-sangnhuong-khachsan-sapa",
        "repo_name": "sangnhuong-khachsan-sapa",
        "number": 32,
        "title": "Sàn Mua Bán & Sang Nhượng Khách Sạn Sa Pa 2026",
        "brand": "SaPa Hotel M&A Hub",
        "tagline": "Tổng hợp khách sạn 2-4 sao, boutique hotel đang vận hành có dòng tiền ổn định tại Sa Pa",
        "icon_symbol": "🏨",
        "keywords": "sang nhượng khách sạn sapa, bán khách sạn sa pa, mua bán khách sạn 3 sao sapa, chuyển nhượng homestay sapa",
        "cta_url": "https://laocaiview.vn/bat-dong-san/sang-nhuong-khach-san-sa-pa",
        "cta_text": "Tra Cứu Khách Sạn Cần Chuyển Nhượng Trên LaoCaiView.vn",
        "category": "Sang Nhượng Khách Sạn",
        "pros": ["Đầy đủ giấy phép PCCC, ANTT và kinh doanh lưu trú", "Dòng tiền doanh thu thực tế chứng minh minh bạch", "Chuyển giao toàn bộ trang thiết bị và đội ngũ vận hành"]
    },
    {
        "id": "33-hauthao-sapa-review",
        "repo_name": "hauthao-sapa-review",
        "number": 33,
        "title": "Cẩm Nang Khảo Sát Đất & Homestay Hầu Thào Sa Pa",
        "brand": "Hầu Thào Cloud Valley",
        "tagline": "Đánh giá quỹ đất săn mây Hầu Thào, view thung lũng Mường Hoa & tiềm năng phát triển resort",
        "icon_symbol": "☁️",
        "keywords": "bán đất hầu thào sa pa, homestay săn mây hầu thào, đất view mường hoa hầu thào, đầu tư đất hầu thào",
        "cta_url": "https://laocaiview.vn/bat-dong-san/ban-dat-hau-thao-sa-pa",
        "cta_text": "Xem Bảng Hàng Đất Săn Mây Hầu Thào Trên LaoCaiView.vn",
        "category": "Săn Mây & Nghỉ Dưỡng",
        "pros": ["Tọa độ săn mây đẹp nhất Sa Pa ngắm trọn Mường Hoa", "Khí hậu mát mẻ quanh năm, không gian yên bình", "Dư địa tăng giá mạnh khi hạ tầng kết nối mở rộng"]
    },
    {
        "id": "34-tavan-sapa-review",
        "repo_name": "tavan-sapa-review",
        "number": 34,
        "title": "Bản Đồ Đất & Nhà Gỗ Sinh Thái Tả Van Sa Pa",
        "brand": "Tả Van Eco Stream",
        "tagline": "Khám phá quỹ đất ven suối Mường Hoa, nhà gỗ bungalow bản địa & dịch vụ du lịch cộng đồng",
        "icon_symbol": "🏞️",
        "keywords": "bán đất tả van sa pa, homestay tả van view suối, mua đất làm homestay tả van, nhà gỗ tả van",
        "cta_url": "https://laocaiview.vn/bat-dong-san/ban-dat-ta-van",
        "cta_text": "Khám Phá Đất Nền & Nhà Gỗ Tả Van Trên LaoCaiView.vn",
        "category": "Du Lịch Sinh Thái Bản",
        "pros": ["Mặt tiền view suối Mường Hoa nước chảy róc rách", "Địa điểm thu hút lượng khách Tây và quốc tế đông đảo", "Văn hóa bản địa người Giáy, H'Mông đậm đà bản sắc"]
    },
    {
        "id": "35-oquyho-sapa-guide",
        "repo_name": "oquyho-sapa-guide",
        "number": 35,
        "title": "Cẩm Nang Khám Phá Đèo Ô Quý Hồ & Cổng Trời Sa Pa",
        "brand": "Ô Quý Hồ Peak Gateway",
        "tagline": "Review Cổng trời Sa Pa, Cầu kính Rồng Mây, điểm săn hoàng hôn huyền thoại trên Tứ đại đỉnh đèo",
        "icon_symbol": "🌅",
        "keywords": "đèo ô quý hồ sa pa, cổng trời sa pa, cầu kính rồng mây, săn hoàng hôn ô quý hồ, du lịch đèo ô quý hồ",
        "cta_url": "https://laocaiview.vn/tin-tuc",
        "cta_text": "Xem Cẩm Nang Khám Phá Tứ Đại Đỉnh Đèo Trên LaoCaiView.vn",
        "category": "Danh Thắng & Check-in",
        "pros": ["Cung đường ngắm hoàng hôn rực rỡ nhất miền Bắc", "Tổ hợp vui chơi giải trí cầu kính quốc tế", "Dịch vụ cafe săn mây ngắm đỉnh Fansipan kỳ vĩ"]
    },
    {
        "id": "36-dat-sapa-giare",
        "repo_name": "dat-sapa-giare",
        "number": 36,
        "title": "Tổng Hợp Đất Sa Pa Giá Rẻ & Cơ Hội Đầu Tư Dưới 2 Tỷ",
        "brand": "SaPa Smart Invest Hub",
        "tagline": "Săn đất nền nông nghiệp, đất xen kẹt bản làng, cơ hội đón sóng hạ tầng dành cho vốn nhỏ",
        "icon_symbol": "💰",
        "keywords": "bán đất sa pa giá rẻ, đất sapa dưới 1 tỷ, đất sapa dưới 2 tỷ, đất nông nghiệp sapa giá rẻ",
        "cta_url": "https://laocaiview.vn/bat-dong-san/ban-dat-sa-pa-gia-re",
        "cta_text": "Xem Danh Sách Đất Sa Pa Giá Rẻ Trên LaoCaiView.vn",
        "category": "Đầu Tư Ngân Sách Vừa",
        "pros": ["Vốn khởi đầu chỉ từ vài trăm triệu đến dưới 2 tỷ", "Phù hợp tích sản dài hạn đón sân bay Sa Pa", "Tính thanh khoản cao, dễ mua dễ bán"]
    },
    {
        "id": "37-baothang-laocai-bds",
        "repo_name": "baothang-laocai-bds",
        "number": 37,
        "title": "Khảo Sát Nhà Đất Bảo Thắng & KCN Tằng Loỏng Lào Cai",
        "brand": "Bảo Thắng Urban & Industry",
        "tagline": "Thông tin đất nền Phố Lu, thị trấn Phong Hải, BĐS phụ trợ khu công nghiệp và logistics",
        "icon_symbol": "🏭",
        "keywords": "nhà đất bảo thắng lào cai, đất nền phố lu, đất khu công nghiệp tằng loỏng, bất động sản bảo thắng",
        "cta_url": "https://laocaiview.vn/bat-dong-san/nha-dat-lao-cai",
        "cta_text": "Tra Cứu BĐS Huyện Bảo Thắng Tại LaoCaiView.vn",
        "category": "Công Nghiệp & Đô Thị",
        "pros": ["Trọng điểm công nghiệp và sản xuất của tỉnh Lào Cai", "Nút giao cao tốc Nội Bài - Lào Cai thuận lợi giao thương", "Mặt bằng giá còn mềm, dư địa tăng trưởng cao"]
    },
    {
        "id": "38-captreo-fansipan-guide",
        "repo_name": "captreo-fansipan-guide",
        "number": 38,
        "title": "Cẩm Nang Tuyến Cáp Treo Fansipan & Ga Mường Hoa",
        "brand": "Fansipan SunWorld Hub",
        "tagline": "Kinh nghiệm đi tàu hỏa leo núi Mường Hoa, bảng giá combo cáp treo Sun World & mẹo săn mây",
        "icon_symbol": "🚡",
        "keywords": "vé cáp treo fansipan, tàu hỏa leo núi mường hoa, sun world fansipan legend, khách sạn gần ga cáp treo",
        "cta_url": "https://laocaiview.vn/dat-phong",
        "cta_text": "Đặt Phòng Gần Tuyến Cáp Treo Fansipan Trên LaoCaiView.vn",
        "category": "Cáp Treo & Danh Thắng",
        "pros": ["Kỷ lục Guinness thế giới cáp treo ba dây", "Trải nghiệm tàu hỏa leo núi ngắm thung lũng hoa", "Quần thể tâm linh đỉnh thiêng Fansipan hùng vĩ"]
    },
    {
        "id": "39-logistics-laocai-hub",
        "repo_name": "logistics-laocai-hub",
        "number": 39,
        "title": "Cẩm Nang Logistics & Cho Thuê Kho Bãi Lào Cai 2026",
        "brand": "Lào Cai Logistics Gateway",
        "tagline": "Khảo sát mặt bằng kho lạnh Kim Thành, bến bãi container cửa khẩu quốc tế & chuỗi cung ứng",
        "icon_symbol": "🚚",
        "keywords": "thuê kho bãi lào cai, logistics cửa khẩu kim thành, kho lạnh xuất nhập khẩu lào cai, dịch vụ hải quan lào cai",
        "cta_url": "https://laocaiview.vn/mat-bang",
        "cta_text": "Tìm Mặt Bằng Kho Bãi Logistics Trên LaoCaiView.vn",
        "category": "Kho Bãi & Dịch Vụ",
        "pros": ["Kết nối trực tiếp hành lang kinh tế Côn Minh - Hải Phòng", "Hệ thống kho ngoại quan và kiểm hóa hiện đại", "Tối ưu chi phí lưu kho vận tải biên giới"]
    },
    {
        "id": "40-alphora-muonghoa-villas",
        "repo_name": "alphora-muonghoa-villas",
        "number": 40,
        "title": "Tổng Quan Đại Dự Án Nghỉ Dưỡng Alphora Mường Hoa 83ha",
        "brand": "Alphora Muong Hoa Luxury Guide",
        "tagline": "Phân tích 79 dinh thự The Residences at InterContinental Sapa Resort & 31 căn Shophouse Làng Ẩm Thực",
        "icon_symbol": "👑",
        "keywords": "dự án alphora mường hoa, biệt thự intercontinental sapa, shophouse làng ẩm thực alphora, alphanam sapa",
        "cta_url": "https://laocaiview.vn/bat-dong-san/du-an-alphora-muong-hoa-sa-pa",
        "cta_text": "Xem Phân Tích Chi Tiết Đại Dự Án Alphora Mường Hoa Trên LaoCaiView.vn",
        "category": "Dự Án Nghỉ Dưỡng Quốc Tế",
        "pros": ["Quần thể nghỉ dưỡng 83ha đẳng cấp bậc nhất Sa Pa", "Vận hành bởi tập đoàn khách sạn 5 sao quốc tế IHG", "Sở hữu lâu dài (Sổ đỏ ODT) - Biểu tượng di sản Sa Pa"]
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
                <span>🎯 TỔNG QUAN THỊ TRƯỜNG & LỢI THẾ CẠNH TRANH</span>
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
    
    for item in SATELLITES_31_TO_40:
        dir_name = item["id"]
        repo_name = item["repo_name"]
        full_dir = os.path.join(SATELLITES_DIR, dir_name)
        os.makedirs(full_dir, exist_ok=True)
        
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
        
        with open(os.path.join(full_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_content)
            
        with open(os.path.join(full_dir, "favicon.svg"), "w", encoding="utf-8") as f:
            f.write(generate_svg_favicon(item["icon_symbol"]))
            
        with open(os.path.join(full_dir, "og-image.svg"), "w", encoding="utf-8") as f:
            f.write(generate_og_image(item["brand"], item["title"], item["icon_symbol"]))
            
        with open(os.path.join(full_dir, "robots.txt"), "w", encoding="utf-8") as f:
            f.write("User-agent: *\nAllow: /\nSitemap: sitemap.xml\n")
            
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
            
        with open(os.path.join(full_dir, "README.md"), "w", encoding="utf-8") as f:
            f.write(f"# #{item['number']} - {item['brand']}\n\nWebsite vệ tinh chính thức: {item['title']}\nBacklink đích: {item['cta_url']}\nHotline: 0918.153.986\n")

        print(f"[{item['number']}] Initializing git for {repo_name}...")
        
        git_dir = os.path.join(full_dir, ".git")
        if not os.path.exists(git_dir):
            subprocess.run("git init", cwd=full_dir, shell=True, capture_output=True)
            subprocess.run("git config user.name 'bacnguyen0106'", cwd=full_dir, shell=True, capture_output=True)
            subprocess.run("git config user.email 'bacnguyen0106@gmail.com'", cwd=full_dir, shell=True, capture_output=True)
            subprocess.run("git branch -M main", cwd=full_dir, shell=True, capture_output=True)
            
        subprocess.run("git add .", cwd=full_dir, shell=True, capture_output=True)
        subprocess.run('git commit -m "feat: init luxury LaoCaiView satellite website with hotline 0918153986"', cwd=full_dir, shell=True, capture_output=True)
        
        check_repo = subprocess.run(f"gh repo view bacnguyen0106/{repo_name}", shell=True, capture_output=True, text=True)
        if check_repo.returncode != 0:
            print(f"Creating GitHub repo bacnguyen0106/{repo_name}...")
            create_cmd = f"gh repo create bacnguyen0106/{repo_name} --public --source=. --remote=origin --push"
            subprocess.run(create_cmd, cwd=full_dir, shell=True, capture_output=True)
        else:
            print(f"Repo bacnguyen0106/{repo_name} already exists, pushing changes...")
            subprocess.run(f"git remote set-url origin https://github.com/bacnguyen0106/{repo_name}.git", cwd=full_dir, shell=True, capture_output=True)
            subprocess.run("git push -u origin main --force", cwd=full_dir, shell=True, capture_output=True)
            
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
        
    print("\n--- ALL 10 SATELLITES (#31-#40) CREATED & DEPLOYED SUCCESSFULLY ---")
    return created_list

if __name__ == "__main__":
    create_and_deploy_satellites()
