import utils
from scraper import SiteScraper
import time
from article import Article


def aggregate():

    start = time.time()
    articles = []  # List of Article Tuples
    article_objects = utils.json_to_articles("dataset.json")
 
    # Get all URL + Headline Tuples
    for Scraper in SiteScraper.__subclasses__():
        articles.extend(Scraper().scrape().get_articles())
    end = time.time()
    print("Scraping took: {} seconds".format(end - start))
    start = time.time()
    # articles = articles[5:15] # Smaller dataset for testing purposes
    # Init all Article Objects
    for url, title in articles:
        article_objects.append(Article(url, title))
    end = time.time()
    print("Initializing objects took: {} seconds".format(end - start))

    start = time.time()
    article_objects = utils.remove_duplicate_articles(article_objects)
    end = time.time()
    print("Removing duplicates took: {} seconds. Got {} articles".format(
        end - start, len(articles)))

    start = time.time()
    counter = 0
    for article in article_objects:
        article.process()
        counter += 1
        print("{}/{}".format(counter, len(article_objects)))
    end = time.time()
    print("Processing articles took: {} seconds".format(end - start))

    start = time.time()
    utils.article_objects_to_json(article_objects)
    end = time.time()
    print("Converting to JSON took: {} seconds".format(end - start))
    # utils.articles_to_vocabulary(articles)
    # utils.articles_to_csv(articles)


if __name__ == "__main__":
    aggregate()
