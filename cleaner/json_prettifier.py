import json


def json_prettifier(input=""):
    try:
        return json.dumps(json.loads(input), sort_keys=True, indent=4)
    except(Exception):
        print(Exception)



