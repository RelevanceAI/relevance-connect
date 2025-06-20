import unittest
from connectors.firecrawl.search.main import search

class TestSearchMethod(unittest.TestCase):

    def test_search(self):
        result = search({"query": "who discovered the universe"})
        self.assertTrue(result["success"])
        self.assertTrue(result["data"])

if __name__ == '__main__':
    unittest.main() 