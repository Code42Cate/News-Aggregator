# encoding:utf-8
import json
from article import Article

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

# YES. I know. remove_faulty_objects and remove_database_articles do 100% the same lol


def remove_faulty_objects(articles, faulty_articles):
    faulty_urls = set()
    for faulty in faulty_articles:
        faulty_urls.add(faulty.url)
    without_faulty = []
    for article in articles:
        if not article.url in faulty_urls:
            without_faulty.append(article)

    return without_faulty


def remove_database_articles(articles, database_articles):
    database_set = set()
    result = []
    for article in database_articles:
        database_set.add(article.url)
    for article in articles:
        if not article.url in database_set:
            result.append(article)

    return result
