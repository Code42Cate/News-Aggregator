from scraper import (HackerNoonScraper, xkcdScraper, HackerNewsScraper,
                     RedditScraper, TechCrunchScraper, TechRepublicScraper, YCombinatorScraper)
import utils

def aggregate():

    scraper_list = [xkcdScraper(), HackerNoonScraper(), HackerNewsScraper(),
                    RedditScraper(), TechCrunchScraper(), TechRepublicScraper(), YCombinatorScraper()]

    articles = []
    for scraper in scraper_list:
        articles.extend(scraper.scrape().get_articles())

    for url, title in articles:
        print('"{}","{}"'.format(title.replace("\n", "").replace('"', "'"), url))
    articles = utils.remove_duplicates(articles)
    utils.articles_to_html(articles)
    utils.articles_to_vocabulary(articles)
    utils.articles_to_csv(articles)

if __name__ == "__main__":
    aggregate()
