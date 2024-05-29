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
        with open(filename, 'wb') as file:
            try:
                file.write(pickle.dumps(self.__dict__))
            except pickle.PicklingError as e:
                return None

    @classmethod
    def deserialize(cls, filename):
        with open(filename, 'rb') as file:
            return cls(**pickle.loads(file.read()))
