
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
    def omkretsK(self):
        return f"Omkretsen er "
    def areal(self):
        return self.lengde**2

class trekant(kant):
    def __init__(self, høyde):
        super().__init__()
        self.høyde = høyde
    def areal(self):
        self.lengde*self.høyde /2
    


lengde = input("Hvor lang? ")        
fourkatbnt = kant(4, lengde)
print(fourkatbnt.lengde)
