import unittest
from extractor import extract_data

class TestExtractor(unittest.TestCase):
    def test_when_keys_are_passed_with_up_to_one_level_deep(self):
        str_obj = """
            {
                "guid": "1234",
                "content": {
                    "type": "text/html"
                },
            }
        """
        keys = ['guid', 'content.type']
        expected_result = {'guid': '1234', 'content.type': 'text/html'}

        actual_result = extract_data(str_obj, keys)

        self.assertEquals(actual_result,
                          expected_result,
                          'It should return a dictionary with the keys expressed in dot notation and its values')

