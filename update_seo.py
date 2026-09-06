import os, re, subprocess
from datetime import date

today = date.today().isoformat()
base_url = "https://lebserval-art.github.io"

with open("robots.txt", "w", encoding="utf-8") as f:
 f.write(f"User-agent: *\nAllow: /\n\nSitemap: {base_url}/sitemap.xml\n")

urls = ["", "/about.html", "/contacts.html", "/privacy.html",
 "/articles/top-obd2-scanners-2026.html", "/articles/top-dashcams-2026.html",
 "/articles/top-powerbanks-2026.html", "/articles/top-robot-vacuums-2026.html"]

items = [f"  <url>\n    <loc>{base_url}{p}</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>{'1.0' if p=='' else ('0.8' if '/articles/' in p else '0.5')}</priority>\n  </url>" for p in urls]

with open("sitemap.xml", "w", encoding="utf-8") as f:
 f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(items) + "\n</urlset>\n")

def get_footer(sub=False):
 p = "../" if sub else ""
 return f'''<footer class="site-footer"><div class="container footer-content"><div class="footer-col"><h4>ТехноГид</h4><p>Честные обзоры гаджетов, электроники и автотоваров.</p></div><div class="footer-col"><h4>Навигация</h4><ul><li><a href="{p}index.html">Все обзоры</a></li><li><a href="{p}about.html">О проекте</a></li><li><a href="{p}contacts.html">Контакты</a></li><li><a href="{p}privacy.html">Политика конфиденциальности</a></li></ul></div><div class="footer-col"><h4>Информация</h4><p class="disclaimer">Сайт может содержать партнерские ссылки.</p><p class="copy">© 2026 ТехноГид.</p></div></div></footer>'''

targets = [("index.html", False), ("articles/top-obd2-scanners-2026.html", True), ("articles/top-dashcams-2026.html", True), ("articles/top-powerbanks-2026.html", True), ("articles/top-robot-vacuums-2026.html", True)]

for path, sub in targets:
 if os.path.exists(path):
  with open(path, "r", encoding="utf-8") as f: c = f.read()
  ft = get_footer(sub)
  c = re.sub(r'<footer[\s\S]*?</footer>', ft, c) if "<footer" in c else c.replace("</body>", f"{ft}\n</body>")
  with open(path, "w", encoding="utf-8") as f: f.write(c)

subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", "Add robots.txt, sitemap.xml and update footers"], check=True)
subprocess.run(["git", "push", "origin", "master"], check=True)
print("SUCCESS_SEO_UPDATED")
