# _balance > protected(o'zgartirilishi kerak emas)
# __balance > private(tashqaridan umuman korinmaydi)

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner=owner
#         self._balance=balance
#         self.__pin=1234
        
# acc=BankAccount("Ali",2000)
# acc._balance=5000
# print(acc.owner)
# print(acc._balance)

 # GETTER & SETTER

class BankAccount:
    def __init__(self, owner, balance):
        self.owner=owner
        self.__balance=balance
        
    # GETTER
    def get_balance(self):
        return self.__balance
    
    # SETTER
    def set_balance(self, value):
        if value < 0:
            print("Manfiy sonni bo'lish mumkun emas!")
        else:
            self.__balance=value

acc=BankAccount("Vali",5000)
acc.set_balance(-100)
print(acc.get_balance())

# POLYMORPHISIM- kod orqali tushunish

class Dog:
    def speak(self):
        return "wooof"
    
class Cat:
    def speak(self):
        return "meow"
    
class Human:
    def speak(self):
        return "hello"
    
animals= [Dog(), Cat(), Human()]
for a in animals:
    print(a.speak())
# terminal:
        # wooof
        # meow 
        # hello   

# ABSTRACT CLASS+METHOD OVERRIDING

from abc import ABC, abstractmethod

# class Car(ABC):
#      def start(self):
#          pass
# class Tesla(Car):
#     def start(self):
#         return "Tesla started"
# t=Tesla()
# print(t.start())

class Animal(ABC):
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "meow"
a=Dog()
print(a.sound())

b=Cat()
print(b.sound())


    
