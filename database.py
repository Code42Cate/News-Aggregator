from pymongo import MongoClient

client = MongoClient()
db = client.news_database
articles_collection = db.articles


def save_articles(articles):
    for article in articles:
        obj = article.to_beautiful_object()
        obj["title"] = obj["title"].encode(
            "utf-8", "ignore").decode("utf-8", "ignore")
        obj["content"] = obj["content"].encode(
            "utf-8", "ignore").decode("utf-8", "ignore")
        for i, keyword in enumerate(obj["keywords"]):
            obj["keywords"][i] = keyword.encode(
                "utf-8", "ignore").decode("utf-8", "ignore")
        article_id = articles_collection.insert_one(obj).inserted_id
        print("Inserted article, ID: {}".format(article_id))
