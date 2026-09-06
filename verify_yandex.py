import subprocess
import os

code = "6pjcg0idg6kg6ho5"

# 1. Добавляем метатег верификации в index.html
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

meta_tag = f'<meta name="yandex-verification" content="{code}" />'

if code not in content:
    if "<head>" in content:
        content = content.replace("<head>", f"<head>\n    {meta_tag}")
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("Meta tag embedded into index.html")

# 2. Создаем HTML файл для верификации (и текстовый на всякий случай)
with open(f"{code}.html", "w", encoding="utf-8") as f:
    f.write(f"<html><head><meta name=\"yandex-verification\" content=\"{code}\"/></head><body>Verification: {code}</body></html>")

with open(f"yandex_{code}.txt", "w", encoding="utf-8") as f:
    f.write(code)

# 3. Деплой
subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", f"Add Yandex verification code {code}"], check=True)
subprocess.run(["git", "push", "origin", "master"], check=True)
print("SUCCESS_VERIFICATION_DEPLOYED")
