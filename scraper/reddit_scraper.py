from scraper import SiteScraper
import requests
from aiohttp import ClientSession
import asyncio


class RedditScraper(SiteScraper):

    def scrape(self):
        subreddit_list = ["https://www.reddit.com/r/programming", "https://www.reddit.com/r/technology",
                          "https://www.reddit.com/r/compsci", "https://www.reddit.com/r/netsec", "https://www.reddit.com/r/webdev"]
        result = []
        tasks = []
        try:
            loop = asyncio.get_event_loop()
            for subreddit in subreddit_list:
                url = subreddit + "/top.json"
                task = asyncio.ensure_future(self.__async_scrape(url, result))
                tasks.append(task)
            loop.run_until_complete(asyncio.wait(tasks))
        except Exception as e:
            print(str(e))
        self.__update_articles(result)
        return self

    async def __async_scrape(self, url, result):
        async with ClientSession(headers={"User-Agent": "Chrome"}) as session:
            async with session.get(url) as response:
                listings = await response.json()
                for child in listings['data']['children']:
                    # Only want external links
                    if "https://www.reddit.com" not in child['data']['url']:
                        result.append(
                            (child['data']['url'], child['data']['title']))

    def __update_articles(self, articles):
        self.articles = articles

    def get_articles(self):
        return super().get_articles()
