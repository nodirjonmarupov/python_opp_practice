# eng sodda misol

def add(a: int, b: int) -> int:
    return a+b

a=add(5,10)
print(a)

def format_user(name:str, age: int,active:bool)->str:
    return f"{name} - {age} yosh. Active: {active}"

# O'zgaruvchilar:

age:int=24
name:str="Nodirjon"
price:float=3.5
is_active:bool=True

# list typing

numbers:list[int]=[1,2,3]
names: list[str]=["ali","vali"]

# Dictionary typing

user: dict[str,str]={
    "name":"ALI",
    "city":"TASHKENT"
}

balances: dict[str,str]={
    "ALI":100,
    "VALI":200
}

# OPTIONAL(None bo'lishi mumkun)
from typing import Optional

age:Optional[int]=None

# UNION

from typing import Union

def convert(value:Union[int, float]) -> float:
    return float(value)

# AMALIY MASHIQ

class BankAccount:
    def __init__(self, owner:str, balance: int)-> None:
        self.owner: str=owner
        self.__balance: int = balance

    def deposit(self,amount: int)-> None:
        self.__balance+= amount

    def get_balance(self)-> int:
        return self.__balance
    
for a in BankAccount:
    print(a)
