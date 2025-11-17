class Odam:
    def __init__(self,ism,yosh):
        print("INIT ISHLADI")
        self.ism=ism
        self.yosh=yosh

    def salom(self):
        print("SALOM ISHLADI")
        return f"Salom, men {self.ism} "
    
a=Odam("Nodirjon",23)
print(a.salom())
       # Salom, men Nodirjon

# class-> reja/shablon
# object->shablon yaratadigan narsa
# __init__ -> object ishlaganda avto ishlaydi
# Self-> objectning o'zi

b=Odam("Ali",30)
print(b.salom())
    # Salom, men Ali

# Inheritance(meros olish)
class Transport:
    def __init__(self,nom,tezlik):
        self.nom=nom
        self.tezlik=tezlik
    
    def info(self):
        return f"ushbu mashinaning rusumi {self.nom}, tezligi {self.tezlik}km/h, rangi {self.rang}"
    
#   child class      
class Mashina(Transport):

    def __init__(self,nom,tezlik,rang):
        super().__init__(nom, tezlik)   #parametr __init__ chaqiradi
        self.rang=rang

    def info(self):
        return f"ushbu mashinaning rusumi {self.nom}, tezligi {self.tezlik}km/h, rangi {self.rang}"
    
m=Mashina("BMW", 220, "qora")
print(m.info())

