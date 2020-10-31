import json
from functools import reduce


def extract_data(str_obj, keys):
    """
    Extract data from a string-like json object.
    Returns a dictionary made up of the 'keys' passed as arguments (expressed in dot notation)
    and the corresponding value.
    if the key does not exist then the resulting dictionary will not have that key.

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
        value = reduce(lambda d, k: d.get(k, None) if d else None, key.split("."), obj)
        if value:
            result[key] = value
    return result
