import json
from functools import reduce
from json.decoder import JSONDecodeError

def extract_data(str_obj, keys):
    """
    Extract data from a string-like json object.
    Returns a dictionary made up of the 'keys' passed as arguments (expressed in dot notation)
    and the corresponding value.

    Example

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
    obj = {}
    if not str_obj:
        return obj

    try:
        obj = json.loads(str_obj)
    except ValueError:
        raise

    result = {}
    for key in keys:
        value = get_value(obj, key)
        if value:
            result[key] = value
    return result


def get_value(obj, key):
    return reduce(lambda a,b: a[b] if b in a else None, key.split('.'), obj)