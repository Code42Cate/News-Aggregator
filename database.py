from bson.objectid import ObjectId
from pymongo import MongoClient
from article import Article
client = MongoClient()
db = client.news_database
articles_collection = db.articles
keywords_collection = db.keywords


def save_articles(articles):
    insert_articles = []
    for article in articles:
        obj = article.to_beautiful_object()
        obj["title"] = obj["title"].encode(
            "utf-8", "ignore").decode("utf-8", "ignore")
        obj["content"] = obj["content"].encode(
            "utf-8", "ignore").decode("utf-8", "ignore")
        for i, keyword in enumerate(obj["keywords"]):
            obj["keywords"][i] = keyword.encode(
                "utf-8", "ignore").decode("utf-8", "ignore")
        insert_articles.append(obj)

    articles_collection.insert_many(insert_articles)
    print("Inserted {} articles".format(len(articles)))


def update_keyword(keyword, category):
    keywords_collection.update_one(
        {"keyword": keyword}, {"$addToSet": {"categories": category}}, upsert=True)


def remove_keyword(id, keyword):
    articles_collection.update_one(
        {"_id": ObjectId(id)}, {"$pull": {"keywords": keyword}})


def get_categories(keyword):
    result = keywords_collection.find_one({"keyword": keyword})
    if result is not None:
        return result["categories"]
    return []


def get_articles():
    article_objects = []
    all_articles = list(articles_collection.find({}))
    for article in all_articles:
        article_objects.append(Article(
            article["url"], article["title"], content=article["content"], keywords=article["keywords"]))
    return article_objects


def get_articles_json():
    return list(articles_collection.find({}))

