from scraper import SiteScraper
import requests
from aiohttp import ClientSession
import asyncio


class YCombinatorScraper(SiteScraper):
    def scrape(self):

        result_list = []
        result = requests.get(
            "https://hacker-news.firebaseio.com/v0/beststories.json").json()
        itemURL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

        loop = asyncio.get_event_loop()
        tasks = []
        for id in result:
            task = asyncio.ensure_future(
                self.__async_scrape(itemURL.format(id), result_list))
            tasks.append(task)
        loop.run_until_complete(asyncio.wait(tasks))

        self.__update_articles(result_list)
        return self

    async def __async_scrape(self, url, result_list):
        async with ClientSession() as session:
            async with session.get(url) as response:
                article_result = await response.json()
                if "url" in article_result:
                    result_list.append(
                        (article_result["url"], article_result["title"]))

    # This should eventually already kill duplicates
    def __update_articles(self, articles):
        self.articles = articles

    def get_articles(self):
        return super().get_articles()
