import unittest
from connectors.firecrawl.crawl.main import crawl, get_crawl_status, cancel_crawl
import time

class TestCrawlMethod(unittest.TestCase):

    def test_crawl(self):
        result = crawl({
            "url": "https://www.example.com",
            "max_depth": 1,
            "max_discovery_depth": 5,
            "ignore_sitemap": False,
            "ignore_query_parameters": False,
            "limit": 5,
            "allow_backward_links": True
        })
        self.assertTrue(result["success"])
        self.assertTrue("id" in result)
        crawl_id = result["id"]

        # Now test get_crawl_status with the actual crawl ID
        while True:
            status_result = get_crawl_status(crawl_id)
            if status_result["status"] != "scraping":
                break
            time.sleep(5)
        self.assertTrue("status" in status_result)
        self.assertEqual(status_result["status"], "completed")

    def test_cancel_crawl(self):
        result = crawl({
            "url": "https://www.example.com",
            "max_depth": 1,
            "max_discovery_depth": 5,
            "ignore_sitemap": False,
            "ignore_query_parameters": False,
            "limit": 5,
            "allow_backward_links": True
        })
        self.assertTrue(result["success"])
        self.assertTrue("id" in result)
        crawl_id = result["id"]
        
        # Test cancel_crawl
        cancel_result = cancel_crawl(crawl_id)
        self.assertEqual(cancel_result["status"], "cancelled")

if __name__ == '__main__':
    unittest.main() 