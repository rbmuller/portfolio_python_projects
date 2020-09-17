#Generating 10 random numbers
import random

for i in range(10):
    x = random.random()
    print(x)

#Generating 10 random numbers using randint, that takes min and max values. 
import random

for i in range(10):
    x = random.randint(2,10)
    print(x)

#choice allows to randomly select a number from a sequence 
lis = [1,2,3]
t = (1,2,3)
d = {1:'a',2:'b',3:'c'}

type(d)

random.choice(d)

