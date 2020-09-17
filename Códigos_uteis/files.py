#so far we have seen virtual programs 
# We gonna see now writable files using pickle

#Example:

#The w parameter means we can write in this file. 
#if the file already exists in the write mode clears out
#the old data and starts fresh, so be careful 
#if the file doesn't exist, a new one is created

fout = open('output.txt', 'w')

line1 = "This here's the wattle,\n"
fout.write(line1)

line2 = "the emblem of our land.\n"
fout.write(line2)

fout.close()

#The argument for 'write' have to be a string
#if other values must go the file, they first have
#to be converted to string 

#Ex, it will generate an error:
x = 52
fout.write(str(x))


#Format operator, the % symbol followed by an integer is the modulus
#operator. But followed by a string is the format operator
#The first operand is the format string, which specify how the second operator
#is formatted. The result is a string. 

4%3

camels = 42
type(camels)

'%d' % camels

'I have spotted %d camels.' % camels

# %d means the second operand is formatted as a decimal integer
# %g means the second operand is formatted as a floating-point number
## %s means the second operand is formatted as string

'In %d years I have spotted %g %s.' % (3,0.1,'camels')

#cwd stands for Current Working Directory 

import os
cwd = os.getcwd()
cwd

#change main directory 
#os.chdir(os.path.dirname(os.path.abspath('/Users/robsonmuller/Documents/Projetos_Python')))

os.getcwd()

#Check path, Check if exists, check if is a directory, check if is a file

os.path.abspath('output.txt')
os.path.exists('output.txt')
os.path.isdir('/Users/robsonmuller/Documents')
os.path.isfile('words.txt')

os.listdir(cwd)

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

walk(cwd)

output = open('output.txt')

for x in output:
    print(x)

#You can handle exceptions with try statment. It is called 'catching' as exception 
# it gives the chance to fix the problem or try again, or even end the program
# in an user oriented manner. 

try:
    fin = open('bad_file')
except:
    print('Something went wrong')    

#dbm is the command used for creating and updating database files
#creating them is similar to creating files. 
#However, in contrast of the first example, were we created the 'fout' file, the dbm command
#is used to create a file that organizes other files


import dbm 

db = dbm.open('caption','c')
#the mode 'c' means that the database should be created
#if it doesn't already exist

db['cleese.png'] = 'Photo of Robson' 

db['cleese.png']

#some dictionary methods such as key or items don't work with databases
#but iteration with a for loop works:

for key in db:
    print(key, db[key])

db.close()    


#A limitation of dbm is that keys and values have to be strings or bytes
#The pickle module can help, it translates almost any type of object
#into a string suitable for storage in a database, and than translates
#strings back into objects

import pickle 

t1 = [1,2,3]
type(t1)

#db['file 2'] = s 
#pickle.loads(db['file 2'])

s = pickle.dumps(t1)
type(s)


t3 = pickle.loads(s)
type(t3)
t3
#The list were converted to bytes using pickle.dumps, than we checked it's format 
#as bytes. So, how can we read it? We use the pickle.loads command. 

#Although the new object has the same value as the old, 
#it is not (in general) the same object:

t1 == t3

t1 is t3

#PIPES
#pipe object: An object that represents a running program, 
#allowing a Python program to run commands and read the results.

#shell is the command-line interface of an Operating System 
#any program that can be launch from shell can also be launched from python 
#using a pipe object, which represents a running program. 

cmd = 'ls -l'
fp = os.popen(cmd)

#The argument is a string that contains a shell command. The return value is an object 
#that behaves like an open file. You can read the output from the ls process one line 
#at a time with readline or get the whole thing at once with read:

res = fp.read()

#When you are done, you close the pipe like a file:

stat = fp.close()
print(stat)

#Let's make an example

file = 'rd.csv'
cmd = 'md5sum' + file
fp = os.popen(cmd)
res = fp.read() 
stat = fp.close()
print(res)
print(stat)

#You can use md5sum to compute a "checksum" for each files. 
# If two files have the same chksum, they probably have the 
# same content. To doublecheck. Can use the unix command diff





