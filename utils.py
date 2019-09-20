# encoding:utf-8
import json
from article import Article


def json_to_articles(filename):
    article_objects = []
    for json_article in json.loads(open(filename, "r").read())["articles"]:
        article_objects.append(Article(json_article["url"], json_article["title"],
                                       content=json_article["content"], keywords=json_article["keywords"]))
    return article_objects


def article_objects_to_json(article_objects):
    article_jsons = []
    for article_object in article_objects:
        article_jsons.append(article_object.to_beautiful_object())
    with open("dataset.json", "w") as f:
        json.dump({"articles": article_jsons}, f)


"""
For arrays of article objects, removing articles with same URL property
"""


def remove_duplicate_articles(articles):
    visited = set()
    without_duplicates = []
    for article in articles:
        if not article.url in visited:
            visited.add(article.url)
            without_duplicates.append(article)
    return without_duplicates


def article_tuples_to_objects(articles):
    article_objects = []
    for url, title in articles:
        article_objects.append(Article(url, title))
    return article_objects
