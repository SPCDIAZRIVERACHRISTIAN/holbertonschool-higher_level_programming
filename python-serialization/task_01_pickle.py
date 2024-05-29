import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        if type(self.is_student) is bool:
            print("Is Student {}".format(self.is_student))

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            print(f"Error while serializing: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            return obj
        except (EOFError, FileNotFoundError) as e:
            print(f"Error while deserializing: {e}")
            return None
