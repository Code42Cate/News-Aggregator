from scraper import SiteScraper
import requests
import xml.etree.ElementTree as ET


class TheNextWebScraper(SiteScraper):

    def scrape(self):
        result_list = []
        try:
            page = requests.get("https://thenextweb.com/feed/")
            root = ET.fromstring(page.text)
            for item in root.find("channel").findall("item"):
                result_list.append(
                    (item.find("link").text, item.find("title").text))
        except Exception as e:
            print(str(e))
        self.__update_articles(result_list)
        return self

    # This should eventually already kill duplicates
    def __update_articles(self, articles):
        self.articles = articles

    def get_articles(self):
        return super().get_articles()
