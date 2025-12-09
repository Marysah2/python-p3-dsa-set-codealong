

class MySet:
    def __init__(self, enumerable=None):
        self.dictionary = {}
        if enumerable is not None:
            for item in enumerable:
                self.dictionary[item] = True

    def has(self, value):
        return value in self.dictionary

    def add(self, value):
        self.dictionary[value] = True
        return self

    def delete(self, value):
        if value in self.dictionary:
            del self.dictionary[value]
            return True
        return False

    def size(self):
        return len(self.dictionary)

    def clear(self):
        self.dictionary = {}

    def __str__(self):
        return f"{{{', '.join(str(k) for k in self.dictionary.keys())}}}"