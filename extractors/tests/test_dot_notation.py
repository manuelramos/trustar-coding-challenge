import unittest

from extractors.dot_notation import get_data


class TestDotNotationGetData(unittest.TestCase):
    def setUp(self):
        self.str_json_obj = (
            "{"
            + '"guid": "1234",'
            + '"content": {"t   ype": "text/html"},'
            + '"score":4321,'
            + '"headers":{"connection": "close"},'
            + '"resource_response":{"error":{"extra_data":{"message":"No user present"}}},'
            + '"arrayed": {"items": [{"id": 1, "value": "UNO"}, {"id": 2, "value": "DOS"}]},'
            + '"complex": [{"items": [{"id": 1, "value": "UNO"}, {"id": 2, "value": "DOS"}]},'
            + '{"items": [{"id": 3, "value": "TRES"}, {"id": 4, "value": "CUATRO"}]}]'
            + "}"
        )

    def test_when_keys_are_passed_with_up_no_level_deep(self):
        keys = ["guid", "score"]
        expected_result = {"guid": "1234", "score": 4321}

        actual_result = get_data(self.str_json_obj, keys)

        self.assertDictEqual(
            actual_result,
            expected_result,
            "It should return a dictionary with the keys and its values",
        )

    def test_when_keys_are_passed_with_up_to_one_level_deep(self):
        keys = ["guid", "content.type"]
        expected_result = {"guid": "1234", "content.type": "text/html"}

        actual_result = get_data(self.str_json_obj, keys)

        self.assertDictEqual(
            actual_result,
            expected_result,
            "It should return a dictionary with the keys expressed in dot notation and its values",
        )

    def test_when_malformed_json_obj_is_passed(self):
        malformed_str_json_obj = '{"prop:2'
        keys = ["prop"]

        with self.assertRaises(ValueError):
            get_data(malformed_str_json_obj, keys)

    def test_when_keys_with_up_no_level_deep_does_not_exist(self):
        keys = ["guid", "non-existent1", "non-existent2"]
        expected_result = {"guid": "1234"}

        actual_result = get_data(self.str_json_obj, keys)

        self.assertDictEqual(
            actual_result,
            expected_result,
            "It should return a dictionary with the values of the keys that do exist",
        )

    def test_when_keys_with_up_to_one_level_deep_does_not_exist(self):
        keys = ["guid", "content.level2", "headers.level2"]
        expected_result = {"guid": "1234"}

        actual_result = get_data(self.str_json_obj, keys)

        self.assertDictEqual(
            actual_result,
            expected_result,
            "It should return a dictionary with the values of the keys that do exist",
        )

    def test_when_no_str_json_object_is_passed_as_parameter(self):
        keys = ["guid"]
        expected_result = {}

        actual_result = get_data(None, keys)

        self.assertDictEqual(
            actual_result,
            expected_result,
            "It should return a dictionary with the values of the keys that do exist",
        )

    def test_when_arbitrary_existing_nested_sequence_properties(self):
        arbitrary_nested_props = ["resource_response.error.extra_data.message"]
        expected_result = {"resource_response.error.extra_data.message": "No user present"}

        actual_result = get_data(self.str_json_obj, arbitrary_nested_props)

        self.assertDictEqual(
            actual_result,
            expected_result,
            "It should return a dictionary with the value for the nested properties",
        )

    def test_when_arbitrary_nested_sequence_properties_with_some_nonexistent(self):
        arbitrary_nested_props = ["resource_response.error.extra_data.does_not_exist.message"]
        expected_result = {}

        actual_result = get_data(self.str_json_obj, arbitrary_nested_props)

        self.assertDictEqual(
            actual_result,
            expected_result,
            "It should return a dictionary without the nested properties as key",
        )

    def test_when_accessing_arrayed_properties(self):
        arrayed_properties = ["complex[1].items[0].value"]
        expected_result = {"complex[1].items[0].value": "TRES"}
        actual_result = get_data(self.str_json_obj, arrayed_properties)

        self.assertDictEqual(
            actual_result, expected_result, "It should return a dict with the arrayed nested property with it value"
        )

    def test_when_accessing_arrayed_properties_and_invalid_indice(self):
        arrayed_properties = ["arrayed.items[20].value"]
        expected_result = {}

        actual_result = get_data(self.str_json_obj, arrayed_properties)

        self.assertDictEqual(
            actual_result, expected_result, "It should return a dictionary without the nested failed property"
        )

    def test_when_accessing_malformed_arrayed_properties(self):
        arrayed_properties = ["arrayed.items.value"]
        expected_result = {}

        actual_result = get_data(self.str_json_obj, arrayed_properties)

        self.assertDictEqual(
            actual_result, expected_result, "It should return a dictionary without the nested failed property"
        )
