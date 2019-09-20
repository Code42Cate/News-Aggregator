# encoding:utf-8
from jinja2 import Template
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


def articles_to_html(articles):
    template_string = ""
    with open("newsletter_template.html", "r") as f:
        template_string = f.read()
    dict_articles = []
    for article in articles:
        if len(article.keywords) != 0:
            dict_article = dict(url=article.url, title=article.title,
                                keywords=" ".join(article.get_keywords()))
            dict_articles.append(dict_article)
    Template(template_string).stream(
        articles=dict_articles).dump("newsletter.html")


def remove_duplicates(articles):
    visited = set()
    without_duplicates = []

    for url, title in articles:
        if not url in visited:
            visited.add(url)
            without_duplicates.append((url, title))
    return without_duplicates
