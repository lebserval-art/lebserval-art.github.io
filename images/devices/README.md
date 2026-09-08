# images/devices/

Изображения смартфонов для виджетов покупки в статье
`articles/flagships-2026-old-vs-new.html` (класс `.device-thumb`, слот 150px,
`object-fit: contain`).

## Как это работает

Каждый `<img>` в статье ссылается на `../images/devices/<slug>.webp`.
Пока такого файла нет, срабатывает `onerror` и подгружается
`<slug>.svg` — схематичный векторный рендер устройства (сгенерирован
скриптом, оригинальная графика, ~1–1.4 КБ, работает в светлой и тёмной
теме). `_placeholder.svg` — универсальная заглушка для новых устройств
без своего `.svg`.

## Как заменить на фото

Положите `<slug>.webp` (рекомендуется 400×400, белый/прозрачный фон,
устройство по центру, вес до 40 КБ) — он автоматически перекроет SVG.
Правок в HTML не требуется.

**Важно об источнике фото.** Промо-рендеры GSMArena, изображения из
Яндекс Маркета и пресс-кита производителей — объекты авторского права
и не лицензированы для размещения на сайте. Легальный источник для
партнёрского сайта — товарные фиды партнёрских программ AliExpress и
Яндекс Маркета (изображения в них разрешены к использованию партнёром),
либо материалы с явной свободной лицензией (Wikimedia Commons CC-BY /
CC-BY-SA — с указанием авторства).

## Слаги (имя модели → файл)

| Модель | Файл |
|---|---|
| Xiaomi 17 | `xiaomi-17` |
| Xiaomi 15 | `xiaomi-15` |
| OnePlus 15T | `oneplus-15t` |
| OnePlus 13T | `oneplus-13t` |
| Apple iPhone 17 | `apple-iphone-17` |
| Apple iPhone 16 Pro | `apple-iphone-16-pro` |
| Vivo X300 Pro mini | `vivo-x300-pro-mini` |
| Vivo X200 Pro mini | `vivo-x200-pro-mini` |
| Samsung Galaxy S26 | `samsung-galaxy-s26` |
| Samsung Galaxy S25 | `samsung-galaxy-s25` |
| Samsung Galaxy S26 Ultra | `samsung-galaxy-s26-ultra` |
| Samsung Galaxy S25 Ultra | `samsung-galaxy-s25-ultra` |
| OnePlus 15R | `oneplus-15r` |
| OnePlus 13R | `oneplus-13r` |
| POCO F8 Pro | `poco-f8-pro` |
| POCO F7 Pro | `poco-f7-pro` |
| Realme GT 8 Pro | `realme-gt-8-pro` |
| Realme GT 7 Pro | `realme-gt-7-pro` |
| OnePlus 15 | `oneplus-15` |
| OnePlus 13 | `oneplus-13` |
| Honor Magic 8 Pro | `honor-magic-8-pro` |
| Honor Magic 7 Pro | `honor-magic-7-pro` |
| Oppo Find X9 Pro | `oppo-find-x9-pro` |
| Oppo Find X8 Pro | `oppo-find-x8-pro` |
| Google Pixel 10 | `google-pixel-10` |
| Google Pixel 9 | `google-pixel-9` |
| Motorola Edge 60 Ultra | `motorola-edge-60-ultra` |
| Motorola Edge 50 Ultra | `motorola-edge-50-ultra` |

Правило слага: имя модели в нижнем регистре, пробелы → `-`.
