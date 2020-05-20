import json
import xml.dom.minidom


def json_prettifier(input=""):
    try:
        return json.dumps(json.loads(input), sort_keys=True, indent=4)
    except Exception:
        print("Not a Valid JSON")


def xml_prettier(input=""):
    try:
        xmlText = xml.dom.minidom.parseString(input)
        return xmlText.toprettyxml()
    except Exception:
        print("Not a valid XML")
