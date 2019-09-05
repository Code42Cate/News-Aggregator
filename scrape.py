import requests
import json
from bs4 import BeautifulSoup
import asyncio
from aiohttp import ClientSession


# Only used by getHackerNewsArticles
async def asyncHackerNewsRequest(url, result_list):
    async with ClientSession() as session:
        async with session.get(url) as response:
            article_result = await response.json()
            if "url" in article_result:
                result_list.append(
                    (article_result["url"], article_result["title"]))


def getHackerNewsArticles():
    print("Getting URLs from Hackernews")
    result_list = []
    result = requests.get(
        "https://hacker-news.firebaseio.com/v0/beststories.json").json()
    itemURL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

    loop = asyncio.get_event_loop()
    tasks = []
    for id in result:
        task = asyncio.ensure_future(
            asyncHackerNewsRequest(itemURL.format(id), result_list))
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    print(result_list)


# We should check how big our subreddit_list is and then maybe do it async too..
def getSubredditNewsArticles(subreddit_list):
    result = []
    for subreddit in subreddit_list:
        url = subreddit + "/top.json"
        # User-Agent is apparently super important on reddit or you get throttled hard
        r = requests.get(url, headers={'User-agent': 'Chrome'})
        listings = r.json()
        for child in listings['data']['children']:
            # Only want external links
            if "https://www.reddit.com" not in child['data']['url']:
                result.append((child['data']['url'], child['data']['title']))
    return result


def getxkcdURL():
    r = requests.get("https://xkcd.com")
    soup = BeautifulSoup(r.text, features="lxml")
    return soup.find("meta",  property="og:url")

# https://thehackernews.com/
# https://hackernoon.com/
# https://bbc.com


article_list = getHackerNewsArticles()

subreddit_list = ["https://www.reddit.com/r/programming", "https://www.reddit.com/r/technology",
                  "https://www.reddit.com/r/compsci", "https://www.reddit.com/r/netsec", "https://www.reddit.com/r/webdev"]

print(getSubredditNewsArticles(subreddit_list))