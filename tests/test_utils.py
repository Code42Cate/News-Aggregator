import unittest
import utils


class TestUtils(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRemoveDuplicates(self):
        duplicates = [("url2", "title"), ("url1", "title"),
                      ("url", "title"), ("url", "title")]
        without_duplicates = [("url2", "title"),
                              ("url1", "title"), ("url", "title")]
        result = utils.remove_duplicates(duplicates)
        self.assertEqual(without_duplicates, result)


if __name__ == "__main__":
    unittest.main()
