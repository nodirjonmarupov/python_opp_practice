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

# mashq 1:

class Maxsulot:
    def __init__(self, nom,narx,chegirma,kategoriya):
        self.nom=nom
        self.narx=narx
        self.chegirma=chegirma
        self.kategoriya=kategoriya
        

    def chegirmali_narx(self):
        return self.narx-(self.narx* self.chegirma /100)
    def info(self):
        return f"Maxsulot: {self.nom}, tan narxi: {self.narx}, hozirda {self.chegirma}% chegirmada, yakuniy narx:{self.chegirmali_narx()}$, kategoriya:{self.kategoriya}"
    
q=Maxsulot("Iphone 17",1200,20,"Elektronika")

print(q.info())

