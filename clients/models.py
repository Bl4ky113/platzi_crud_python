
from uuid import uuid4

class Client:
    def __init__ (self, name:str, company:str, email:str, position:str, idx=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.idx = idx or uuid4()
 

    def to_dict (self):
        return vars(self)

    @staticmethod
    def schema ():
        return ["idx", "name", "company", "email", "position"]
