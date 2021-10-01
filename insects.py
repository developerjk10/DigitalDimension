import _init_ as mammals
class notmammals(mammals):
    def __init__(self,name, age, why):
        self.why = why
    def setWhy(self, why):
        self.why = why
    def getWhy(self):
        return  self.why

