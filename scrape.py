import utils
from scraper import SiteScraper


def aggregate():

    articles = []
    for Scraper in SiteScraper.__subclasses__():
        articles.extend(Scraper().scrape().get_articles())

    for url, title in articles:
        print('"{}","{}"'.format(title.replace("\n", "").replace('"', "'"), url))
    articles = utils.remove_duplicates(articles)
    utils.articles_to_html(articles)
    utils.articles_to_vocabulary(articles)
    utils.articles_to_csv(articles)


if __name__ == "__main__":
    aggregate()
