import unittest
from scraper import SiteScraper
import socket


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

    def testAllScraperNoConnection(self):
        articles = []
        for Scraper in SiteScraper.__subclasses__():
            articles.extend(Scraper().scrape().get_articles())
        self.assertEqual([], articles)


if __name__ == "__main__":
    unittest.main()
