import uuid

class Client:
    def __init__(self,name,company,mail,age,uid=None):
        self.name=name
        self.company = company
        self.mail = mail
        self.age = age
        self.uid = uid or uuid.uuid4()
    def to_dict(self):
        return vars(self)
    
    @staticmethod
    def schema():
        return ['name','company','mail','age','uid']
