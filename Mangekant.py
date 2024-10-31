
class kant:
    def __init__(self,kanter:int, lengder:list):
        self.kanter = kanter
        self.sider = kanter
        self.lengder = lengder

    def omkrets(self):
        omkretsen = 0
        for i in range(0,self.sider):
            omkretsen += self.lengder[i]
        return omkretsen
    
    def visInfo(self):
        print(f"kanten din har {self.kanter} mengde kanter og sider, og omkretsen er {self.omkrets()} lang :)")

class rektangel(kant):
    def __init__(self, lengde, bredde):
        super().__init__(lengde, bredde)
        self.lengde = lengde
        self.bredde = bredde
  
    def omkretsK(self):
        return self.omkrets()
    def areal(self):
        return self.lengde**2

class trekant(kant):
    def __init__(self, høyde):
        super().__init__()
        self.høyde = høyde
    def areal(self):
        self.lengde*self.høyde /2

""" i = 0
sider = int(input("hvor mange sider? "))
liste = []
while i < sider:
    liste.append(int(input(f"hvor lang er lengde {i+1}? ")))  
    i += 1
     
fourkatbnt = kant(sider, liste)
print(fourkatbnt.lengde)
print(fourkatbnt.omkrets())
fourkatbnt.visInfo() """

fankebank = kant(3,[4,2,6])
googleshlarp = kant(4,[4,2,6,7])
yimabadoo = kant(6,[6,6,6,6,6,6])

listeMedMangekanter = [fankebank,googleshlarp,yimabadoo] 

kvadrant = rektangel(5,7)
print(kvadrant.sider)
