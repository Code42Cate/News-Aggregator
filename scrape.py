import utils
from scraper import SiteScraper
import time
from article import Article
import database


def aggregate():

    articles = []  # List of Article Tuples
    article_objects = []
    start = time.time()
    database_articles = database.get_articles()
    end = time.time()
    print("Getting articles from database took: {} seconds".format(end - start))
    start = time.time()
    # Get all URL + Headline Tuples
    for Scraper in SiteScraper.__subclasses__():
        articles.extend(Scraper().scrape().get_articles())
    end = time.time()
    article_objects.extend(utils.article_tuples_to_objects(
        articles))  # Convert to article objects
    print("Scraping took: {} seconds".format(end - start))
    # article_objects = article_objects[0:10] # Smaller dataset for testing purposes
    start = time.time()
    article_objects = utils.remove_duplicate_articles(article_objects)
    article_objects = utils.remove_database_articles(
        article_objects, database_articles)
    end = time.time()
    print("Removing duplicates and known articles took: {} seconds. Got {} articles".format(
        end - start, len(article_objects)))

    start = time.time()
    counter = 0
    failed_articles = []  # We want to remove and more importantly log them for later
    for article in article_objects:
        if not article.process():   # Process is downloading, parsing and classifying each article. Currently everything synchronous so slow af
            failed_articles.append(article)
        counter += 1
        print("{}/{}".format(counter, len(article_objects)))
    end = time.time()
    print("Processing articles took: {} seconds".format(end - start))

    article_objects = utils.remove_faulty_objects(
        article_objects, failed_articles)

    start = time.time()
    if len(article_objects) > 0:
        database.save_articles(article_objects)
    end = time.time()
    print("Saving to database took: {} seconds".format(end - start))


if __name__ == "__main__":
    aggregate()
