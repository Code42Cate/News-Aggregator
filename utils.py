# encoding:utf-8
from jinja2 import Template
import csv
import time
from rake_nltk import Rake


def articles_to_csv(articles_tuple):

    dataset_file = ""
    with open("dataset.csv", "r") as f:
        dataset_file = f.read().split("\n")
    csv_dataset = csv.reader(dataset_file)
    for row in csv_dataset:
        if len(row) == 3:
            articles_tuple.append((row[1], row[0], row[2]))

    articles_tuple = remove_duplicates(articles_tuple)

    with open("dataset.csv", "w", encoding="utf8") as f:
        for url, title, timestamp in articles_tuple:
            f.write('"{}","{}",{}\n'.format(title.replace(
                "\n", "").replace('"', "'").strip(), url, timestamp))


def articles_to_html(articles_tuple):
    template_string = ""
    with open("newsletter_template.html", "r") as f:
        template_string = f.read()
    articles = []
    for url, title, timestamp in articles_tuple:
        dict_article = dict(url=url, title=title)
        articles.append(dict_article)
    Template(template_string).stream(articles=articles).dump("newsletter.html")


def articles_to_vocabulary(articles_tuple):
    vocabulary = []
    with open("vocabulary.txt", "r") as vocabulary_file:
        vocabulary = vocabulary_file.read().split('\n')
    r = Rake()
    for url, title, timestamp in articles_tuple:
        r.extract_keywords_from_text(title)
        words = r.get_ranked_phrases()
        for word in words:
            word = word.lower()
            if word not in vocabulary:
                vocabulary.append(word)
    with open("vocabulary.txt", "w") as vocabulary_file:
        for word in vocabulary:
            vocabulary_file.write("{}\n".format(word))


def add_timestamps(articles):
    timestamp = time.time()
    new_articles = []
    for url, title in articles:
        new_articles.append((url, title, timestamp))
    return new_articles


def remove_duplicates(articles):
    visited = set()
    without_duplicates = []

    for url, title, timestamp in articles:
        if not url in visited:
            visited.add(url)
            without_duplicates.append((url, title, timestamp))
    return without_duplicates


def filter_by_keywords(articles, keywords):
    # I am sure there is a more pythonic way for this
    relevant_articles = []
    r = Rake()
    for url, title, timestamp in articles:
        r.extract_keywords_from_text(title)
        title_keywords = r.get_ranked_phrases()
        for keyword in keywords:
            if keyword.casefold() in map(str.casefold, title_keywords):
                relevant_articles.append((url, title))
                break
    return relevant_articles


def extract_keywords(headline):
    r = Rake()
    r.extract_keywords_from_text(headline)
    print(r.get_ranked_phrases())
