
class kant:
    def __init__(self,kanter, lengde):
        self.kanter = kanter
        self.sider = kanter
        self.lengde = lengde
    def omkrets(self):
        return f"{self.kanter * self.lengde}"

class kvadrat(kant):
    def __init__(self):
        super().__init__()
    


lengde = input("Hvor lang? ")        
fourkatbnt = kant(4, lengde)
print(fourkatbnt.lengde)
