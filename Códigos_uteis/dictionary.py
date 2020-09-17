def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d        



#Example using get method 

h = histogram('casa')    

h
h.get('a',0)


def histogram2(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0) + 1
    return d

histogram2('casa')           

def print_hist(h):
    for key in sorted(h):
        print(key,h[key])

print_hist(h)

a = {1:'a',2:'b',3:'c'}

a

a[2]

for x in a:
    print(x,a[x])

b = a.values()

b

def reverse_lookup(d,v):
    for key in d:
        if d[key] == v:
            return key
    raise LookupError()        

reverse_lookup(a,'d')


h = histogram('parrot')
key = reverse_lookup(h,1)
key

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse 

hist = histogram('parrot')

inverse = invert_dict(hist)

inverse 

# Another solution for inverting a dict 

my_inverted_dict = dict()
for key, value in hist.items():
    my_inverted_dict.setdefault(value, list()).append(key)

my_inverted_dict

# Usage of memo (computed values kept for posterior use)
# using the fibonacci example 

know = {0:0,1:1}

def fibonacci2(n):
    if n in know:
        return know[n]
    
    res = fibonacci2(n-1) + fibonacci2(n-2)
    know[n] = res  
    return res

fibonacci2(5)     

know

# Test of fibonacci2 speed 

y = 1
while y < 10:   
    x = fibonacci2(y)
    y += 1
    print(x)

count = 1

def teste2():
    global count 
    count += 1
    return count 

teste2()


# Testing the difference of speed using Dict rather than List
# for pulling words.txt in a set object (dict with only keys) 

dicionario = set()

def dict_words():
    fin = open('words.txt')

    global dicionario

    #x = 1 used this for implementing integers as key 

    for line in fin:
        if line not in dicionario:
            dicionario.add(line.strip()) 
            #x += 1
    return dicionario     

dict_words()

x = 'yes'

x in dicionario

#Create a dictionary traversing the set using for and computing it as the key, 
#while the value is the product of the operation 

{x: x**2 for x in (2,4,6)}

# Methods for dict manipulation 

sorted(hist)
sorted(inverse)

list(hist)
list(inverse)

#Implementing for using two references in the dict, like in the e.g. bellow, makes 
#reference to both k(key) and v(value)

# items() allow to retreive key and value at the same time 

for k, v in hist.items():
    print(k, v)

for k, v in inverse.items():
    print(k, v)

# enumerate() allow to retreive index and key at the same time

for i, v in enumerate(hist):
    print(i, v)


teste1 = ['name','location']
teste2 = ['robson','downtown']

for x, y in zip(teste1,teste2):
    print('What is your {0}?  It is {1}.'.format(x, y))

for x, y in zip(hist,inverse):
    print('What is your {0}?  It is {1}.'.format(x, y))



#Check the difference among dictionares 

def subtract(d1,d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

