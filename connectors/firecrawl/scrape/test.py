import unittest
from connectors.firecrawl.scrape.main import scrape

class TestScrapeMethod(unittest.TestCase):

    def test_scrape(self):
        params = {
            "url": "https://mairistumpf.com",
            "formats": ["markdown"],
            "only_main_content": True,
            "include_tags": None,
            "exclude_tags": None,
            "max_age": 0,
            "headers": None,
            "wait_for": 0,
            "mobile": True
        }
        result = scrape(params)
        self.assertTrue(result["success"])
        self.assertTrue(result["data"])

if __name__ == '__main__':
    unittest.main() 