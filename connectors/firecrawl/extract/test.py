import unittest
from connectors.firecrawl.extract.main import extract, get_extract_status
import time

class TestExtractMethod(unittest.TestCase):

    def test_extract(self):
        result = extract({
            "urls": ["https://mairistumpf.com"],
            "prompt": "Extract how many years of experience the professional has"
        })
        self.assertTrue(result["success"])
        self.assertTrue("id" in result)
        extract_id = result["id"]
        
        # Now test get_extract_status with the actual extract ID
        while True:
            status_result = get_extract_status(extract_id)
            if status_result["status"] != "processing":
                self.assertTrue(status_result["success"])
                self.assertTrue("data" in status_result)
                break
            time.sleep(2)

if __name__ == '__main__':
    unittest.main() 