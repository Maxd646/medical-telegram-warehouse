from pydantic import BaseModel

class ProductReport(BaseModel):
    term: str
    freq: int
