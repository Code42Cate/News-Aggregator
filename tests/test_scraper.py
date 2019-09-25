import unittest
from scraper import SiteScraper
import socket
import re


class TestAllScraperNoInternet(unittest.TestCase):
    old_socket = None

    def setUp(self):
        # Kill connection
        def guard(*args, **kwargs):
            raise Exception(
                "The internet is a scary place, please don't go there")

        TestAllScraperNoInternet.old_socket = socket.socket
        socket.socket = guard

    def tearDown(self):
        # reset the socket so we can establish connections again
        socket.socket = TestAllScraperNoInternet.old_socket
        pass
    """
    Since we killed all possible connections, we are expecting no articles from scraping.
    There is still a problem because some sockets arent getting closed properly, not sure how to fix that right now
    I should also introduce a better error handling system for all the scrapers in general
    """
    @unittest.skip("Skipping because it is taking too long.")
    def testAllScraperNoConnection(self):
        articles = []
        for Scraper in SiteScraper.__subclasses__():
            articles.extend(Scraper().scrape().get_articles())
        self.assertEqual([], articles)


class TestAllScraperOutput(unittest.TestCase):
    @unittest.skip("Skipping because it is taking too long.")
    def testTupleOutput(self):
        # Basially our header, should always be the same format. Currently: ("url", "title")
        tuple_size = len(SiteScraper().scrape().get_articles()[0])
        for Scraper in SiteScraper.__subclasses__():
            articles = Scraper().scrape().get_articles()
            for article in articles:
                self.assertEqual(tuple_size, len(article))

    @unittest.skip("Skipping because it is taking too long.")
    def testURLOutput(self):
        for Scraper in SiteScraper.__subclasses__():
            articles = Scraper().scrape().get_articles()
            for url, title in articles:
                self.assertTrue(self.is_valid_url(url))

    """Weird somewhat okay-ish URL Validator. Mostly taken from django, so credit goes to them: https://github.com/django/django/blob/master/django/core/validators.py#L74"""

    def is_valid_url(self, url):
        regex = re.compile(
            r'^https?://'  # http:// or https://
            # domain...
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{1,63}\.?|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return url is not None and regex.search(url)


if __name__ == "__main__":
    unittest.main()
