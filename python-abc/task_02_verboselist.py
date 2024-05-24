class VerboseList(list):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def append(self, item):
        print("Added: [{}] to the list".format(item))
        return super().append(item)

    def extend(self, items):
        print('Extended the list with [{}] items.'.format(len(items)))
        return super().extend(items)

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        return super().remove(item)

    def pop(self, index=0):
        if index is None:
            index = len(self) - 1
        print("Popped [{}] from the list.".format(index))
        return super().pop(index)
