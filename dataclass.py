# No dataclass

# class User:
#     def __init__(self,name,age,active=True):
#         self.name=name
#         self.age=age
#         self.active=active
    
#     def __reper__(self):
#         return f"User(name={self.name}, age={self.age}, active={self.active})"
    
# this dataclass
from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    name: str
    age: int
    active: bool =True


# test
u =User("Ali", 25)
print(u)

# default qiymatlar(eng sodda )

# @dataclass
# class Poduct:
#     name: str
#     price: float
#     stock: int=0

# p=Poduct("phone", 1200)
# print(p.stock)

# # field(default=...)
# # normal holar
# @dataclass
# class User:
#     name:str
#     age: int
#     active: bool=True

# field bilan
from dataclasses import dataclass, field


@dataclass
class User:
    name: str
    age:int
    active: bool=field(default=True)
    friends: list=field(default_factory=list)  #bu har bir objectga yangi list qilib beradi.

# mashq

@dataclass
class Product:
    name:str
    price:float
    tags:list=field(default_factory=list)
    avtive:bool= True
    created_at: datetime =field(default_factory=datetime.now)

p=Product("iphone",1200)
print(p)

# repr=False--mahfiy malumotlar bolganda

@dataclass
class User:
    name: str
    password: str=field(repr=False)

u=User("Nodirjon","12345")
print(u)

# compare=False
# == orqali taqqoslashda bu maydon ishga kirmasin
@dataclass
class Product:
    name: str
    price: float
    updated_at: str = field(compare=False)

p1= Product("phone",1000, "today")
p2=Product("phone",1000,"yesterday")

print(p1==p2)

# natija: True qaytaradi, chunki updated_at e'tiborga olinmagan.

# init=False
@dataclass
class Order:
    id:int
    amount: float
    status: str=field(default="pendding", init=False)

o=Order(10,200)
print(o)










        
