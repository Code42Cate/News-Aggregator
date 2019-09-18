import utils
from scraper import SiteScraper
import time
from article import Article


def aggregate():

    start = time.time()
    articles = []  # List of Article Tuples
    article_objects = []  # List of Article Objects after removing duplicates

    # Get all URL + Headline Tuples
    for Scraper in SiteScraper.__subclasses__():
        articles.extend(Scraper().scrape().get_articles())
    end = time.time()
    print("Scraping took: {} seconds".format(end - start))
    start = time.time()
    articles = utils.remove_duplicates(articles)
    end = time.time()
    print("Removing duplicates took: {} seconds".format(end - start))
    start = time.time()
    # Init all Article Objects
    for url, title in articles:
        article_objects.append(Article(url, title))
    end = time.time()
    print("Initializing objects took: {} seconds".format(end - start))
    start = time.time()
    for article in article_objects:
        article.process()
    end = time.time()
    print("Processing articles took: {} seconds".format(end - start))
    start = time.time()
    utils.articles_to_html(article_objects)
    end = time.time()
    print("Filling template took: {} seconds".format(end - start))
    # utils.articles_to_vocabulary(articles)
    # utils.articles_to_csv(articles)


if __name__ == "__main__":
    aggregate()
