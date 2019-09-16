from scraper import SiteScraper
import requests
from aiohttp import ClientSession
import asyncio
import xml.etree.ElementTree as ET


class WiredScraper(SiteScraper):
    def scrape(self):

        rss_feeds = ["https://www.wired.com/feed/category/security/latest/rss",
                     "https://www.wired.com/feed/category/science/latest/rss", "https://www.wired.com/feed/category/business/latest/rss", "https://www.wired.com/feed/rss", "https://www.wired.com/feed/category/ideas/latest/rss", "https://www.wired.com/feed/category/backchannel/latest/rss"]
        result_list = []
        try:
            loop = asyncio.get_event_loop()
            tasks = []
            for rss in rss_feeds:
                task = asyncio.ensure_future(
                    self.__async_scrape(rss, result_list))
                tasks.append(task)
            loop.run_until_complete(asyncio.wait(tasks))
        except Exception as e:
            print(str(e))
        self.__update_articles(result_list)
        return self

    async def __async_scrape(self, url, result_list):
        async with ClientSession() as session:
            async with session.get(url) as response:
                article_result = await response.text()
                root = ET.fromstring(article_result)
                for item in root.find("channel").findall("item"):
                    result_list.append(
                        (item.find("link").text, item.find("title").text))

    def __update_articles(self, articles):
        self.articles = articles

    def get_articles(self):
        return super().get_articles()
