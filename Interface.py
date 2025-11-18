from abc import ABC, abstractmethod
class Payment(ABC):

    def pay(self,amount):
        pass
    def refund(self,amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        return f"CreditCard orqali {amount}$ to'landi"
    
    def refund(self, amount):
        return f"CreditCard orqali {amount}$ qaytarildi"
    
c=CreditCard()
print(c.refund(20))

class PayPal(Payment):
    def pay(self, amount):
        return f"PayPal orqali {amount}$ to'landi"
    
    def refund(self, amount):
        return f"PayPal orqali {amount}$ qaytarildi"
    
q=PayPal()
print(q.pay(50))

# Interface + Polymorphism
systems= [PayPal(),CreditCard()]
for s in systems:
    print(s.pay(100))

# mashq
class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass
class EmailNotifier(Notifier):
    def send(self, message):
        return f"Email orqali {message} yuborildi"
    
class SmsNotifier(Notifier):
    def send(self, message):
        return f"SMS orqali {message} yuborildi"

xabar=[EmailNotifier(),SmsNotifier()]
for x in xabar:
    print(x.send("salom"))


# INHERITANCE-meros olish
class Hayvon:
    def __init__(self,name):
        self.name=name
    
class It(Hayvon):
    def __init__(self, name,age):
        super().__init__(name)
        self.age=age

# mashq

class Employee:
    def __init__(self,name, salary):
        self.name=name
        self.salary=salary
    
    def info(self):
        print(f"Name:{self.name}")
        print(f"Salary:{self.salary}")
class Developer(Employee):
    def __init__(self, name, salary,programming_language):
        super().__init__(name, salary)
        self.language=programming_language
    
    def info(self):
        super().info()
        print(f"Programming language:{self.language}")

class Designer(Employee):
    def __init__(self, name, salary, tool):
        super().__init__(name, salary)
        self.tool=tool

    def info(self):
        super().info()
        print(f"Design Tool:{self.tool}")

# test
dev=Developer("Ali",1500,"Python")
design=Designer("Madina",1200,"Figma")

dev.info()
print()
design.info()