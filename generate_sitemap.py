from pathlib import Path

BASE_URL = "https://jaketroubleshoots.com"
ROOT = Path(__file__).resolve().parent

urls = [f"{BASE_URL}/"]
for path in sorted(ROOT.rglob("*.html")):
    if ".git" in path.parts:
        continue
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        continue
    urls.append(f"{BASE_URL}/{rel}")

sitemap = ['<?xml version="1.0" encoding="UTF-8"?>']
sitemap.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
for url in urls:
    sitemap.append("<url>")
    sitemap.append(f"<loc>{url}</loc>")
    sitemap.append("</url>")
sitemap.append("</urlset>")

(ROOT / "sitemap.xml").write_text("\n".join(sitemap) + "\n")
print(f"Sitemap generated with {len(urls)} URLs.")
