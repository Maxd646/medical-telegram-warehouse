import os
import json
import psycopg2
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

def load_raw():
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )
    cur = conn.cursor()

    cur.execute("CREATE SCHEMA IF NOT EXISTS raw;")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS raw.telegram_messages (
            message_id BIGINT,
            channel_name TEXT,
            message_date TIMESTAMP,
            message_text TEXT,
            views INT,
            forwards INT,
            has_media BOOLEAN,
            image_path TEXT
        );
    """)

    base_path = Path("data/raw/telegram_messages")

    for json_file in base_path.rglob("*.json"):
        with open(json_file, "r", encoding="utf-8") as f:
            for row in json.load(f):
                cur.execute("""
                    INSERT INTO raw.telegram_messages VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                """, (
                    row["message_id"],
                    row["channel_name"],
                    row["message_date"],
                    row["message_text"],
                    row["views"],
                    row["forwards"],
                    row["has_media"],
                    row["image_path"]
                ))

    conn.commit()
    cur.close()
    conn.close()
    print("Raw data loaded.")

if __name__ == "__main__":
    load_raw()
