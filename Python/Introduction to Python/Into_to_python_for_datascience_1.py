
# coding: utf-8

# In[1]:

def add_number(x,y,z=None,flag=True):
    if(flag==False):
        print('Flag is False')
    else:
        print('Flag is True')
        
    if(z==None):
        return x+y
    else:
        return x+y+z
    
print(add_number(1,2,flag=False))


# In[3]:

def add_number(x,y):
    return x+y

a= add_number
a(1,2)


# In[4]:

type('This is a string')


# In[5]:

type(add_number)


# In[7]:

#Tuples are an immutable data structure (cannot be altered).

x= (1,'a',2,'b')
type(x)


# In[8]:

#Lists are a mutable data structure.

x=[1,'a',2,'b']
type(x)


# In[9]:

#Use append to append an object to a list.

x.append(3.3)
print(x)


# In[10]:

# loop

for item in x:
    print(item)


# In[13]:

# loop using the indexing operator

i=0
while(i!=len(x)):
      print(x[i])
      i=i+1


# In[14]:

# Use + to concatenate lists.

[1,2]+[3.4,5.6]


# In[15]:

# Use * to repeat lists.

[1]*3


# In[16]:

# Use the in operator to check if something is inside a list.

1 in [1,2,3]


# In[23]:

# Now let's look at strings. Use bracket notation to slice a string.

x = 'This is string'
print(x[0])
print(x[0:3])
print(x[-1])
print(x[-3])
print(x[-4:-2])
print(x[:3])


# In[28]:

firstname = 'Ankur'
lastname = 'singh'

print(firstname+' '+lastname)
print(firstname*3)
print('Ankur' in firstname)


# In[31]:

# Split returns a list of all the words in a string, or a list split on a specific character.

firstname = 'Ankur Atul Nidhi'.split(' ')
lastname = 'Singh Kumar Rajput'.split(' ')

print(firstname)
print(lastname)


# In[32]:

# Make sure you convert objects to strings before concatenating.

'Ankur'+str(31)


# In[39]:

#Dictionaries associate keys with values.

x = {'Ankur':'ankur310794@gmail.com','Atul':'atul@gmail.com'}
print(x['Ankur'])

# Iterate over all of the keys:

for name in x:
    print(x[name])

# Iterate over all of the values:

for email in x.values():
    print(email)
    
# Iterate over all of the items in the list:

for name,email in x.items():
    print(name+':'+email)
    
    


# In[41]:

# You can unpack a sequence into different variables:

x = ('Ankur','ankur@gmail.com',str(310794))
name,email,eid=x
print(name+' '+email+' '+eid)


# In[42]:

# Python has a built in method for convenient string formatting.

sales_record = {
'price': 3.24,
'num_items': 4,
'person': 'Chris'}

sales_statement = '{} bought {} item(s) at a price of {} each for a total of {}'

print(sales_statement.format(sales_record['person'],
                            sales_record['num_items'],
                            sales_record['price'],
                            sales_record['num_items']*sales_record['price']))


# In[63]:

# Let's import our datafile mpg.csv, which contains fuel economy data for 234 cars.

import csv
get_ipython().magic(u'precision 2')

with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))

mpg[:3]


# In[64]:

# len shows that our list is comprised of 234 dictionaries

len(mpg)


# In[66]:

# find the average cty fuel economy across all cars

sum(float(d['cty']) for d in mpg) / len(mpg)


# In[67]:

# find the average hwy fuel economy across all cars.

sum(float(d['hwy']) for d in mpg)/len(mpg)


# In[69]:

# set to return the unique values for the number of cylinders the cars in our dataset have

cylinders = set(d['cyl'] for d in mpg)
cylinders


# In[72]:

# grouping the cars by number of cylinder, and finding the average cty mpg for each group.

CtyMpgByCyl = []

for c in cylinders:
    summpg = 0
    cyltypecount =0
    
    for d in mpg:
        if d['cyl']==c:
            summpg+= float(d['cty'])
            cyltypecount += 1
    CtyMpgByCyl.append((c,summpg/cyltypecount))
    
CtyMpgByCyl.sort(key=lambda x: x[0])
CtyMpgByCyl
            


# In[73]:

# Use set to return the unique values for the class types in our dataset.

vehicleclass = set(d['class'] for d in mpg)

vehicleclass


# In[74]:

# find the average hwy mpg for each class of vehicle in our dataset

HwyMpgByClass = []

for t in vehicleclass:
    summpg=0
    vclasscount=0
    
    for d in mpg:
        if d['class']==t:
            summpg+= float(d['hwy'])
            vclasscount+=1
    HwyMpgByClass.append((t,summpg/vclasscount))
    
HwyMpgByClass.sort(key=lambda x:x[1])

HwyMpgByClass


# In[75]:

import datetime as dt
import time as tm


# In[76]:

tm.time()


# In[77]:

# Convert the timestamp to datetime.

dtnow = dt.datetime.fromtimestamp(tm.time())
dtnow


# In[79]:

# Class 

class Person:
    dept = 'CSE'
    
    def set_name(self, new_name):
        self.name = new_name
    def set_location(self, new_location):
        self.location = new_location
        
person = Person()
person.set_name('Ankur')
person.set_location('GKP')

print('{} live in {} and works in {} department'.format(person.name,person.location,person.dept))


# In[84]:

store1 = [10.00,11.00,12.34,2.34]
store2 = [9.00,11.10,12.34,2.01]

cheapest = map(min,store1,store2)
cheapest


# In[85]:

for item in cheapest:
    print(item)


# In[96]:

# example of lambda that takes in three parameters and adds the first two

my_function = lambda a,b,c:a+b
my_function(1,2,3)


# In[98]:

# iterate from 0 to 999 and return the even numbers.

my_list = []
for number in range(0,100):
    if number%2==0:
        my_list.append(number)
        
my_list


# In[99]:

#  same thing but with list comprehension.

my_list = [number for number in range(0,100) if number%2==0]
my_list


# In[101]:

# The Python Programming Language: Numerical Python 

import numpy as np


# In[102]:

# Create a list and convert it to a numpy array

mylist = [1,2,3]
x = np.array(mylist)
x


# In[103]:

# Pass in a list of lists to create a multidimensional array.

m  = np.array([[1,2,3],[4,5,6]])
m


# In[105]:

# Use the shape method to find the dimensions of the array

m.shape


# In[106]:

# arange returns evenly spaced values within a given interval.

n = np.arange(0,30,2)
n


# In[107]:

# reshape returns an array with the same data with a new shape.

n = n.reshape(3,5)
n


# In[110]:

# linspace returns evenly spaced numbers over a specified interval.

o = np.linspace(0,5,9)
o


# In[111]:

# resize changes the shape and size of array in-place.

o.resize(3,3)
o


# In[114]:

# ones returns a new array of given shape and type, filled with ones.

np.ones((3,2))


# In[115]:

# zeros returns a new array of given shape and type, filled with zeros.

np.zeros((2,3))


# In[116]:

# eye returns a 2-D array with ones on the diagonal and zeros elsewhere.

np.eye(3)


# In[117]:

#diag extracts a diagonal or constructs a diagonal array.

y = [1,2,3]
np.diag(y)


# In[118]:

# Create an array using repeating list (or see np.tile)

np.array([1,2,3]*3)


# In[119]:

# Repeat elements of an array using repeat.

np.repeat([1,2,3],3)


# In[128]:

# Combining Arrays

p = np.ones([2,3],int)
p


# In[130]:

#Use vstack to stack arrays in sequence vertically (row wise).

x = np.vstack([p,2*p])
x


# In[131]:

# Use hstack to stack arrays in sequence horizontally (column wise).

y = np.hstack([p,2*p])
y


# In[153]:

# Use +, -, *, / and ** to perform element wise addition, subtraction, multiplication, division and power.

x = np.array([1,2,3])
y = np.array([4,5,6])

print(x + y)
print(x - y)
print(x * y)
print(x / y)

print('dot product:')
print(x.dot(y))

print(x**2)

z = np.array([x,y])
z.T


# In[156]:

# Math Functions
# Numpy has many built in math functions that can be performed on arrays

a = np.array([-4, -2, 1, 3, 5])

print(a.sum())
print(a.min())
print(a.max())
print(a.mean())
print(a.std())
print(a.argmax())
print(a.argmin())


# In[ ]:

# Indexing / Slicing


