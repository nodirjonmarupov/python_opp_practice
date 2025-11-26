# Iterator
class Counter:
    def __init__(self,limit):
        self.limit=limit
        self.current=0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.limit:
            self.current +=1
            return self.current
        else:
            raise StopIteration
        
# foydalanish
c=Counter(5)
for i in c:
    print(i)

# Generator
# misol_1

def counter(limit):
    num=1
    while num <=limit:
        yield num
        num+=1

# foydalanish
for x in counter(5):
    print(x)

# misol_2

def read_file(path):
    with open(path) as file:
        for line in file:
            yield line

# mashqlar
class Intedor:
    def __init__(self, natija):
        self.natija=natija
        self.current=0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.natija:
            self.current +=1
            return self.current
        else:
            raise StopIteration
        
# foydalanish
a =Intedor(10)
for x in a:
    print(x)

# No_2- string uchun Iterator
class WordIterator:
    def __init__(self, word):
        self.word=word
        self.index=0
    
    def __iter__(self):
        return self
    
    
    def __next__(self):
        if self.index < len(self.word):
            harf=self.word[self.index]
            self.index +=1
            return harf
        else:
            raise StopIteration
        
# foydalanish

w =WordIterator("cat")
for i in w:
    print(i)

# No_3.mashq

class Juft:
    def __init__(self,even):
        self.even=even
        self.number=2

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.number <= self.even:
            current=self.number
            self.number+=2
            return current
        else:
            raise StopIteration

# foydalanish
for q in Juft(10):
    print(q)

# GENERATOR

def id_generator(prefix="ID"):
    num=1
    while True:
        yield f"{prefix}-{num}"
        num +=1

ids=id_generator("USER")
print(next(ids))
print(next(ids))
print(next(ids))
print(next(ids))
print(next(ids))
print(next(ids))



        



