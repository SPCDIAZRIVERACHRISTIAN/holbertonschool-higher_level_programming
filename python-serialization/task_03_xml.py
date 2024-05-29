import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("root")
    for key, value in dictionary:
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
        return dictionary
