# api/feedback.js — обработчик формы обратной связи

Форма на `contacts.html` отправляет `POST /api/feedback` с JSON
`{ name, contact, topic, message }`. Обработчик пересылает заявку в Telegram
в супергруппу `-1004311094405`, топик `917` («Заявки TechnoGid»).

**GitHub Pages не исполняет серверный код** — этот файл нужно задеплоить туда,
где есть serverless-функции. Токен бота (`TELEGRAM_BOT_TOKEN`) задаётся только
как секрет платформы и никогда не попадает в браузер.

## Вариант A — Vercel (рекомендуется)

1. Импортировать репозиторий `lebserval-art/lebserval-art.github.io` в Vercel
   как проект (Framework preset: **Other**, Output dir: корень).
2. В Project → Settings → Environment Variables добавить:
   - `TELEGRAM_BOT_TOKEN` — токен бота `@lebserval_ai_bot` (тот же, что у aleks-auto);
   - (опц.) `TECHNOGID_CHAT_ID`, `TECHNOGID_TOPIC_ID`, `FEEDBACK_ALLOW_ORIGIN`.
3. Привязать домен `techno-gid.ru` к проекту Vercel. Тогда `contacts.html` и
   `/api/feedback` работают на одном origin — правки в клиентском коде не нужны
   (`FEEDBACK_ENDPOINT = '/api/feedback'`).

Статические страницы Vercel отдаёт как есть, поэтому GitHub Pages можно
оставить или отключить — на выбор.

## Вариант B — держать хостинг на GitHub Pages, функцию — отдельно

Задеплоить только функцию (Vercel/Cloudflare Worker) на отдельный домен,
например `https://feedback-technogid.vercel.app/api/feedback`, задать там
`TELEGRAM_BOT_TOKEN`, а в `contacts.html` заменить
`var FEEDBACK_ENDPOINT = '/api/feedback';` на этот абсолютный URL.
CORS уже настроен через `FEEDBACK_ALLOW_ORIGIN`.

## Пока функция не задеплоена

Форма отправляет запрос, ловит ошибку сети и показывает
«❌ Ошибка отправки… напишите нам напрямую в Telegram» со ссылкой на
`@lebserval_ai_bot` — то есть остаётся рабочий запасной канал.

## Тест

```
curl -X POST https://techno-gid.ru/api/feedback \
  -H 'Content-Type: application/json' \
  -d '{"name":"Тест","contact":"@tester","topic":"Другое","message":"проверка"}'
# -> {"success":true}  и карточка в топике «Заявки TechnoGid»
```
