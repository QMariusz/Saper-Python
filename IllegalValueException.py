class IllegalValueException(Exception):
    def __init__(self, comment):
        self.comment = comment
w
    def __str__(self):
        return self.comment
