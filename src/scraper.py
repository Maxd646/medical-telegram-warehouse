import os
import json
from datetime import datetime
from pathlib import Path
from telethon import TelegramClient
from dotenv import load_dotenv
from src.logger import get_logger
from src.utils import ensure_dir

load_dotenv()
logger = get_logger()

API_ID = os.getenv("TELEGRAM_API_ID")
API_HASH = os.getenv("TELEGRAM_API_HASH")

CHANNELS = [
    "lobelia4cosmetics",
    "tikvahpharma",
    "Chemed_Telegram_Channel"
]

BASE_RAW = Path("data/raw")

async def scrape():
    async with TelegramClient("session", API_ID, API_HASH) as client:
        for channel in CHANNELS:
            logger.info(f"Scraping {channel}")

            date_str = datetime.utcnow().strftime("%Y-%m-%d")
            msg_dir = BASE_RAW / "telegram_messages" / date_str
            img_dir = BASE_RAW / "images" / channel

            ensure_dir(msg_dir)
            ensure_dir(img_dir)

            records = []

            async for msg in client.iter_messages(channel, limit=500):
                image_path = None

                if msg.photo:
                    image_path = img_dir / f"{msg.id}.jpg"
                    await client.download_media(msg.photo, file=image_path)

                records.append({
                    "message_id": msg.id,
                    "channel_name": channel,
                    "message_date": msg.date.isoformat() if msg.date else None,
                    "message_text": msg.text,
                    "views": msg.views or 0,
                    "forwards": msg.forwards or 0,
                    "has_media": bool(msg.media),
                    "image_path": str(image_path) if image_path else None
                })

            with open(msg_dir / f"{channel}.json", "w", encoding="utf-8") as f:
                json.dump(records, f, indent=2)

            logger.success(f"{channel}: {len(records)} messages saved")

if __name__ == "__main__":
    import asyncio
    asyncio.run(scrape())
