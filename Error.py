class WrongDataException(Exception):
    def __init__(self, comment):
        self.comment = comment

    def __str__(self):
        return self.comment
