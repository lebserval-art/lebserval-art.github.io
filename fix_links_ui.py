import os
import re
import subprocess

# 1. Дополняем CSS нормальными стилями для ссылок и кнопок в статьях
css_append = """

/* Article & Links Styling */
a {
 color: #38bdf8;
 text-decoration: none;
}

a:hover {
 color: #7dd3fc;
 text-decoration: underline;
}

.article-full a, .content-page a {
 color: #38bdf8;
}

.btn, a.btn, a.read-more {
 display: inline-block;
 padding: 10px 18px;
 border-radius: 8px;
 font-weight: 600;
 text-decoration: none !important;
 transition: all 0.2s ease;
 margin-top: 10px;
 margin-right: 10px;
}

.btn-primary, a.btn-primary {
 background: #facc15;
 color: #0f172a !important;
}

.btn-primary:hover, a.btn-primary:hover {
 background: #eab308;
 color: #000 !important;
}

.btn-secondary, a.btn-secondary {
 background: #e11d48;
 color: #ffffff !important;
}

.btn-secondary:hover, a.btn-secondary:hover {
 background: #be123c;
 color: #ffffff !important;
}

.product-card {
 background: #1e293b;
 border: 1px solid #334155;
 border-radius: 12px;
 padding: 24px;
 margin-bottom: 24px;
}
"""

with open("style.css", "a", encoding="utf-8") as f:
    f.write(css_append)
print("Updated style.css with readable buttons and links")

# 2. Очищаем статьи от коротких ya.cc редиректов
articles_dir = "articles"
if os.path.exists(articles_dir):
    for fname in os.listdir(articles_dir):
        if fname.endswith(".html"):
            fpath = os.path.join(articles_dir, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()

            # Заменяем все ya.cc на поиск в Яндекс Маркете
            content = re.sub(r'href="https?://ya\.cc/[^"]*"', 'href="https://market.yandex.ru/search?text=Электроника"', content)

            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Sanitized links in {fname}")

# 3. Коммит и пуш
subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", "UI: Fix link readability, button styles, and remove broken ya.cc redirects"], check=True)
subprocess.run(["git", "push", "origin", "master"], check=True)
print("SUCCESS_LINKS_AND_STYLES_FIXED")
