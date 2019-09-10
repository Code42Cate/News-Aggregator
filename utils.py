from jinja2 import Template


def articles_to_html(articles_tuple):
    template_string = ""
    with open("newsletter_template.html", "r") as f:
        template_string = f.read()
    articles = []
    for url, title in articles_tuple:
        dict_article = dict(url=url, title=title)
        articles.append(dict_article)
    Template(template_string).stream(articles=articles).dump("newsletter.html")
