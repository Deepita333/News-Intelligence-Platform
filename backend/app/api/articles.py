from fastapi import APIRouter, HTTPException
from app.schemas.article import Article

router = APIRouter()

articles = [
    {
        "title": "AI is changing the world",
        "source": "Example News",
        "category": "technology"
    },
    {
        "title": "New AI model released",
        "source": "Tech News",
        "category": "technology"
    },
    {
        "title": "India announces new economic policy",
        "source": "Daily News",
        "category": "business"
    }
]


@router.get("/", response_model=list[Article])
def get_articles(
    limit: int = 10,
    category: str | None = None
):
    filtered_articles = articles

    if category:
        filtered_articles = [
            article
            for article in articles
            if article["category"].lower() == category.lower()
        ]

    return filtered_articles[:limit]


@router.get("/{article_id}", response_model=Article)
def get_article(article_id: int):
    if article_id < 1 or article_id > len(articles):
        raise HTTPException(
            status_code=404,
            detail="Article not found"
        )

    return articles[article_id - 1]