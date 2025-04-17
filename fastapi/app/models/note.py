from odmantic import Model

class Note(Model):
    title: str
    content: str
    username: str  # this links note to the user
