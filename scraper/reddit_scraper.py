from scraper import SiteScraper
import requests
from bs4 import BeautifulSoup


class RedditScraper(SiteScraper):
    def scrape(self):
        subreddit_list = ["https://www.reddit.com/r/programming", "https://www.reddit.com/r/technology",
                          "https://www.reddit.com/r/compsci", "https://www.reddit.com/r/netsec", "https://www.reddit.com/r/webdev"]
        result = []
        for subreddit in subreddit_list:
            url = subreddit + "/top.json"
            # User-Agent is apparently super important on reddit or you get throttled hard
            r = requests.get(url, headers={'User-agent': 'Chrome'})
            listings = r.json()
            for child in listings['data']['children']:
                # Only want external links
                if "https://www.reddit.com" not in child['data']['url']:
                    result.append(
                        (child['data']['url'], child['data']['title']))
        self.__update_articles(result)
        return self

    # This should eventually already kill duplicates
    def __update_articles(self, articles):
        self.articles = articles

    def get_articles(self):
        return super().get_articles()
