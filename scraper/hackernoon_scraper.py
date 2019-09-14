from scraper import SiteScraper
from bs4 import BeautifulSoup
import requests
from aiohttp import ClientSession
import asyncio


class HackerNoonScraper(SiteScraper):
    def scrape(self):
        hackernoon_urls = ["https://hackernoon.com/tagged/cryptocurrency", "https://hackernoon.com/tagged/coding",
                           "https://hackernoon.com/tagged/artificial-intelligence", "https://hackernoon.com/tagged/futurism", "https://hackernoon.com/tagged/startups"]
        result = []
        tasks = []
        loop = asyncio.get_event_loop()
        for hackernoon_topic_url in hackernoon_urls:
            task = asyncio.ensure_future(
                self.__async_scrape(hackernoon_topic_url, result))
            tasks.append(task)
        loop.run_until_complete(asyncio.wait(tasks))
        self.__update_articles(result)
        return self

    async def __async_scrape(self, url, result_list):
        async with ClientSession() as session:
            async with session.get(url) as response:
                text = await response.text(encoding="utf-8")
                soup = BeautifulSoup(text, features="lxml")
                titles = soup.find_all("div", "title")
                articles = []
                for title in titles:
                    result_list.append(("https://hackernoon.com" +
                                        title.findChildren("a", recursive=False)[0]["href"], title.text))

    # This should eventually already kill duplicates
    def __update_articles(self, articles):
        self.articles = articles

    def get_articles(self):
        return super().get_articles()
