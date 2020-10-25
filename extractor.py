import json
from functools import reduce

def extract(str_obj, keys):
    obj = json.loads(str_obj)
    result = {}
    for key in keys:
        result[key] = _get_value(obj, key)
    return result


def _get_value(obj, key):
    return reduce(lambda a,b: a[b], key.split('.'), obj)