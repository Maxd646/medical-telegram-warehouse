from fastapi import FastAPI
from sqlalchemy import text
from api.database import SessionLocal
from pydantic import BaseModel

app = FastAPI(title="Medical Telegram Analytics API")

class ProductReport(BaseModel):
    term: str
    freq: int

@app.get("/api/reports/top-products", response_model=list[ProductReport])
def top_products(limit: int = 10):
    db = SessionLocal()
    query = text("""
        select word as term, count(*) as freq
        from (
            select regexp_split_to_table(lower(message_text), '\s+') as word
            from fct_messages
        ) t
        where length(word) > 3
        group by word
        order by freq desc
        limit :limit
    """)
    return db.execute(query, {"limit": limit}).mappings().all()
