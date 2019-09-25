import unittest
import utils
from article import Article


class TestUtils(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_remove_database_articles(self):
        articlesA = [Article("url0", "title0"), Article("url1", "title1")]
        articlesB = [Article("url0", "title0")]
        expectedC = [Article("url1", "title1")]
        result = utils.remove_database_articles(articlesA, articlesB)
        self.assertEqual(len(expectedC), len(result))
        index = 0
        while index < len(result):
            self.assertEqual(
                result[index].url, expectedC[index].url)
            self.assertEqual(
                result[index].title, expectedC[index].title)
            self.assertEqual(
                result[index].content, expectedC[index].content)
            self.assertEqual(
                result[index].keywords, expectedC[index].keywords)
            index += 1

    def test_remove_faulty_objects(self):
        articlesA = [Article("url0", "title0"), Article("url1", "title1")]
        articlesB = [Article("url0", "title0")]
        expectedC = [Article("url1", "title1")]
        result = utils.remove_faulty_objects(articlesA, articlesB)
        self.assertEqual(len(expectedC), len(result))
        index = 0
        while index < len(result):
            self.assertEqual(
                result[index].url, expectedC[index].url)
            self.assertEqual(
                result[index].title, expectedC[index].title)
            self.assertEqual(
                result[index].content, expectedC[index].content)
            self.assertEqual(
                result[index].keywords, expectedC[index].keywords)
            index += 1

    def test_article_tuples_to_objects(self):
        article_tuples = [("url0", "title0"), ("url1", "title1")]
        expected_article_objects = [
            Article("url0", "title0"), Article("url1", "title1")]
        article_objects = utils.article_tuples_to_objects(article_tuples)
        self.assertEqual(len(expected_article_objects), len(article_objects))
        index = 0
        while index < len(article_objects):
            self.assertEqual(
                article_objects[index].url, expected_article_objects[index].url)
            self.assertEqual(
                article_objects[index].title, expected_article_objects[index].title)
            self.assertEqual(
                article_objects[index].content, expected_article_objects[index].content)
            self.assertEqual(
                article_objects[index].keywords, expected_article_objects[index].keywords)
            index += 1

    def test_remove_duplicate_articles(self):
        articlesA = [Article("url0", "title0"), Article(
            "url1", "title1"), Article("url1", "title1")]
        result = utils.remove_duplicate_articles(articlesA)
        self.assertEqual(len(result), 2)
        self.assertTrue(result[0].url is not result[1].url)
        self.assertTrue(result[0].title is not result[1].title)


if __name__ == "__main__":
    unittest.main()
