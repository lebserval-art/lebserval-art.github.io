import os
import re
import subprocess
from datetime import date

base_url = "https://lebserval-art.github.io"
today = date.today().isoformat()

# 1. Шаблоны служебных страниц
base_head = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>%s — ТехноГид</title>
    <link rel="stylesheet" href="style.css">
    <!-- Yandex.Metrika counter -->
    <script type="text/javascript">
    (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
    m[i].l=1*new Date();
    for (var j = 0; j < document.scripts.length; j++) {if (document.scripts[j].src === r) { return; }}
    k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
    (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");
    ym(112303137, "init", { clickmap:true, trackLinks:true, accurateTrackBounce:true, webvisor:true });
    </script>
    <noscript><div><img src="https://mc.yandex.ru/watch/112303137" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
</head>
<body>
<header class="site-header">
    <div class="container header-container">
        <a href="index.html" class="logo">Техно<span>Гид</span></a>
        <nav class="main-nav">
            <a href="index.html">Главная</a>
            <a href="about.html">О проекте</a>
            <a href="contacts.html">Контакты</a>
        </nav>
    </div>
</header>
<main class="container content-page">
"""

footer_html = """
</main>
<footer class="site-footer">
    <div class="container footer-content">
        <div class="footer-col">
            <h4>ТехноГид</h4>
            <p>Честные обзоры гаджетов, потребительской электроники и автотоваров. Экспертные подборки с реальным опытом использования.</p>
        </div>
        <div class="footer-col">
            <h4>Навигация</h4>
            <ul>
                <li><a href="index.html">Все обзоры</a></li>
                <li><a href="about.html">О проекте</a></li>
                <li><a href="contacts.html">Контакты</a></li>
                <li><a href="privacy.html">Политика конфиденциальности</a></li>
            </ul>
        </div>
        <div class="footer-col">
            <h4>Информация</h4>
            <p class="disclaimer">Сайт может содержать партнерские ссылки. При переходе по ссылкам мы можем получать комиссионное вознаграждение без дополнительных расходов для покупателя.</p>
            <p class="copy">© 2026 ТехноГид. Все права защищены.</p>
        </div>
    </div>
</footer>
</body>
</html>
"""

about_content = """
    <article class="static-article">
        <h1>О проекте «ТехноГид»</h1>
        <p>Добро пожаловать на <strong>ТехноГид</strong> — независимое издание, посвященное потребительской технике, автомобильным девайсам и умным устройствам для дома.</p>
        <h2>Наша миссия</h2>
        <p>Мы анализируем рынок потребительской электроники, отделяя реальные преимущества от маркетинговых обещаний. Каждый наш рейтинг и руководство составляются на основе реальных характеристик, тестов надежности и отзывов пользователей.</p>
        <h2>Независимость и прозрачность</h2>
        <p>Редакция не размещает платные заказные места в подборках. Проект развивается благодаря партнерским интеграциям с крупными торговыми площадками (Яндекс Маркет, AliExpress).</p>
    </article>
"""

contacts_content = """
    <article class="static-article">
        <h1>Контакты редакции</h1>
        <p>Мы открыты к вопросам, предложениям и замечаниям по материалам проекта.</p>
        <div class="contact-box" style="margin-top:20px;line-height:1.8;">
            <p><strong>Электронная почта редакции:</strong> info@technogid-media.ru</p>
            <p><strong>По вопросам партнерства:</strong> partner@technogid-media.ru</p>
            <p><strong>График работы:</strong> Пн–Пт с 09:00 до 18:00 (МСК)</p>
        </div>
    </article>
"""

privacy_content = """
    <article class="static-article">
        <h1>Политика конфиденциальности</h1>
        <p>Настоящая Политика регламентирует обработку обезличенных данных посетителей сайта «ТехноГид».</p>
        <h2>1. Аналитические данные</h2>
        <p>Мы используем счетчик Яндекс Метрики для анализа трафика, оптимизации скорости загрузки страниц и улучшения навигации. Счетчик собирает обезличенные технические параметры (файлы cookie, IP-адрес, тип браузера).</p>
        <h2>2. Партнерские ссылки</h2>
        <p>При переходе по ссылкам на маркетплейсы действуют политики конфиденциальности соответствующих торговых площадок.</p>
        <h2>3. Безопасность</h2>
        <p>Сайт не собирает и не хранит персональные данные пользователей (пароли, платежные реквизиты, телефоны).</p>
    </article>
"""

pages = [
    ("about.html", "О проекте", about_content),
    ("contacts.html", "Контакты", contacts_content),
    ("privacy.html", "Политика конфиденциальности", privacy_content),
]

for filename, title, body in pages:
    with open(filename, "w", encoding="utf-8") as f:
        f.write((base_head % title) + body + footer_html)
    print(f"Created {filename}")

# 2. Замена заглушек ya.cc/m/placeholder... в статьях на рабочие ссылки поиска
articles_dir = "articles"
if os.path.exists(articles_dir):
    for fname in os.listdir(articles_dir):
        if fname.endswith(".html"):
            fpath = os.path.join(articles_dir, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()

            content = re.sub(
                r'href="https://ya\.cc/m/placeholder-[^"]*"',
                'href="https://market.yandex.ru/catalog--elektronika/54440"',
                content
            )
            content = re.sub(
                r'href="https://ya\.cc/m/placeholder-ali-[^"]*"',
                'href="https://aliexpress.ru"',
                content
            )

            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Replaced placeholders in {fname}")

# 3. Деплой
subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", "Fix 404: create about, contacts, privacy pages and remove dead links"], check=True)
subprocess.run(["git", "push", "origin", "master"], check=True)
print("SUCCESS_PAGES_AND_LINKS_FIXED")
