import unittest
from extractor import extract_data

class TestExtractor(unittest.TestCase):

    def setUp(self):
        self.str_obj = '{\"guid\": \"1234\", \"content\": {\"type\": \"text/html\"}, \"score\":4321}'

    def test_when_keys_are_passed_with_up_no_level_deep(self):
        keys = ['guid', 'score']
        expected_result = {'guid': '1234', 'score': 4321}

        actual_result = extract_data(self.str_obj, keys)

        self.assertDictEqual(actual_result,
                             expected_result,
                             'It should return a dictionary with the keys and its values')

    def test_when_keys_are_passed_with_up_to_one_level_deep(self):
        keys = ['guid', 'content.type']
        expected_result = {'guid': '1234', 'content.type': 'text/html'}

        actual_result = extract_data(self.str_obj, keys)

        self.assertDictEqual(actual_result,
                             expected_result,
                             'It should return a dictionary with the keys expressed in dot notation and its values')

