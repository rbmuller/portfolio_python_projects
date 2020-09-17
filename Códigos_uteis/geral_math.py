def absolute_value(x,y):
    if x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return -1

absolute_value(3,2)        


import math 

#funcao para calcular area 

def area(radius):
    x = math.pi * radius**2
    return x

area(12)    

#funcao para calular raio
def distance(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
    dsquare = (dx**2) + (dy**2)
    print(dsquare)
    result = math.sqrt(dsquare)
    return result

distance(1,2,4,6)    
   
#fazendo encapsulamento, usando uma
#funcao para calcular outra 

def circle_area(xc,yx,xp,yp):
    #radius = distance(xc,yx,xp,yp)
    #result = area(radius)
    #return result 
    return area(distance(xc,yx,xp,yp))

circle_area(1,4,2,8)    

import math 

def hypotenuse(x,y):
    hyp = (x**2) + (y**2)
    result = math.sqrt(hyp)
    return result

hypotenuse(2,2)


def is_divisible(x,y):
    return x % y == 0

is_divisible(4,2)    

def is_between(x,y,z):
    return x<=y<=z

is_between(5,5,5)

def factorial(n):
    if n == 0:
        return 1 
    else:
        recurse = factorial(n-1)
        result = n*recurse
        return result    

factorial(1.5)       

#Numero Fibonacci é a soma dos 2 num antecessores 

def fibonacci(n):
    if n == 0: 
        return 0 
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(10)


y = 1
while y < 100:
    x = fibonacci(y)
    y = y + 1 
    print(x)


#Funcao fatorial esta aplicando apenas para int, isinstance 
#checa se o valor tem a entrada pedida

def factorial(n):
    if not isinstance(n,int):
        print ('This Factorial func just applies for integers!')
        return None
    elif n < 0:
        print('Cannot calculate negative Factorials')
        return None 
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)        

factorial(5)        

#Ackermann function

def b(z):
    prod = a(z,z)
    print(z, prod)
    return prod

def a(x,y):
    x = x+1
    return x * y

def c(x,y,z):
    total = x + y + z
    square = b(total)**2
    return square

c(1,2,3)



while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)

print('Boa moleque!')    