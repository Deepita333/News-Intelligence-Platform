from pydantic import BaseModel


class ArticleCreate(BaseModel):
    title: str
    source: str
    category: str