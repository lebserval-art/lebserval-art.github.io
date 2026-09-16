// Serverless relay: techno-gid.ru feedback form -> Telegram topic "Заявки TechnoGid".
//
// Mirrors the aleks-auto booking.js approach: the Telegram bot token is read
// from the TELEGRAM_BOT_TOKEN environment variable on the server and is never
// exposed to the browser. Deploy this file as a Vercel Serverless Function
// (route: /api/feedback). For Cloudflare Workers / Pages Functions the body of
// `handler` can be reused almost verbatim.
//
// Required env var:  TELEGRAM_BOT_TOKEN
// Optional env vars: TECHNOGID_CHAT_ID (default -1004311094405)
//                    TECHNOGID_TOPIC_ID (default 917)
//                    FEEDBACK_ALLOW_ORIGIN (default https://techno-gid.ru)

const CHAT_ID = process.env.TECHNOGID_CHAT_ID || "-1004311094405";
const TOPIC_ID = process.env.TECHNOGID_TOPIC_ID || "917";
const ALLOW_ORIGIN = process.env.FEEDBACK_ALLOW_ORIGIN || "https://techno-gid.ru";

export default async function handler(req, res) {
  res.setHeader("Access-Control-Allow-Origin", ALLOW_ORIGIN);
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");
  res.setHeader("Vary", "Origin");

  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed" });

  try {
    const raw = typeof req.body === "string" ? JSON.parse(req.body || "{}") : (req.body || {});

    const name = String(raw.name || "").trim().slice(0, 120);
    const contact = String(raw.contact || "").trim().slice(0, 160);
    const topic = String(raw.topic || "Другое").trim().slice(0, 80);
    const message = String(raw.message || "").trim().slice(0, 4000);
    const honeypot = String(raw.website || "").trim();

    // Spam bot filled the hidden field — pretend everything is fine, send nothing.
    if (honeypot) return res.status(200).json({ success: true });

    if (!name || !contact || !message) {
      return res.status(400).json({ error: "Заполните имя, контакт и сообщение" });
    }

    const token = process.env.TELEGRAM_BOT_TOKEN;
    if (!token) {
      console.warn("TELEGRAM_BOT_TOKEN is not configured");
      return res.status(500).json({ error: "Форма не настроена на сервере" });
    }

    // Plain text (no parse_mode) — user-supplied content cannot break formatting.
    const text =
      `📬 Новая заявка с TechnoGid\n\n` +
      `👤 Имя: ${name}\n` +
      `💬 Контакт: ${contact}\n` +
      `📌 Тема: ${topic}\n` +
      `📝 Сообщение: ${message}`;

    const tgResponse = await fetch(`https://api.telegram.org/bot${token}/sendMessage`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        chat_id: CHAT_ID,
        message_thread_id: parseInt(TOPIC_ID, 10),
        text,
        disable_web_page_preview: true
      })
    });

    const result = await tgResponse.json();
    if (!result.ok) {
      console.error("Telegram API error:", result);
      return res.status(502).json({ error: "Не удалось доставить сообщение" });
    }

    return res.status(200).json({ success: true });
  } catch (err) {
    console.error("Feedback error:", err);
    return res.status(500).json({ error: "Internal Server Error" });
  }
}
