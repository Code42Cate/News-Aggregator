import utils
from scraper import SiteScraper
import time


def aggregate():
    start = time.time()
    articles = []
    for Scraper in SiteScraper.__subclasses__():
        articles.extend(Scraper().scrape().get_articles())

    for url, title in articles:
        print('"{}","{}"'.format(title.replace("\n", "").replace('"', "'"), url))
    articles = utils.remove_duplicates(articles)
    #articles = utils.filter_by_keywords(articles, ["google", "security", "startup"])
    utils.articles_to_html(articles)
    # utils.articles_to_vocabulary(articles)
    utils.articles_to_csv(articles)
    end = time.time()
    print("Scraping took: {} seconds".format(end - start))


if __name__ == "__main__":
    aggregate()
