import os
import sys
import io
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SATELLITES_DIR = os.path.join(SCRIPT_DIR, "satellites")

ARTICLES_UPDATE = [
    ("01-github-batdongsan-sapa", "alphora-muong-hoa-sapa-tong-quan.html"),
    ("02-cloudflare-matbang-sapa", "shophouse-alphora-muong-hoa-kinh-doanh.html"),
    ("08-azure-bietthu-sapa", "biet-thu-intercontinental-alphora-muong-hoa.html"),
    ("07-amplify-dautu-sapa", "co-hoi-dau-tu-alphora-muong-hoa-sapa.html"),
    ("04-netlify-homestay-sapa", "trai-nghiem-nghi-duong-alphora-muong-hoa.html"),
]

for folder, fname in ARTICLES_UPDATE:
    fpath = os.path.join(SATELLITES_DIR, folder, fname)
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Link directly to the new dedicated project page
        content = content.replace("https://laocaiview.vn/bat-dong-san", "https://laocaiview.vn/bat-dong-san/du-an-alphora-muong-hoa-sa-pa")
        
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
            
        subprocess.run(["git", "-C", os.path.join(SATELLITES_DIR, folder), "add", fname], capture_output=True)
        subprocess.run(["git", "-C", os.path.join(SATELLITES_DIR, folder), "commit", "-m", f"seo: update backlink target to https://laocaiview.vn/bat-dong-san/du-an-alphora-muong-hoa-sa-pa"], capture_output=True)
        subprocess.run(["git", "-C", os.path.join(SATELLITES_DIR, folder), "push", "origin", "main"], capture_output=True)
        print(f"Updated backlink in {folder}/{fname}")
