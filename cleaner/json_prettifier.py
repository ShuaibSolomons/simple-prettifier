import json


def json_prettifier(input=""):
    return json.dumps(json.loads(input), sort_keys=True, indent=4)
