# News Aggregator

This project is the solution to my frustration which most news sites/aggregators I used caused for way too long.

I read a lot of news articles everyday, but I usually don't have the time to scout on multiple news site for articles that interest me.

The problem with many news sites is, that their algorithms are way too freaking sensitive and like to put mit into annoying bubbles.

Don't know about you, but I don't like bubbles:(


### Okay, enough rant. We have a problem? Whats the solution?
### Let's build our own news aggregator!
| Supported Sites | Planned Additional Sites |
|-----------------|--------------------------|
| Hackernews      | The Verge                |
| Hackernoon      | Mashable                 |
| Reddit          | Engadget                 |
| TechCrunch      | ArsTechnica              |
| TechRepublic    | Vox                      |
| Wired           | MakeUseOf                |
| XKCD            | TechMeme                 |
| yCombinator     | Buzzfeednews             |
| Slashdot        | Inquisitr                |
| Digg            | businessInsider          |
| ReadWrite       | nytimes                  |
| thenextweb      | time                     |
| Techradar       | bbc                      |
| cnet            |                          |

## How does it work?

Yeyee coming tonight:D

## Tech Stack

- Backend Language: Python 3.7
    - [Flask](https://github.com/pallets/flask) && [Connexion](https://github.com/zalando/connexion) as Webserver / API
    - [Newspaper](https://github.com/codelucas/newspaper) for the text scraping
- Database: [mongoDB](https://www.mongodb.com/)
- Frontend: JavaScript and [Bootstrap 4.0](https://getbootstrap.com/), also using the [google material colour palette](https://github.com/8lueberry/google-material-color/)

- Testing: [pyunit](https://wiki.python.org/moin/PyUnit) for python backend testing and [puppeteer](https://github.com/GoogleChrome/puppeteer) with [node.js](https://nodejs.org/en/) for frontend testing

## Screenshots
Since I am only running it locally in my dev environment and you might want to see how the frontend looks:

![alt text][main]

If you click on 'Add Label' this shows up:

![alt text][modal]

[main]: docs/main.png "Landing Page with article table"
[modal]: docs/modal.png "'Add label' popup modal"


## Requirements for local environment

- Installation of [mongoDB](https://www.mongodb.com/)
- Python 3.7+
- Node.js (I am using v10, not sure how far back you can go. ES6 is required!)
- And more stuff, an installation script is coming some time in the future

## You want to add your own scrapers for your favourite site?
All the scrapers are in the `scraper/` directory.

If you want to add another scraper, all you need to do is make a class which inherits from SiteScraper and implement the scrape() method. The scraper will be dynamically used by scrape.py.

If you need inspiration, take a look at the existing scrapers. Some use RSS Feeds [wired_scraper.py](scraper/wired_scraper.py), some json [reddit_scraper.py](scraper/reddit_scraper.py) and the others beautifulsoup.
AND please, if you do more than 1 request, make it asynchronously
Before you push, make sure they work with the provided unit tests!:)

## Testing

Feel free to add more tests:D

This project is using pyunit for unit tests. Go into the root directory of this project and run: 

`python3 -m unittest discover`

I am also using node.js and puppeteer for some frontend testing. Run them with `npm run` in the testing folder. (You need to run `python3 api.py` before and might want to update your database with `python3 scrape.py` first!)

## TODO:

### Backend:
- Figure out how we can prevent timeouts (and handle other errors) from all the sites
    (Might wanna use proxies?)
- Figure out how the fuck asyncio works so I can make the main scraping loop in async:D
- Figure out how to close failing connections
- Figure out how to handle exceptions in the scrapers, it would be good if people who implement scrapers do not need to do worry about that
- Make it production ready!
- Write more tests
### Frontend:
- Write more tests
- Add filtering options for frontend
- Work on site performance
- Make it possible to scroll while dragging
- Send the delete requests in batches

## Authors
* **Jonas Scholz** - [Code42Cate](https://github.com/Code42Cate)