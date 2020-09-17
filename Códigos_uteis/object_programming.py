#Example of Class implementation and manipulation 

class Time:
    '''
    class with hour, time and second attribuites
    '''

time = Time()
time.hour = 10
time.minute = 30
time.second = 35

type(time)

def print_time(t):
    print('%.2d:%.2d:%.2d' % (t.hour,t.minute,t.second))

print_time(time)

def is_after(t1,t2):
    int1 = t1.hour * 60 + t1.minute
    int2 = t2.hour * 60 + t2.minute
    return int2 > int1
     

t1 = Time()        
t1.hour = 12
t1.minute = 20
t1.second = 35

t2 = Time()
t2.hour = 13
t2.minute = 30
t2.second = 35

is_after(t1,t2)

def add_time(t1,t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    return sum 

add_time(t1,t2)


start = Time()
start.hour = 9
start.minute = 45
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

done = add_time(start,duration)
print_time(done)

#We tested and the funciont did not deal well when minutes surpass 60
#so, we created a add_time2 version, see below 

def add_time2(t1,t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.second -=60
        sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum         

done2 = add_time2(start,duration)
print_time(done2)


#Example of Modifier

#this function takes a time object and amount of seconds as parameters and adds the 
#seconds to the  time object

def increment(time,seconds):
    time.second += seconds
    
    if time.second >= 60: 
        time.second -=60
        time.minute += 1

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1

print_time(t2)

increment(t2,60)

#The increment function modifies the time parameter received, 
#write a 'pure' version that create a new object

import copy 

def increment_pure(time,seconds):
    time2 = copy.deepcopy(time)
    time2.second += seconds
    
    while time2.second >= 60: 
        time2.second -=60
        time2.minute += 1

    while time2.minute >= 60:
        time2.minute -= 60
        time2.hour += 1

    return print_time(time2)

print_time(t1)

increment_pure(t1,60)


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds,60)
    time.hour, time.minute = divmod(minutes,60)
    return time 

#Simple example of consistency check:

x = 1000

time_to_int(int_to_time(x)) == x


def add_time2(t1,t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)
    
#Code to check invariant. It stands for situations which must always be true 
#in this time example, a Time object needs to have positive hours, minutes and seconds 
#and values lower than 60. Since 60 minutes is equals to 1 hour 


def valid_time(t):
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60:
        return False
    return True

#This function can be used to validate time entry before operation in other functions 

def add_time2(t1,t2):
    if not valid_time(t1) or not valid_time(t2):
        raise ValueError('Invalid Time object in add_tim2 function')
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


#Or an assert statement can be used, which checks a given invariant and raises and exception if it fails

def add_time2(t1,t2):
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


from datetime import date
x = date.today()
x

def print_day_week(date):
    wk_day = date.weekday()
    week = {'0':'Monday',
            '1':'Tuesday',
            '2':'Wednesday',
            '3':'Thursday',
            '4':'Friday',
            '5':'Saturday',
            '6':'Sunday'}
    for day in week:
        if day == str(wk_day):
            print(week[day]) 

print_day_week(x)    

#Method is a function associated with a particular class

#Previously, we have created a Class named Time and created a function
#called print_time. We will transform the function into a method. 

#All we have to do, is to assign the function in the class definition, as bellow

#By convention, the first parameter of a method is called self, 
#so it would be more common to write print_time like this:

#rewriting is_after as method inside a class object is a bit more complicated
#it takes two Time object as paramter, the firs is likewise called self, the second is called other


class Time:
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour,self.minute,self.second))

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds    

    def increment(self,seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self,other):
        return self.time_to_int() > other.time_to_int()

    def __init__(self,hour=0,minute=0,second=0):
        self.hour = hour
        self.minute = minute
        self.second = second 


#I created a Time object called time, at the begining of this file

Time.print_time(time)

#This notation bellow is most common 

time.print_time()


#The reason for this convention is an implicit metaphor:

# The syntax for a function call, print_time(start), suggests that the function is the active agent. 
# It says something like, “Hey print_time! Here’s an object for you to print.”

# In object-oriented programming, the objects are the active agents. A method invoca- tion like 
# start.print_time() says “Hey start! Please print yourself.”


#When you write a method you don't need to pass the class object as an argument
#look up to the function 'increment' and compare to bellow verson writen as a method

time.print_time()

end = time.increment(60)
end.print_time()

#Implementing is_after function as a class method for two objects
#Invoke one and pass the other as argument

t2.is_after(t1)

#The __init__ method (short for “initialization”) is a special method that 
#gets invoked when an object is instantiated. See in the class definition 

x = Time()
x.print_time()

#One argument override the first parameter 
x = Time(9)
x.print_time()

#Two arguments override the first and second parameter, and so on until reach the standard 
#assigned in the statiation

x = Time(9,40)
x.print_time()

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y 

    def print_point(self):
        print('Ponto X:',self.x)
        print('Ponto Y:',self.y)
    

a = Point(2,2)

a.print_point()


#__str__ is a special method, like __init__, that is supposed 
#to return a string representation of an object.

class Time2:
    def __init__(self,hour=0,minute=0,second=0,milisecond=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.milisecond = milisecond

    def __str__(self):
        return '%.2d:%.2d:%.2d:%.3d' % (self.hour,self.minute,self.second,self.milisecond)

        

x = Time2(2,30,40,340)

#Note as having the __str__ method. We can print the class instatiation directly from print function
print(x)

class Point2:
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y 
        self.z = z

    def __str__(self):
       return '%.1d - %.1d - %.1d' % (self.x,self.y,self.z)

p = Point2(2,4,6)

print(p)

#We can make a __add__ function and sum instatiations 
#the add method replace the + operator
#for each operator there is a specific methos that can be applied 
#see documentation for more info 

#this is the pure version of __add__:
'''
def __add__(self,other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
'''

#below We defined again the class Time, being called as Time3
#we modified _add__ function, so it can validate the entry of the object for adding 

#there is an implementation of __radd__ method. It check the right side of the object instantiated
#the increment method were configured to firstly take a time obj and add an integer
#If you try the opposite, adding a time to an integer, you would get an error
#this can be solved using special method __radd__ which invert the order if necessary

class Time3:
    def __init__(self,hour=0,minute=0,second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour,self.minute,self.second)

    def __add__(self,other):
        if isinstance(other,Time3):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self,other):
        return self.__add__(other)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def increment(self,seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def add_time(self,other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def is_after(self,other):
        return self.time_to_int() > other.time_to_int()
                    
def int_to_time(seconds):
    time = Time3()
    minute,time.second = divmod(seconds,60)
    time.hour,time.minute = divmod(minute,60)
    return time 

start = Time3(1,20,30)
duration = Time3(1)
break_time = 30

print(start)
print(duration)

print(start + duration)

print(start + break_time)

print(start + 120)
print(120 + duration)

#Vars is a function that returns a class attributes in dict format 
#mapping its atrb names to their values. 
vars(start)

def print_attr(obj):
    for attr in vars(obj):
        print(attr,getattr(obj,attr))


print_attr(duration)







