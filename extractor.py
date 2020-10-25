import json
from functools import reduce

def extract_data(str_obj, keys):
    """
    Extract data from a string-like json object.
    Returns a dictionary made up of the 'keys' passed as arguments (expressed in dot notation)
    and the corresponding value.

    Example
    =======
    INPUT:
        a= '{
                "guid": "1234",
                "content": {
                    "type": "text/html",
                    "title": "Challenge 1",
                    "entities": [ "1.2.3.4", "wannacry", "malware.com"]
                },
                "score": 74,
                "time": 1574879179
        }'
        b = ["guid", "content.entities", "score", "score.sign"]

        > extract_data(a,b)

    OUTPUT:
        { "guid": "1234", "content.entities": [ "1.2.3.4", "wannacry", "malware.com"], "score": 74 }

    """
    obj = json.loads(str_obj)
    result = {}
    for key in keys:
        result[key] = get_value(obj, key)
    return result


def get_value(obj, key):
    return reduce(lambda a,b: a[b], key.split('.'), obj)