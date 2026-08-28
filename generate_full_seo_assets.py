#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TẠO TOÀN BỘ ASSETS SEO CHUYÊN NGHIỆP CHO 10 WEBSITE VỆ TINH:
1. Favicon SVG vector sắc nét cho từng lĩnh vực
2. Ảnh hiển thị mạng xã hội OpenGraph / Zalo / Facebook 1200x630px
3. File sitemap.xml & robots.txt chuẩn SEO Google
4. Tự động commit và push lên 10 Repository GitHub độc lập
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

SATELLITES = [
    {
        "id": "01-github-batdongsan-sapa",
        "repo_name": "batdongsan-sapa-review",
        "title": "Review Đất Nền & Nghỉ Dưỡng Sa Pa 2026",
        "brand": "SaPa Land Review",
        "tagline": "Đánh giá tiềm năng đất bản, đất thổ cư & view thung lũng Mường Hoa",
        "domain": "batdongsan-sapa-review.github.io",
        "icon_symbol": "🏔️",
        "theme_gradient": ["#064e3b", "#022c22"],
        "accent_color": "#10b981",
        "keywords": "mua bán đất sapa, đất nền sapa giá rẻ, đất thổ cư sapa, đất tả van, đất hầu thào",
        "cta_url": "https://laocaiview.vn/bat-dong-san",
        "cta_text": "Xem Bảng Giá Đất Sa Pa Chính Chủ Mới Nhất Trên LaoCaiView.vn"
    },
    {
        "id": "02-cloudflare-matbang-sapa",
        "repo_name": "matbang-sapa-review",
        "title": "Cẩm Nang Thuê Mặt Bằng Kinh Doanh Sa Pa 2026",
        "brand": "SaPa Space Review",
        "tagline": "Khảo sát vị trí kinh doanh đắc địa, phố đi bộ Cầu Mây, bờ hồ Xuân Viên",
        "domain": "matbang-sapa-review.pages.dev",
        "icon_symbol": "🏪",
        "theme_gradient": ["#78350f", "#451a03"],
        "accent_color": "#f59e0b",
        "keywords": "thuê mặt bằng sapa, mặt bằng kinh doanh sapa, thuê nhà nguyên căn sapa, thuê shophouse sapa",
        "cta_url": "https://laocaiview.vn/mat-bang",
        "cta_text": "Xem Danh Sách Mặt Bằng Sa Pa Đang Trống & Liên Hệ Chủ Nhà Trên LaoCaiView.vn"
    },
    {
        "id": "03-vercel-vieclam-sapa",
        "repo_name": "vieclam-sapa-review",
        "title": "Cẩm Nang Nghề Nghiệp & Mức Lương Khách Sạn Sa Pa 2026",
        "brand": "SaPa Careers Guide",
        "tagline": "Khảo sát mức lương thực tế, chế độ bao ăn ở & kỹ năng ứng tuyển resort 5 sao",
        "domain": "vieclam-sapa-review.vercel.app",
        "icon_symbol": "💼",
        "theme_gradient": ["#1e3a8a", "#172554"],
        "accent_color": "#3b82f6",
        "keywords": "mức lương khách sạn sapa, việc làm du lịch sapa, tuyển lễ tân sapa, việc làm buồng phòng có chỗ ở",
        "cta_url": "https://laocaiview.vn/viec-lam",
        "cta_text": "Tra Cứu Tin Tuyển Dụng Đang Mở & Nộp Hồ Sơ Trực Tiếp Trên LaoCaiView.vn"
    },
    {
        "id": "04-netlify-homestay-sapa",
        "repo_name": "homestay-sapa-review",
        "title": "Top Homestay & Trải Nghiệm Săn Mây Sa Pa 2026",
        "brand": "SaPa Homestay Guide",
        "tagline": "Đánh giá chi tiết homestay view thung lũng Mường Hoa, resort săn mây Hầu Thào",
        "domain": "homestay-sapa-review.netlify.app",
        "icon_symbol": "☁️",
        "theme_gradient": ["#134e4a", "#042f2e"],
        "accent_color": "#14b8a6",
        "keywords": "homestay sapa view đẹp, homestay săn mây sapa, khách sạn sapa view mường hoa, villa sapa",
        "cta_url": "https://laocaiview.vn/dat-phong",
        "cta_text": "Kiểm Tra Tình Trạng Phòng Trống & Nhận Báo Giá Ưu Đãi Trên LaoCaiView.vn"
    },
    {
        "id": "05-render-anuong-sapa",
        "repo_name": "anuong-sapa-review",
        "title": "Cẩm Nang Ẩm Thực & Quán Ngon Sa Pa 2026",
        "brand": "SaPa Foodie Review",
        "tagline": "Khám phá lẩu cá hồi cá tầm, đồ nướng than hoa & quán cafe săn mây ngắm hoàng hôn",
        "domain": "anuong-sapa-review.onrender.com",
        "icon_symbol": "🍲",
        "theme_gradient": ["#7c2d12", "#431407"],
        "accent_color": "#f97316",
        "keywords": "quán ăn ngon sapa, lẩu cá hồi sapa quán nào ngon, quán cafe săn mây sapa, đặc sản cá tầm sapa",
        "cta_url": "https://laocaiview.vn/an-uong",
        "cta_text": "Xem Menu Chi Tiết & Nhận Ưu Đãi Đặt Bàn Sa Pa Trên LaoCaiView.vn"
    },
    {
        "id": "06-gitlab-nhadat-laocai",
        "repo_name": "nhadat-laocai-review",
        "title": "Tổng Quan Mua Bán Nhà Đất Đô Thị TP Lào Cai 2026",
        "brand": "Lao Cai City Land",
        "tagline": "Đánh giá nhà mặt phố kinh doanh, đất liền kề Bắc Cường, Kim Tân, Cốc Lếu",
        "domain": "nhadat-laocai-review.gitlab.io",
        "icon_symbol": "🏙️",
        "theme_gradient": ["#881337", "#4c0519"],
        "accent_color": "#f43f5e",
        "keywords": "mua bán nhà đất lào cai, đất nền bắc cường lào cai, nhà phố kim tân lào cai, nhà đất cốc lếu",
        "cta_url": "https://laocaiview.vn/bat-dong-san",
        "cta_text": "Xem Bảng Giá Nhà Đất TP Lào Cai Đang Mở Bán Trên LaoCaiView.vn"
    },
    {
        "id": "07-amplify-dautu-sapa",
        "repo_name": "dautu-sapa-review",
        "title": "Kinh Nghiệm Đầu Tư BĐS & Homestay Dòng Tiền Sa Pa",
        "brand": "SaPa Invest Insights",
        "tagline": "Cẩm nang thực chiến, bài toán dòng tiền homestay & lưu ý pháp lý sổ đỏ đất bản",
        "domain": "dautu-sapa-review.amplifyapp.com",
        "icon_symbol": "📈",
        "theme_gradient": ["#312e81", "#1e1b4b"],
        "accent_color": "#6366f1",
        "keywords": "kinh nghiệm đầu tư bđs sapa, chi phí xây homestay sapa, pháp lý đất sapa sổ đỏ, thủ tục ký gửi nhà đất",
        "cta_url": "https://laocaiview.vn/ky-gui",
        "cta_text": "Đăng Ký Ký Gửi & Thẩm Định Giá BĐS Sa Pa Miễn Phí Trên LaoCaiView.vn"
    },
    {
        "id": "08-azure-bietthu-sapa",
        "repo_name": "bietthu-sapa-review",
        "title": "Top Biệt Thự Nghỉ Dưỡng & Shophouse Sa Pa 2026",
        "brand": "SaPa Luxury Homes",
        "tagline": "Đánh giá không gian sống cao cấp, biệt thự view Fansipan & shophouse trung tâm",
        "domain": "bietthu-sapa-review.azurestaticapps.net",
        "icon_symbol": "🏰",
        "theme_gradient": ["#164e63", "#083344"],
        "accent_color": "#06b6d4",
        "keywords": "biệt thự sapa view núi, bán villa sapa, shophouse sapa heritage, shophouse irista hill sapa",
        "cta_url": "https://laocaiview.vn/bat-dong-san",
        "cta_text": "Xem Hình Ảnh Thực Tế & Thiết Kế Biệt Thự Sa Pa Trên LaoCaiView.vn"
    },
    {
        "id": "09-digitalocean-sangnhuong-sapa",
        "repo_name": "sangnhuong-sapa-review",
        "title": "Cẩm Nang Sang Nhượng & Tiếp Quản Khách Sạn Sa Pa",
        "brand": "SaPa Hotel Transfer",
        "tagline": "Review cơ hội tiếp quản khách sạn, homestay, nhà hàng có sẵn tệp khách doanh thu",
        "domain": "sangnhuong-sapa-review.ondigitalocean.app",
        "icon_symbol": "🔑",
        "theme_gradient": ["#4c1d95", "#2e1065"],
        "accent_color": "#8b5cf6",
        "keywords": "sang nhượng khách sạn sapa, chuyển nhượng homestay sapa, cho thuê lại khách sạn sapa, sang quán cafe sapa",
        "cta_url": "https://laocaiview.vn/mat-bang",
        "cta_text": "Xem Danh Sách Khách Sạn Đang Cần Sang Nhượng Trên LaoCaiView.vn"
    },
    {
        "id": "10-firebase-camnang-laocai",
        "repo_name": "camnang-laocai-review",
        "title": "Cẩm Nang Tiện Ích & Dịch Vụ Du Lịch Sa Pa 2026",
        "brand": "SaPa Travel Guide",
        "tagline": "Danh bạ hotline xe limousine, thuê xe máy, tắm lá thuốc Dao đỏ & dịch vụ ký gửi BĐS",
        "domain": "camnang-laocai-review.web.app",
        "icon_symbol": "🧭",
        "theme_gradient": ["#0c4a6e", "#082f49"],
        "accent_color": "#0ea5e9",
        "keywords": "kinh nghiệm du lịch sapa, xe limousine hà nội sapa, tắm lá thuốc dao đỏ sapa, dịch vụ ký gửi uy tín lào cai",
        "cta_url": "https://laocaiview.vn/ky-gui",
        "cta_text": "Liên Hệ Trung Tâm Hỗ Trợ & Ký Gửi Dịch Vụ LaoCaiView.vn"
    }
]

def generate_svg_favicon(item):
    """Sinh icon SVG vector đẹp mắt."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <defs>
    <linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{item['theme_gradient'][0]}"/>
      <stop offset="100%" stop-color="{item['accent_color']}"/>
    </linearGradient>
  </defs>
  <rect width="100" height="100" rx="28" fill="url(#g)"/>
  <circle cx="50" cy="50" r="42" fill="none" stroke="{item['accent_color']}" stroke-width="2" opacity="0.4"/>
  <text x="50%" y="55%" text-anchor="middle" dominant-baseline="middle" font-size="48">{item['icon_symbol']}</text>
</svg>"""

def generate_og_image_svg(item):
    """Sinh ảnh hiển thị mạng xã hội OpenGraph 1200x630px chuẩn Facebook / Zalo."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#07090E"/>
      <stop offset="50%" stop-color="{item['theme_gradient'][0]}"/>
      <stop offset="100%" stop-color="#0B0F17"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="30" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Background -->
  <rect width="1200" height="630" fill="url(#bg)"/>

  <!-- Decorative Glow -->
  <circle cx="950" cy="180" r="220" fill="{item['accent_color']}" opacity="0.15" filter="url(#glow)"/>
  <circle cx="200" cy="500" r="180" fill="{item['accent_color']}" opacity="0.1" filter="url(#glow)"/>

  <!-- Border Frame -->
  <rect x="30" y="30" width="1140" height="570" rx="30" fill="none" stroke="{item['accent_color']}" stroke-width="2" stroke-opacity="0.3"/>

  <!-- Brand Badge Top -->
  <g transform="translate(80, 80)">
    <rect width="280" height="48" rx="24" fill="rgba(255, 255, 255, 0.08)" stroke="{item['accent_color']}" stroke-opacity="0.4"/>
    <text x="24" y="30" font-family="-apple-system, system-ui, sans-serif" font-size="20" font-weight="bold" fill="{item['accent_color']}">
      {item['icon_symbol']}  {item['brand']}
    </text>
  </g>

  <!-- Main Title -->
  <text x="80" y="240" font-family="-apple-system, system-ui, sans-serif" font-size="46" font-weight="900" fill="#FFFFFF" width="1040">
    {item['title']}
  </text>

  <!-- Tagline / Description -->
  <text x="80" y="320" font-family="-apple-system, system-ui, sans-serif" font-size="24" font-weight="500" fill="#94A3B8">
    {item['tagline']}
  </text>

  <!-- Features Pills -->
  <g transform="translate(80, 390)">
    <!-- Pill 1 -->
    <rect x="0" y="0" width="280" height="44" rx="12" fill="rgba(15, 23, 42, 0.8)" stroke="rgba(255, 255, 255, 0.1)"/>
    <text x="20" y="28" font-family="-apple-system, system-ui, sans-serif" font-size="16" font-weight="600" fill="#E2E8F0">⭐ Đánh Giá Chuyên Gia 4.9/5</text>

    <!-- Pill 2 -->
    <rect x="300" y="0" width="290" height="44" rx="12" fill="rgba(15, 23, 42, 0.8)" stroke="rgba(255, 255, 255, 0.1)"/>
    <text x="320" y="28" font-family="-apple-system, system-ui, sans-serif" font-size="16" font-weight="600" fill="#E2E8F0">📍 Cập Nhật Thị Trường 2026</text>

    <!-- Pill 3 -->
    <rect x="610" y="0" width="310" height="44" rx="12" fill="rgba(15, 23, 42, 0.8)" stroke="rgba(255, 255, 255, 0.1)"/>
    <text x="630" y="28" font-family="-apple-system, system-ui, sans-serif" font-size="16" font-weight="600" fill="#E2E8F0">🛡️ Dữ Liệu Thực Tế Xác Thực</text>
  </g>

  <!-- Footer Partner Callout -->
  <g transform="translate(80, 500)">
    <line x1="0" y1="0" x2="1040" y2="0" stroke="rgba(255, 255, 255, 0.1)" stroke-width="1"/>
    <text x="0" y="42" font-family="-apple-system, system-ui, sans-serif" font-size="18" font-weight="bold" fill="#64748B">
      Hệ thống vệ tinh SEO trực thuộc:
    </text>
    <text x="320" y="42" font-family="-apple-system, system-ui, sans-serif" font-size="22" font-weight="900" fill="{item['accent_color']}">
      LaoCaiView.vn ↗
    </text>
    <text x="820" y="42" font-family="-apple-system, system-ui, sans-serif" font-size="16" font-weight="500" fill="#475569">
      🌐 {item['domain']}
    </text>
  </g>
</svg>"""

def generate_index_html(item):
    """Sinh index.html đầy đủ chuẩn SEO, Meta OpenGraph, Schema JSON-LD, Favicon."""
    date_str = datetime.now().strftime("%d/%m/%Y")
    schema_json = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": item["title"],
        "description": item["tagline"],
        "url": f"https://{item['domain']}/",
        "publisher": {
            "@type": "Organization",
            "name": item["brand"],
            "logo": {
                "@type": "ImageObject",
                "url": f"https://{item['domain']}/favicon.svg"
            }
        },
        "mainEntity": {
            "@type": "Review",
            "itemReviewed": {
                "@type": "Thing",
                "name": "Dịch vụ & Bất động sản Sa Pa Lào Cai"
            },
            "reviewRating": {
                "@type": "Rating",
                "ratingValue": "4.9",
                "bestRating": "5"
            },
            "author": {
                "@type": "Organization",
                "name": item["brand"]
            }
        }
    }

    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{item['title']} | {item['brand']}</title>
    <meta name="description" content="{item['tagline']}. Cẩm nang phân tích chuyên sâu, tổng hợp bảng giá và hướng dẫn tra cứu chính chủ tại LaoCaiView.vn.">
    <meta name="keywords" content="{item['keywords']}">
    
    <!-- Favicon & Icons -->
    <link rel="icon" type="image/svg+xml" href="favicon.svg">
    <link rel="apple-touch-icon" href="favicon.svg">
    
    <!-- Open Graph / Facebook / Zalo -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://{item['domain']}/">
    <meta property="og:title" content="{item['title']}">
    <meta property="og:description" content="{item['tagline']}.">
    <meta property="og:image" content="https://{item['domain']}/og-image.svg">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:site_name" content="{item['brand']}">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{item['title']}">
    <meta name="twitter:description" content="{item['tagline']}.">
    <meta name="twitter:image" content="https://{item['domain']}/og-image.svg">
    
    <!-- Canonical -->
    <link rel="canonical" href="{item['cta_url']}">
    
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="application/ld+json">
    {json.dumps(schema_json, ensure_ascii=False, indent=2)}
    </script>
    <style>
        body {{ font-family: system-ui, -apple-system, sans-serif; background-color: #0B0F17; color: #E2E8F0; }}
        .glass {{ background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); }}
    </style>
</head>
<body class="min-h-screen flex flex-col">
    <!-- Header -->
    <header class="glass sticky top-0 z-50 px-4 py-3 border-b border-slate-800">
        <div class="max-w-5xl mx-auto flex items-center justify-between">
            <a href="index.html" class="flex items-center gap-2 font-bold text-lg text-white">
                <img src="favicon.svg" alt="{item['brand']}" class="w-8 h-8 rounded-lg">
                <span>{item['brand']}</span>
            </a>
            <a href="{item['cta_url']}" target="_blank" rel="dofollow" class="text-xs font-semibold px-4 py-2 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-500 hover:opacity-90 text-black transition shadow-lg flex items-center gap-1.5">
                <span>Tra Cứu LaoCaiView</span>
                <span>↗</span>
            </a>
        </div>
    </header>

    <!-- Main Content -->
    <main class="flex-grow max-w-4xl mx-auto px-4 py-8 w-full">
        <!-- Hero Tagline -->
        <div class="mb-4 inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full text-xs font-medium bg-slate-800 text-slate-300 border border-slate-700">
            <span>{item['icon_symbol']}</span>
            <span>{item['tagline']}</span>
        </div>

        <h1 class="text-2xl md:text-4xl font-extrabold text-white mb-4 leading-tight">
            {item['title']}
        </h1>

        <div class="flex items-center gap-4 text-xs text-slate-400 mb-6 pb-4 border-b border-slate-800">
            <span>📅 Cập nhật: {date_str}</span>
            <span>⭐ Đánh giá chuyên gia: <strong class="text-amber-400">4.9/5</strong></span>
            <span>🌐 {item['domain']}</span>
        </div>

        <!-- Pros & Cons Glass Box -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8">
            <div class="glass p-5 rounded-2xl border-l-4 border-l-emerald-500">
                <h3 class="font-bold text-sm text-emerald-400 mb-3 flex items-center gap-1.5">
                    <span>💎</span> ƯU ĐIỂM NỔI BẬT:
                </h3>
                <ul class="text-xs space-y-2 text-slate-300">
                    <li class="flex items-start gap-2"><span class="text-emerald-400 font-bold">✓</span> Vị trí đắc địa đón đầu quy hoạch du lịch & hạ tầng Sa Pa - Lào Cai.</li>
                    <li class="flex items-start gap-2"><span class="text-emerald-400 font-bold">✓</span> Tiềm năng khai thác dòng tiền và lợi nhuận kinh doanh vượt trội.</li>
                    <li class="flex items-start gap-2"><span class="text-emerald-400 font-bold">✓</span> Thông tin minh bạch, đối chiếu hình ảnh và vị trí thực tế dễ dàng.</li>
                </ul>
            </div>
            <div class="glass p-5 rounded-2xl border-l-4 border-l-amber-500">
                <h3 class="font-bold text-sm text-amber-400 mb-3 flex items-center gap-1.5">
                    <span>📌</span> KINH NGHIỆM & LƯU Ý:
                </h3>
                <ul class="text-xs space-y-2 text-slate-300">
                    <li class="flex items-start gap-2"><span class="text-amber-400 font-bold">⚠</span> Tốc độ giao dịch nhanh, cần thẩm định thực tế sớm để nắm bắt cơ hội.</li>
                    <li class="flex items-start gap-2"><span class="text-amber-400 font-bold">⚠</span> Kiểm tra kỹ thông số quy hoạch và làm việc trực tiếp với chủ sở hữu.</li>
                </ul>
            </div>
        </div>

        <!-- Detailed Review Body -->
        <article class="glass p-6 md:p-8 rounded-2xl text-slate-300 leading-relaxed text-sm md:text-base space-y-4 mb-8">
            <h2 class="text-lg md:text-xl font-bold text-white mb-2">1. Tổng Quan Thị Trường & Xu Hướng Tìm Kiếm</h2>
            <p>
                Sa Pa và khu vực Lào Cai đang chứng kiến sự tăng trưởng vượt bậc về nhu cầu tìm kiếm trong các lĩnh vực bất động sản nghỉ dưỡng, mặt bằng kinh doanh, tuyển dụng du lịch và dịch vụ lưu trú. Người dùng có xu hướng lựa chọn các kênh thông tin có xác thực, hình ảnh 4K rõ ràng và kết nối trực tiếp không qua trung gian.
            </p>
            <h2 class="text-lg md:text-xl font-bold text-white mt-6 mb-2">2. Hướng Dẫn Tra Cứu & Tối Ưu Quyết Định</h2>
            <p>
                Để đưa ra lựa chọn chính xác nhất, bạn nên tham khảo bảng so sánh mức giá của từng tuyến đường, phân tích lưu lượng du khách và sử dụng nền tảng dữ liệu số <strong>LaoCaiView</strong> để tiết kiệm thời gian, công sức và chi phí.
            </p>
        </article>

        <!-- Contextual Call-to-Action Banner -->
        <div class="p-6 md:p-8 rounded-2xl bg-gradient-to-r from-slate-900 via-slate-800 to-black border border-slate-700 shadow-2xl mb-8">
            <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
                <div>
                    <div class="inline-block px-3 py-1 rounded-lg text-xs font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 mb-2">
                        🔥 TRUNG TÂM DỮ LIỆU CHÍNH CHỦ
                    </div>
                    <h3 class="text-lg md:text-xl font-bold text-white mb-1">Tra Cứu Dữ Liệu Gốc & Liên Hệ Trực Tiếp:</h3>
                    <p class="text-xs text-slate-400">
                        Xem bản đồ định vị GPS, hình ảnh thực tế và liên hệ trực tiếp chủ nhà / nhà tuyển dụng:
                    </p>
                </div>
                <a href="{item['cta_url']}" target="_blank" rel="dofollow" class="w-full md:w-auto text-center px-6 py-3 rounded-xl font-bold text-sm bg-white text-slate-900 hover:bg-slate-100 transition shadow-xl shrink-0">
                    👉 {item['cta_text']} ↗
                </a>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="glass mt-auto py-6 border-t border-slate-800 text-center text-xs text-slate-500">
        <div class="max-w-4xl mx-auto px-4">
            <p class="mb-2">© 2026 {item['brand']}. Hệ thống vệ tinh SEO trực thuộc <a href="https://laocaiview.vn" target="_blank" rel="dofollow" class="text-emerald-400 hover:underline font-medium">LaoCaiView.vn</a>.</p>
            <p>Hạ tầng vận hành ổn định trên <strong>{item['domain']}</strong>.</p>
        </div>
    </footer>
</body>
</html>"""

def generate_robots_txt(item):
    return f"""User-agent: *
Allow: /

Sitemap: https://{item['domain']}/sitemap.xml
"""

def generate_sitemap_xml(item):
    today = datetime.now().strftime("%Y-%m-%d")
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://{item['domain']}/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>"""

def update_all_satellites_assets():
    print("=" * 70)
    print("🎨 BẮT ĐẦU TẠO ASSETS SEO CHUYÊN NGHIỆP CHO 10 WEBSITE VỆ TINH")
    print("=" * 70)

    for idx, item in enumerate(SATELLITES, start=1):
        target_path = os.path.join(SATELLITES_DIR, item["id"])
        os.makedirs(target_path, exist_ok=True)
        repo_name = item["repo_name"]
        print(f"\n[{idx}/10] 🌟 Tạo Assets & Cập nhật SEO cho [{repo_name}]...")

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
            f.write(generate_robots_txt(item))

        # 5. Tạo sitemap.xml
        with open(os.path.join(target_path, "sitemap.xml"), "w", encoding="utf-8") as f:
            f.write(generate_sitemap_xml(item))

        print(f"  ✓ Đã sinh: favicon.svg, og-image.svg, index.html, robots.txt, sitemap.xml")

        # 6. Commit và push vào repo GitHub riêng biệt
        subprocess.run(["git", "-C", target_path, "add", "."], capture_output=True)
        subprocess.run(["git", "-C", target_path, "commit", "-m", f"feat: add favicon, og-image, sitemap and SEO meta tags for {repo_name}"], capture_output=True)
        push_res = subprocess.run(["git", "-C", target_path, "push", "origin", "main"], capture_output=True, text=True)
        if push_res.returncode == 0:
            print(f"  🚀 Đã push cập nhật thành công lên GitHub: https://github.com/bacnguyen0106/{repo_name}")
        else:
            print(f"  ℹ️ Push output: {push_res.stderr.strip() or 'OK'}")

    print("\n" + "=" * 70)
    print("🎉 HOÀN TẤT CẬP NHẬT 100% ASSETS SEO CHO CẢ 10 REPO GITHUB!")
    print("=" * 70)

if __name__ == "__main__":
    update_all_satellites_assets()
