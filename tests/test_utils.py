import unittest
import utils


class TestUtils(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRemoveDuplicates(self):
        duplicates = [("url2", "title", 123), ("url1", "title", 123),
                      ("url", "title", 123), ("url", "title", 123)]
        without_duplicates = [("url2", "title", 123),
                              ("url1", "title", 123), ("url", "title", 123)]
        result = utils.remove_duplicates(duplicates)
        self.assertEqual(without_duplicates, result)


if __name__ == "__main__":
    unittest.main()
