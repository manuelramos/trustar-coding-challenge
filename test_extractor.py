import unittest
from extractor import extract

class TestExtractorMethods(unittest.TestCase):
    """
    Example:
    '{
        "guid": "1234",
        "content": {
            "type": "text/html",
            "title": "Challenge 1",
            "entities": [ "1.2.3.4", "wannacry", "malware.com"]
        },
        "score": 74,
        "time": 1574879179
    }'
    """
    def test_when_pass_single_prop_should_return_single_value(self):
        # obj = '{\"guid\":\"1234\",\"content\":{\"type\":\"text\/html\",\"title\":\"Challenge 1\",\"entities\":[\"1.2.3.4\",\"wannacry\",\"malware.com\"]},\"score\":74,\"time\":1574879179}'
        str_obj = """
            {
                "guid": "1234",
                "content": {
                    "type": "text/html",
                    "title": "Challenge 1",
                    "entities": [ "1.2.3.4", "wannacry", "malware.com"]
                },
                "score": 74,
                "time": 1574879179
            }
        """
        keys = ['guid', 'content.type']

        expected_result = {'guid': '1234', 'content.type': 'text/html'}
        actual_result = extract(str_obj, keys)

        self.assertEquals(actual_result, expected_result, 'should return a dict with the corresponding values')

