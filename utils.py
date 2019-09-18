# encoding:utf-8
from jinja2 import Template


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
