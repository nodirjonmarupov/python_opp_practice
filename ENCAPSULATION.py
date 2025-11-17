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




    
