import os

BASE_URL = "https://jaketroubleshoots.com"
GUIDE_FOLDER = "./guides"   # folder where your guide files are

urls = []

for file in os.listdir(GUIDE_FOLDER):
    if file.endswith(".html"):
        slug = file.replace(".html", "")
        urls.append(f"{BASE_URL}/guides/{slug}")

sitemap = ['<?xml version="1.0" encoding="UTF-8"?>']
sitemap.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

# homepage
sitemap.append("<url>")
sitemap.append(f"<loc>{BASE_URL}</loc>")
sitemap.append("</url>")

for url in urls:
    sitemap.append("<url>")
    sitemap.append(f"<loc>{url}</loc>")
    sitemap.append("</url>")

sitemap.append("</urlset>")

with open("sitemap.xml", "w") as f:
    f.write("\n".join(sitemap))

print("Sitemap generated!")