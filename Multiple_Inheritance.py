class A:
    def feature_a(self):
        print("Feature A")

class B:
    def feature_b(self):
        print("Feature B")

class C(A,B):
    pass
   
# test

c=C()
c.feature_a()
c.feature_b()
# --- Feature A
# ---Feature B

# super() ishlaydigan:

class A:
    def show(self):
        print("A -> show()")

class B:
    def show(self):
        print("B-> show()")

class C(A,B):
    def show(self):
        print("C-> show()")
        super().show()

obj=C()
obj.show()

# DIAMOND PROBLEM

class A:
    def say(self):
        print("A")

class B(A):
    def say(self):
        print("B")
        super().say()

class C(A):
    def say(self):
        print("C")
        super().say()

class D(B,C):
    def say(self):
        print("D")
        super().say()

# test
D().say()

print(D.mro())


# mashq PAYMENT

class LoggingMixin:
    def process(self):
        print("Logging: payment started")
        super().process()

class NotificationMixin:
    def process(self):
        print("Notification: user notified")
        super().process()

class PaymentMixin:
    def process(self):
        print("Payment: transactoin completed")
        super().process()

class BaseProcessor:
    def process(self):
        print("BaseProcessor: done")

class PaymentProcessor(LoggingMixin,NotificationMixin,PaymentMixin,BaseProcessor):
    pass

# test
p=PaymentProcessor()
p.process()