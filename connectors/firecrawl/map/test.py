import unittest
from connectors.firecrawl.map.main import map

class TestMapMethod(unittest.TestCase):

    def test_map(self):
        result = map({"url": "https://www.firecrawl.dev"})
        self.assertTrue(result["success"])
        self.assertTrue(result["links"])

if __name__ == '__main__':
    unittest.main() 