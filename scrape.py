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
    article_objects = utils.article_tuples_to_objects(articles) # Convert to article objects
    print("Scraping took: {} seconds".format(end - start))
    article_objects = article_objects[5:15] # Smaller dataset for testing purposes
    
    start = time.time()
    article_objects = utils.remove_duplicate_articles(article_objects)
    end = time.time()
    print("Removing duplicates took: {} seconds. Got {} articles".format(
        end - start, len(articles)))

    start = time.time()
    counter = 0
    failed_articles = [] # We want to remove and more importantly log them for later
    for article in article_objects:
        if not article.process():   # Process is downloading, parsing and classifying each article. Currently everything synchronous so slow af
            failed_articles.append(article)
        counter += 1
        print("{}/{}".format(counter, len(article_objects)))
    end = time.time()
    print("Processing articles took: {} seconds".format(end - start))

    article_objects = utils.remove_faulty_objects(article_objects, failed_articles)

    start = time.time()
    utils.article_objects_to_json(article_objects)
    end = time.time()
    print("Converting to JSON took: {} seconds".format(end - start))


if __name__ == "__main__":
    aggregate()
