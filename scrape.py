from scraper import (HackerNoonScraper, xkcdScraper, HackerNewsScraper,
                     RedditScraper, TechCrunchScraper, TechRepublicScraper, YCombinatorScraper)
from utils import articles_to_html

def aggregate():

    scraper_list = [xkcdScraper(), HackerNoonScraper(), HackerNewsScraper(),
                    RedditScraper(), TechCrunchScraper(), TechRepublicScraper(), YCombinatorScraper()]

    articles = []
    for scraper in scraper_list:
        articles.extend(scraper.scrape().get_articles())

    articles_to_html(articles)

if __name__ == "__main__":
    aggregate()