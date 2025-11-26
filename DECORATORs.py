
class User:
    def __init__(self,name):
        self._name=name
    @property

    def name(self):
        return self._name
    
u=User("ali".upper())
print(u.name)

# SETTER-o'zgarishni nazorat qilish
class User:
    def __init__(self,age):
        self._age=age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,value):
        if value<0:
            raise ValueError ("yosh MANFIYga bolish mumkun emas")
        self._age=value

u=User(20)
u._age=30
print(u.age)

# staticmethod

class Math:
    @staticmethod
    def add(a,b):
        return a+b
    
print(Math.add(5,5 ))

# classmethod
class User:
    def __init__(self,name):
        self.name=name
    @classmethod
    def from_upper(cls, name):
            return cls(name.upper())

u=User.from_upper("ali")
print(u.name)

# mashq

class BankAccount:
    USD_RATE= 13000    #1$=13 000 SO'M

    def __init__(self,balance):
        self.__balance=balance  #private

        @property
        def balance(self):
            return self._balance
        @balance.setter
        def balance(self,value):
            if value < 0:
                raise ValueError("Balans manfiy bo'lishi mumkun emas!")
            self.__balance=value

        @staticmethod
        def usd_to_uzs(amount):
            return amount * BankAccount.USD_RATE
        
        @classmethod
        def from_usd(cls,usd_amount):
            uzs=cls.usd_to_uzs(usd_amount)
            return cls(uzs)

# test
acc=BankAccount(50000)
print(acc._BankAccount__balance)


        
        
