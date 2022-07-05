import unittest

from src.jbzd import Scraper


class TestPage(unittest.TestCase):

    def test_mainpage(self):
        page = Scraper().getPage(1)
        self.assertNotEqual(page, '', 'Should contain content')


if __name__ == '__main__':
    unittest.main()
