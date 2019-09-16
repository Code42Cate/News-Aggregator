# encoding:utf-8
from jinja2 import Template
import csv


def articles_to_csv(articles_tuple):

    dataset_file = ""
    with open("dataset.csv", "r") as f:
        dataset_file = f.read().split("\n")
    csv_dataset = csv.reader(dataset_file)
    for row in csv_dataset:
        if len(row) == 2:
            articles_tuple.append((row[1], row[0]))

    articles_tuple = remove_duplicates(articles_tuple)

    with open("dataset.csv", "w", encoding="utf8") as f:
        for url, title in articles_tuple:
            f.write('"{}","{}"\n'.format(title.replace(
                "\n", "").replace('"', "'").strip(), url))


def articles_to_html(articles_tuple):
    template_string = ""
    with open("newsletter_template.html", "r") as f:
        template_string = f.read()
    articles = []
    for url, title in articles_tuple:
        dict_article = dict(url=url, title=title)
        articles.append(dict_article)
    Template(template_string).stream(articles=articles).dump("newsletter.html")


def get_stopwords():
    with open("stopwords.txt", "r") as stopwords_file:
        return stopwords_file.read().split("\n")

# This function should do some more clean up. After the first iteration I found words like:
# "if it, letâs


def articles_to_vocabulary(articles_tuple):
    vocabulary = []
    stopwords = get_stopwords()
    with open("vocabulary.txt", "r") as vocabulary_file:
        vocabulary = vocabulary_file.read().split('\n')

    for url, title in articles_tuple:
        words = title.split(" ")
        for word in words:
            word = word.lower()
            if word not in vocabulary and word not in stopwords:
                vocabulary.append(word.replace("\n", ""))
    with open("vocabulary.txt", "w") as vocabulary_file:
        for word in vocabulary:
            vocabulary_file.write("{}\n".format(word))
    print(vocabulary)


def remove_duplicates(articles):
    visited = set()
    without_duplicates = []

    for url, title in articles:
        if not url in visited:
            visited.add(url)
            without_duplicates.append((url, title))
    return without_duplicates


def filter_by_keywords(articles, keywords):
    # I am sure there is a more pythonic way for this
    relevant_articles = []
    for url, title in articles:
        for keyword in keywords:
            if keyword.lower() in title.lower():
                relevant_articles.append((url, title))
                break
    return relevant_articles
