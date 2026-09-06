import os
import subprocess

domain = "techno-gid.ru"
base_url = f"https://{domain}"

# 1. Записываем файл CNAME для GitHub Pages
with open("CNAME", "w", encoding="utf-8") as f:
    f.write(domain)
print("Created CNAME file with techno-gid.ru")

# 2. Обновляем sitemap.xml
if os.path.exists("sitemap.xml"):
    with open("sitemap.xml", "r", encoding="utf-8") as f:
        smap = f.read()
    smap = smap.replace("https://lebserval-art.github.io", base_url)
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(smap)
    print("Updated sitemap.xml to techno-gid.ru")

# 3. Деплой изменений
subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", f"Bind custom domain {domain} and update sitemap"], check=True)
subprocess.run(["git", "push", "origin", "master"], check=True)
print("SUCCESS_DOMAIN_BOUND")
