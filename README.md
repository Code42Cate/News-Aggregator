# Google News s****

This project is the solution to my frustration which Google News caused for way too long.

I read a lot of news articles everyday, but I usually don't have the time to scout on multiple news site for articles that interest me. So I've been using different news aggregator sites for a long time, up until now Google News on my phone was the best choice.


The problem with Google News was, that their ********* algorithms are way too ********* sensitive and whenever I read any controversial article I instantly saw how hard they are trying to put me into a bubble.
The results of getting into a bubble where, that I only got the most boring mainstream articles about the same topics, _every freaking day_. I don't know you, but I read to learn about new topics and to think about different perspectives/opinions, not to get confirmation by 100s of articles every day that my opinion is the correct one >:(

### Okay, enough rant. We have a problem? Whats the solution?
### Let's build our own news aggregator!

Sites that are currently supported: (Mostly the tech categories)
- Hackernews
- Hackernoon
- Reddit
- TechCrunch
- TechRepublic
- Wired
- XKCD
- yCombinator
- Slashdot
- Digg
- Readwrite
- thenextweb
- Techradar

Sites that I am planning on adding:

    https://www.theverge.com/
    https://mashable.com/?europe=true
    https://www.engadget.com
    https://arstechnica.com/
    https://www.vox.com/recode
    https://www.makeuseof.com/
    https://techmeme.com/
    https://www.buzzfeednews.com/section/tech
    https://www.inquisitr.com/category/tech/
    https://www.businessinsider.com/sai?IR=T
    https://www.nytimes.com/section/technology
    https://time.com/section/tech
    https://www.bbc.com/news/technology
    https://www.cnet.com/topics/tech-industry/

## You want to add your own scrapers for your favourite site?
All the scrapers are in the `scraper/` directory.

If you want to add another scraper, all you need to do is make a class which inherits from SiteScraper and implement the scrape() method. The scraper will be dynamically used by scrape.py.

If you need inspiration, take a look at the existing scrapers. Some use RSS Feeds (wired_scraper.py), some json (reddot_scraper.py) and the others beautifulsoup.

Before you push, make sure they work with the providing unit tests!:)
