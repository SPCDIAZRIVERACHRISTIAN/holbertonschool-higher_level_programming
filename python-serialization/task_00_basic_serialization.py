import json


def serialize_and_save_to_file(data, filename):
    """This function writes data into a json file"""

    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """This function takes data from a json file and returns it"""

    with open(filename, 'r') as file:
        return json.load(file)
