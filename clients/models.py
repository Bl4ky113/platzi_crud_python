
from uuid import uuid4

class Client:
    def __init__ (self, name:str, company:str, email:str, position:str, id=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.id = id or uuid4()
 

    def to_dict (self):
        return vars(self)

    @staticmethod
    def schema ():
        return ["id", "name", "company", "email", "position"]
