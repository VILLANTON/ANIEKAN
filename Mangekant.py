import math

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

class kvadrat(rektangel):
    def __init__(self,lengde,kanter):
        self.lengde = lengde
        self.kanter = kanter
        super().__init__()
    def omkretsK(self):
        return f"Omkretsen er {self.lengde * {self.kanter}}"
    def areal(self):
        return self.lengde**2

class Trekant(kant):
    def __init__(self, a, b, c):
        super().__init__(3, [a, b, c])
        self.a = a
        self.b = b
        self.c = c
    
    def omkrets(self):
        return self.a + self.b + self.c
    
    def areal(self):
        s = self.omkrets() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def __str__(self):
        return (f"areaket er {self.areal()}")

A = Trekant(5,5,5)


print(f"{A}")



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

""""
fankebank = kant(3,[4,2,6])
googleshlarp = kant(4,[4,2,6,7])
yimabadoo = kant(6,[6,6,6,6,6,6])

listeMedMangekanter = [fankebank,googleshlarp,yimabadoo] 

kvadrant = rektangel(5,7)
print(kvadrant.sider) """
