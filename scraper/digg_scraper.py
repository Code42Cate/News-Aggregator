from scraper import SiteScraper
import requests
from bs4 import BeautifulSoup


class DiggScraper(SiteScraper):

    def scrape(self):
        try:
            page = requests.get("https://digg.com/channel/technology")
            soup = BeautifulSoup(page.text, features="lxml")
            headlines = [x.text for x in soup.find_all("h2", "headline")]
            links = [self.__build_url__(x.parent["href"])
                     for x in soup.findAll("h2", "headline")]

            self.__update_articles(list(zip(links, headlines)))
        except Exception as e:
            print(str(e))

        return self

    def __build_url__(sef, url):
        if url[0] is "/":
            return "https://digg.com{}".format(url)
        return url

    def __update_articles(self, articles):
        self.articles = articles

    def get_articles(self):
        return super().get_articles()
