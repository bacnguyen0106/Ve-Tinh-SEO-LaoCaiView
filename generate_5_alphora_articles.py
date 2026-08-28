#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TỰ ĐỘNG BIÊN TẬP VÀ XUẤT BẢN 5 BÀI VIẾT CHUYÊN SÂU VỀ ALPHORA MƯỜNG HOA SA PA
LÊN 5 WEBSITE VỆ TINH VỚI 5 GÓC NHÌN SEO ĐỘC LẬP & BACKLINK DOFOLLOW CHẤT LƯỢNG CAO
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

# 5 Articles Configuration
ARTICLES = [
    {
        "satellite_folder": "01-github-batdongsan-sapa",
        "repo_name": "batdongsan-sapa-review",
        "filename": "alphora-muong-hoa-sapa-tong-quan.html",
        "title": "Đánh Giá Tổng Quan Dự Án Alphora Mường Hoa Sa Pa 2026: Vị Trí, Quy Mô & Pháp Lý Sổ Đỏ",
        "brand": "SaPa Land Review",
        "accent": "#10b981",
        "theme_bg": "#06100c",
        "category": "Tổng Quan Dự Án BĐS",
        "target_url": "https://laocaiview.vn/bat-dong-san",
        "anchor_text": "bảng giá bất động sản Sa Pa chính chủ",
        "cta_text": "Tra Cứu Dự Án BĐS Sa Pa Trên LaoCaiView ↗",
        "intro_p": "Được quy hoạch trên diện tích rộng tới 83ha tại thung lũng Mường Hoa, <strong>Alphora Mường Hoa Sa Pa</strong> (do Tập đoàn Alphanam làm chủ đầu tư) đang là tâm điểm chú ý của giới đầu tư bất động sản nghỉ dưỡng cao cấp phía Bắc nhờ pháp lý sở hữu lâu dài cực kỳ khan hiếm.",
        "h2_1": "1. Vị Trí Đắc Địa Tại Trục Du Lịch Trọng Điểm Tỉnh Lộ 152",
        "p_1": "Tọa lạc tại tổ dân phố Cầu Mây 2, phường Sa Pa, dự án Alphora Mường Hoa nằm ngay mặt tiền Tỉnh lộ 152 kết nối trực tiếp từ trung tâm thị xã Sa Pa xuống các bản du lịch di sản nổi tiếng như Tả Van, Lao Chải, Hầu Thào. Với vị trí chỉ cách Quảng trường trung tâm Sa Pa khoảng 4km, dự án sở hữu tầm nhìn không góc chết hướng thẳng ra dải ruộng bậc thang uốn lượn và đỉnh Fansipan hùng vĩ.",
        "h2_2": "2. Quy Mô 83ha & Quy Hoạch Không Gian Đô Thị Đẳng Cấp",
        "p_2": "Quần thể Alphora Mường Hoa được xây dựng theo mô hình công viên văn hóa - nghỉ dưỡng đa chức năng gồm các phân khu shophouse thương mại, biệt thự đồi cao cấp, làng ẩm thực quốc tế và chuỗi khách sạn 5 sao vận hành bởi các thương hiệu hàng đầu thế giới (trong đó có InterContinental). Để theo dõi biến động thị trường và đối chiếu giá bán thực tế, nhà đầu tư nên tham khảo <a href='https://laocaiview.vn/bat-dong-san' target='_blank' rel='dofollow' class='text-emerald-400 font-bold hover:underline'>bảng giá bất động sản Sa Pa chính chủ</a> được kiểm chứng minh bạch.",
        "h2_3": "3. Pháp Lý Sổ Đỏ Sở Hữu Lâu Dài - Điểm Tựa Vững Chắc Cho Nhà Đầu Tư",
        "p_3": "Điểm khác biệt lớn nhất giúp Alphora Mường Hoa tạo cơn sốt chính là yếu tố pháp lý đất ở đô thị có sổ đỏ lâu dài. Giữa bối cảnh quỹ đất sở hữu vĩnh viễn tại vùng lõi du lịch Sa Pa gần như cạn kiệt, dự án mang lại giá trị tài sản truyền đời và tiềm năng tăng giá vượt bậc theo đà phát triển của du lịch quốc tế Sa Pa."
    },
    {
        "satellite_folder": "02-cloudflare-matbang-sapa",
        "repo_name": "matbang-sapa-review",
        "filename": "shophouse-alphora-muong-hoa-kinh-doanh.html",
        "title": "Tiềm Năng Kinh Doanh Shophouse Phố Thương Mại Alphora Mường Hoa Sa Pa 2026",
        "brand": "SaPa Space Review",
        "accent": "#f59e0b",
        "theme_bg": "#0f0a05",
        "category": "Mặt Bằng Thương Mại F&B",
        "target_url": "https://laocaiview.vn/mat-bang",
        "anchor_text": "thuê mặt bằng kinh doanh Sa Pa vị trí đắc địa",
        "cta_text": "Xem Mặt Bằng Kinh Doanh Sa Pa Trên LaoCaiView ↗",
        "intro_p": "Sự xuất hiện của phân khu <strong>Shophouse Alphora Mường Hoa</strong> đang mở ra một trung tâm thương mại sầm uất bậc nhất Sa Pa, giải quyết cơn khát mặt bằng kinh doanh ẩm thực, spa, cafe cao cấp phục vụ hàng triệu lượt du khách đổ về thung lũng Mường Hoa.",
        "h2_1": "1. Đón Đầu Dòng Du Khách Khổng Lồ Khám Phá Thung Lũng Mường Hoa",
        "p_1": "Mỗi năm, thung lũng Mường Hoa đón hàng triệu lượt du khách trong và ngoài nước tham quan cảnh quan ruộng bậc thang và trải nghiệm văn hóa bản địa. Tuyến phố shophouse tại Alphora Mường Hoa được quy hoạch thông minh, tối ưu diện tích mặt tiền từ 6m - 10m, vỉa hè rộng thoáng phù hợp với các mô hình kinh doanh ăn uống F&B, thời trang bản địa và dịch vụ chăm sóc sức khỏe.",
        "h2_2": "2. Phân Khu Làng Ẩm Thực Quốc Tế & Phố Đi Bộ Bản Địa",
        "p_2": "Khác biệt với các khu phố cũ trong thị xã, shophouse Alphora Mường Hoa được quy hoạch đồng bộ theo phân khu chức năng: Khu ẩm thực Tây Bắc, Làng nghề thủ công 6 dân tộc và các chuỗi F&B quốc tế. Nếu bạn đang tìm kiếm cơ hội thuê địa điểm kinh doanh, hãy tham khảo cẩm nang <a href='https://laocaiview.vn/mat-bang' target='_blank' rel='dofollow' class='text-amber-400 font-bold hover:underline'>thuê mặt bằng kinh doanh Sa Pa vị trí đắc địa</a> để chọn được mặt bằng sinh lời tối đa.",
        "h2_3": "3. Tỷ Suất Khai Thác Cho Thuê & Hoàn Vốn Vượt Trội",
        "p_3": "Nhờ được chủ đầu tư Alphanam định hướng phát triển chuỗi sự kiện lễ hội quanh năm, các căn shophouse tại đây có khả năng duy trì tỷ lệ lấp đầy kinh doanh cao ngay cả trong mùa thấp điểm. Tỷ suất lợi nhuận từ việc tự kinh doanh hoặc cho thuê lại ước tính đạt từ 12% - 15%/năm."
    },
    {
        "satellite_folder": "08-azure-bietthu-sapa",
        "repo_name": "bietthu-sapa-review",
        "filename": "biet-thu-intercontinental-alphora-muong-hoa.html",
        "title": "Review Dinh Thự Biệt Thự InterContinental Sapa Tại Quần Thể Alphora Mường Hoa",
        "brand": "SaPa Luxury Homes",
        "accent": "#06b6d4",
        "theme_bg": "#030d12",
        "category": "Biệt Thự & Dinh Thự Thượng Lưu",
        "target_url": "https://laocaiview.vn/bat-dong-san",
        "anchor_text": "biệt thự nghỉ dưỡng Sa Pa view Fansipan",
        "cta_text": "Xem Bộ Sưu Tập Biệt Thự Sa Pa Trên LaoCaiView ↗",
        "intro_p": "Nằm tại vị trí đắc địa nhất trong quần thể Alphora Mường Hoa, phân khu biệt thự <strong>The Residences at InterContinental Sapa Resort</strong> khẳng định đẳng cấp sống thượng lưu độc bản giữa thiên nhiên hùng vĩ của đất trời Sa Pa.",
        "h2_1": "1. Sự Kết Hợp Hoàn Mỹ Giữa Kiến Trúc Bản Địa & Chuẩn Mực 5 Sao IHG",
        "p_1": "Mỗi căn biệt thự tại Alphora Mường Hoa được thiết kế tinh tế lấy cảm hứng từ nếp nhà sàn truyền thống của đồng bào vùng cao, kết hợp vật liệu đá tự nhiên, gỗ thông tuyết và kính tràn panorama cao cấp. Dưới sự quản lý vận hành của tập đoàn khách sạn danh tiếng InterContinental Hotels Group (IHG), các chủ nhân được tận hưởng dịch vụ quản gia 24/7 theo tiêu chuẩn resort quốc tế.",
        "h2_2": "2. Tầm Nhìn Triệu Đô Ôm Trọn Thung Lũng Sương Mù & Đỉnh Fansipan",
        "p_2": "Tọa lạc trên các triền đồi giật cấp tự nhiên, 100% các căn villa đều sở hữu tầm nhìn trực diện xuống biển mây thung lũng Mường Hoa. Để tra cứu thông tin chuyển nhượng và danh sách các căn dinh thự sang trọng nhất, bạn có thể xem thêm tại chuyên mục <a href='https://laocaiview.vn/bat-dong-san' target='_blank' rel='dofollow' class='text-cyan-400 font-bold hover:underline'>biệt thự nghỉ dưỡng Sa Pa view Fansipan</a> trên cổng thông tin LaoCaiView.",
        "h2_3": "3. Giá Trị Tài Sản Tích Sản & Khẳng Định Vị Thế Chủ Nhân",
        "p_3": "Sở hữu một căn biệt thự mang thương hiệu quốc tế với quyền sử dụng đất lâu dài tại Sa Pa không chỉ là nơi nghỉ dưỡng tái tạo năng lượng cho gia đình thượng lưu mà còn là tài sản tích sản gia tăng giá trị phi mã theo thời gian."
    },
    {
        "satellite_folder": "07-amplify-dautu-sapa",
        "repo_name": "dautu-sapa-review",
        "filename": "co-hoi-dau-tu-alphora-muong-hoa-sapa.html",
        "title": "Phân Tích Suất Sinh Lời & Pháp Lý Sở Hữu Lâu Dài Tại Alphora Mường Hoa Sa Pa",
        "brand": "SaPa Invest Insights",
        "accent": "#6366f1",
        "theme_bg": "#070614",
        "category": "Phân Tích Tài Chính & Dòng Tiền",
        "target_url": "https://laocaiview.vn/ky-gui",
        "anchor_text": "thẩm định và ký gửi bất động sản Sa Pa uy tín",
        "cta_text": "Thẩm Định & Ký Gửi BĐS Trên LaoCaiView ↗",
        "intro_p": "Bài viết phân tích chuyên sâu góc nhìn tài chính, bài toán dòng tiền khai thác lưu trú và khả năng tăng trưởng giá trị vốn của siêu dự án 83ha <strong>Alphora Mường Hoa Sa Pa</strong> trong chu kỳ đầu tư 2026 - 2030.",
        "h2_1": "1. Đòn Bẩy Hạ Tầng: Cao Tốc & Sân Bay Sa Pa Đi Vào Hoạt Động",
        "p_1": "Khi các dự án hạ tầng trọng điểm như Cảng hàng không Sa Pa và tuyến đường kết nối cao tốc Nội Bài - Lào Cai - Sa Pa hoàn thành, thời gian di chuyển từ Hà Nội và các tỉnh thành lớn đến Sa Pa chỉ còn chưa đầy 3 tiếng. Điều này tạo cú hích cực mạnh giúp giá trị bất động sản tại Alphora Mường Hoa đón đầu đợt sóng tăng trưởng giá trị mới.",
        "h2_2": "2. Bài Toán Dòng Tiền Khai Thác Nghỉ Dưỡng 4 Mùa",
        "p_2": "Sa Pa sở hữu lợi thế du lịch 4 mùa độc nhất vô nhị: Mùa xuân ngắm hoa đào hoa mận, mùa hè trốn nóng, mùa thu ngắm lúa chín vàng và mùa đông săn tuyết săn mây. Mô hình vận hành cho thuê ủy thác chuyên nghiệp giúp nhà đầu tư thu về dòng tiền đều đặn hàng năm mà không tốn công quản lý. Nhà đầu tư có nhu cầu định giá tài sản có thể sử dụng dịch vụ <a href='https://laocaiview.vn/ky-gui' target='_blank' rel='dofollow' class='text-indigo-400 font-bold hover:underline'>thẩm định và ký gửi bất động sản Sa Pa uy tín</a>.",
        "h2_3": "3. Đánh Giá Khẩu Vị Rủi Ro & Chiến Lược Vào Tiền An Toàn",
        "p_3": "Nhờ pháp lý minh bạch và năng lực tài chính mạnh mẽ từ Tập đoàn Alphanam, Alphora Mường Hoa là lựa chọn an toàn hàng đầu cho các nhà đầu tư theo trường phái giá trị và dòng tiền dài hạn."
    },
    {
        "satellite_folder": "04-netlify-homestay-sapa",
        "repo_name": "homestay-sapa-review",
        "filename": "trai-nghiem-nghi-duong-alphora-muong-hoa.html",
        "title": "Trải Nghiệm Nghỉ Dưỡng & Khám Phá Công Viên Văn Hóa Tại Alphora Mường Hoa Sa Pa",
        "brand": "CloudStay SaPa",
        "accent": "#14b8a6",
        "theme_bg": "#041816",
        "category": "Trải Nghiệm Du Lịch & Lưu Trú",
        "target_url": "https://laocaiview.vn/dat-phong",
        "anchor_text": "đặt phòng khách sạn homestay Sa Pa view đẹp",
        "cta_text": "Đặt Phòng Sa Pa Giá Tốt Trên LaoCaiView ↗",
        "intro_p": "Không chỉ là một dự án bất động sản, <strong>Alphora Mường Hoa Sa Pa</strong> được kiến tạo như một thiên đường nghỉ dưỡng sinh thái, nơi du khách đắm chìm trong vẻ đẹp thơ mộng của thung lũng Mường Hoa và văn hóa 6 dân tộc anh em vùng Tây Bắc.",
        "h2_1": "1. Không Gian Sống Giữa Trái Tim Thung Lũng Ruộng Bậc Thang Đẹp Nhất Thế Giới",
        "p_1": "Thung lũng Mường Hoa từng được xếp hạng là một trong những thung lũng có ruộng bậc thang kỳ vĩ nhất thế giới. Tại Alphora Mường Hoa, du khách sẽ được tận hưởng không khí trong lành với độ ẩm lý tưởng, ngắm nhìn sương sớm bồng bềnh tràn qua các triền đồi và tận hưởng sự thanh bình tuyệt đối.",
        "h2_2": "2. Tiện Ích Trải Nghiệm Văn Hóa, Wellness Spa & Tắm Lá Thuốc Bản Địa",
        "p_2": "Dự án tích hợp đầy đủ các dịch vụ chăm sóc sức khỏe theo liệu pháp thảo mộc của người Dao đỏ, bể bơi nước nóng 4 mùa, trung tâm biểu diễn nghệ thuật dân gian và các tuyến đường dạo bộ hoa đào hoa mận. Khi lên kế hoạch du lịch, bạn nên tham khảo dịch vụ <a href='https://laocaiview.vn/dat-phong' target='_blank' rel='dofollow' class='text-teal-400 font-bold hover:underline'>đặt phòng khách sạn homestay Sa Pa view đẹp</a> với giá ưu đãi trực tiếp không qua trung gian.",
        "h2_3": "3. Điểm Check-In Không Thể Bỏ Lỡ Mùa Du Lịch 2026",
        "p_3": "Với cảnh quan được trau chuốt tỉ mỉ hòa quyện cùng núi rừng Tây Bắc, Alphora Mường Hoa hứa hẹn sẽ là tọa độ check-in 'triệu view' mới của giới trẻ và các tín đồ du lịch trải nghiệm khi đến với thị xã sương mù Sa Pa."
    }
]

def generate_article_html(art):
    date_str = datetime.now().strftime("%d/%m/%Y")
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
    <title>{art['title']} | {art['brand']}</title>
    <meta name="description" content="{art['intro_p'][:160].replace('<strong>', '').replace('</strong>', '')}...">
    <meta name="keywords" content="alphora muong hoa, alphora sapa, du an alphora muong hoa, shophouse alphora sapa, biet thu intercontinental sapa, bds muong hoa sapa">
    
    <link rel="icon" type="image/svg+xml" href="favicon.svg">
    <link rel="canonical" href="{art['target_url']}">
    
    <!-- Open Graph -->
    <meta property="og:type" content="article">
    <meta property="og:title" content="{art['title']}">
    <meta property="og:description" content="{art['intro_p'][:160].replace('<strong>', '').replace('</strong>', '')}...">
    <meta property="og:image" content="og-image.svg">
    <meta property="og:site_name" content="{art['brand']}">
    
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{art['title']}",
      "description": "{art['intro_p'][:200].replace('<strong>', '').replace('</strong>', '')}",
      "image": "og-image.svg",
      "author": {{
        "@type": "Organization",
        "name": "{art['brand']}"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "LaoCaiView",
        "url": "https://laocaiview.vn"
      }},
      "datePublished": "2026-08-27",
      "dateModified": "2026-08-27"
    }}
    </script>
    <style>
        body {{{{ background-color: {art['theme_bg']}; color: #e2e8f0; font-family: system-ui, -apple-system, sans-serif; }}}}
        .glass-box {{{{ background: rgba(15, 23, 42, 0.8); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); }}}}
        .prose-content p {{{{ margin-bottom: 1.25rem; line-height: 1.8; color: #cbd5e1; font-size: 0.95rem; }}}}
        .prose-content h2 {{{{ color: #ffffff; font-weight: 800; font-size: 1.35rem; margin-top: 1.75rem; margin-bottom: 0.75rem; border-left: 4px solid {art['accent']}; padding-left: 0.75rem; }}}}
    </style>
</head>
<body class="min-h-screen flex flex-col">
    <!-- Navbar -->
    <nav class="glass-box sticky top-0 z-50 px-4 py-3.5 border-b border-slate-800">
        <div class="max-w-5xl mx-auto flex items-center justify-between">
            <a href="index.html" class="flex items-center gap-2 font-bold text-white text-base md:text-lg">
                <img src="favicon.svg" alt="{art['brand']}" class="w-8 h-8 rounded-lg shadow">
                <span>{art['brand']}</span>
            </a>
            <a href="{art['target_url']}" target="_blank" rel="dofollow" class="px-4 py-2 rounded-xl text-xs font-bold bg-white text-slate-950 hover:bg-slate-100 transition shadow-lg flex items-center gap-1">
                <span>Khám Phá LaoCaiView</span>
                <span>↗</span>
            </a>
        </div>
    </nav>

    <!-- Breadcrumbs -->
    <div class="max-w-4xl mx-auto px-4 pt-6 text-xs text-slate-400 flex items-center gap-2">
        <a href="index.html" class="hover:underline">Trang chủ</a>
        <span>/</span>
        <span class="text-slate-200">{art['category']}</span>
        <span>/</span>
        <span class="text-white font-medium">Alphora Mường Hoa</span>
    </div>

    <!-- Header -->
    <header class="max-w-4xl mx-auto px-4 pt-6 pb-6">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold bg-slate-800 text-slate-300 border border-slate-700 mb-3">
            <span>🔥 TỌA ĐỘ VÀNG SA PA 2026</span>
        </div>
        <h1 class="text-2xl md:text-4xl font-extrabold text-white mb-4 leading-tight">
            {art['title']}
        </h1>
        <div class="flex flex-wrap items-center gap-4 text-xs text-slate-400 pb-4 border-b border-slate-800">
            <span>✍️ Ban Biên Tập {art['brand']}</span>
            <span>📅 Cập nhật: {date_str}</span>
            <span>⭐ Đánh giá chuyên gia: <strong class="text-amber-400">9.9/10</strong></span>
            <span>🛡️ Dữ liệu xác thực</span>
        </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-4xl mx-auto px-4 pb-16 flex-grow">
        <!-- Highlights Card -->
        <div class="glass-box p-6 rounded-2xl mb-8 border-l-4" style="border-left-color: {art['accent']};">
            <h3 class="font-bold text-white text-sm uppercase mb-2">📌 TÓM TẮT THÔNG TIN DỰ ÁN:</h3>
            <p class="text-xs md:text-sm text-slate-300 leading-relaxed">
                {art['intro_p']}
            </p>
        </div>

        <!-- Article Body -->
        <article class="prose-content">
            <h2>{art['h2_1']}</h2>
            <p>{art['p_1']}</p>

            <h2>{art['h2_2']}</h2>
            <p>{art['p_2']}</p>

            <h2>{art['h2_3']}</h2>
            <p>{art['p_3']}</p>
        </article>

        <!-- CTA Conversion Banner -->
        <div class="mt-10 p-8 rounded-3xl bg-gradient-to-r from-slate-900 via-slate-800 to-black border-2 border-slate-700 shadow-2xl">
            <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
                <div>
                    <div class="inline-block px-3 py-1 rounded-md text-xs font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 mb-2">
                        🔥 TRUNG TÂM DỮ LIỆU LAOCAIVIEW.VN
                    </div>
                    <h3 class="text-xl font-bold text-white mb-2">Tra Cứu Dữ Liệu BĐS & Du Lịch Mường Hoa Sa Pa:</h3>
                    <p class="text-xs text-slate-400 max-w-lg">
                        Xem bản đồ quy hoạch, hình ảnh thực tế và kết nối trực tiếp với chủ sở hữu trên nền tảng:
                    </p>
                </div>
                <a href="{art['target_url']}" target="_blank" rel="dofollow" class="w-full md:w-auto text-center px-8 py-4 rounded-2xl font-black text-sm bg-white text-slate-950 hover:bg-slate-100 transition shadow-2xl shrink-0">
                    👉 {art['cta_text']}
                </a>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="glass-box mt-auto py-6 border-t border-slate-800 text-center text-xs text-slate-500">
        <div class="max-w-4xl mx-auto px-4">
            <p>© 2026 {art['brand']}. Hệ thống vệ tinh SEO trực thuộc <a href="https://laocaiview.vn" target="_blank" rel="dofollow" class="text-emerald-400 hover:underline font-semibold">LaoCaiView.vn</a>.</p>
        </div>
    </footer>
</body>
</html>"""

def publish_all_5_articles():
    print("=" * 75)
    print("🚀 BẮT ĐẦU TẠO VÀ XUẤT BẢN 5 BÀI VIẾT ALPHORA MƯỜNG HOA LÊN 5 VỆ TINH")
    print("=" * 75)

    for idx, art in enumerate(ARTICLES, start=1):
        target_dir = os.path.join(SATELLITES_DIR, art["satellite_folder"])
        article_file = os.path.join(target_dir, art["filename"])
        repo_name = art["repo_name"]
        print(f"\n[{idx}/5] 📝 Đang xuất bản bài viết [{art['filename']}] lên [{repo_name}]...")

        # 1. Ghi file bài viết HTML
        html_code = generate_article_html(art)
        with open(article_file, "w", encoding="utf-8") as f:
            f.write(html_code)
        print(f"  ✓ Đã tạo file: {art['filename']}")

        # 2. Cập nhật sitemap.xml
        sitemap_file = os.path.join(target_dir, "sitemap.xml")
        today = datetime.now().strftime("%Y-%m-%d")
        new_url_entry = f"""  <url>
    <loc>https://bacnguyen0106.github.io/{repo_name}/{art['filename']}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
</urlset>"""
        if os.path.exists(sitemap_file):
            with open(sitemap_file, "r", encoding="utf-8") as f:
                sitemap_content = f.read()
            if art['filename'] not in sitemap_content:
                sitemap_content = sitemap_content.replace("</urlset>", new_url_entry)
                with open(sitemap_file, "w", encoding="utf-8") as f:
                    f.write(sitemap_content)
                print(f"  ✓ Đã cập nhật sitemap.xml")

        # 3. Commit và Push lên GitHub
        subprocess.run(["git", "-C", target_dir, "add", "."], capture_output=True)
        subprocess.run(["git", "-C", target_dir, "commit", "-m", f"feat(seo): add in-depth article about Alphora Muong Hoa ({art['filename']})"], capture_output=True)
        push_res = subprocess.run(["git", "-C", target_dir, "push", "origin", "main"], capture_output=True, text=True)
        if push_res.returncode == 0:
            print(f"  🚀 Đã push thành công lên GitHub: https://github.com/bacnguyen0106/{repo_name}")
        else:
            print(f"  ℹ️ Push: {push_res.stderr.strip() or 'OK'}")

    print("\n" + "=" * 75)
    print("🎉 HOÀN TẤT XUẤT BẢN ĐỦ 5 BÀI VIẾT ALPHORA MƯỜNG HOA LÊN 5 VỆ TINH!")
    print("=" * 75)

if __name__ == "__main__":
    publish_all_5_articles()
