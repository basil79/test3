







class A:
    i = 12345
    def foo(self):
        return 'Hello world!!!'


a = A()

print(a.foo())
print(a.i)



class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i


x = Complex(3.0, -4.5)
print(x.r)
print(x.i)



class Dog:
    kind = 'canine' # class variable shared by all instances

    def __init__(self, name):
        self.name = name # instance variable unique to each instance


d = Dog('Fido')
print(d.name)
print(d.kind)

e = Dog('Punch')
print(e.name)


class Cat:
    tricks = [] # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


c = Cat('Mura')
print(c.name)

c.add_trick('roll over')
print(c.tricks)

f = Cat('Buddy')
print(f.name)

print(f.tricks)

f.add_trick('play dead')

print(c.tricks)



class D:

    def __init__(self, name):
        self.name = name
        self.tricks = [] # creates a new empty list for each d

    def add_trick(self, trick):
        self.tricks.append(trick)

s = D('Test 1')

print(s.name)

s.add_trick('roll over')

print(s.tricks)


w = D('Test 2')
print(w.name)

w.add_trick('play dead')

print(w.tricks)




# Random Remark

# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class F:
    f = f1
    def g(self):
        return 'hello world'
    h = g

f2 = F()
print(f2.f(1, 2))
print(f2.h())




# Classes Inheritance and Multi Inheritance


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update # private copy of original update() method


class MappingSubClass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

mp = MappingSubClass({ 'one' : 1, 'two': 2})
print(mp.items_list)
mp.update(['tree', 'four'], [5,7])
print(mp.items_list)




# Odds and Ends

class Employee:
    pass

empl = Employee()
empl.name = 'John Doe'
empl.dept = 'computer lab'
empl.salary = 1000

print(empl.name)



# Iterators
for element in [1, 2, 3]:
    print(element)

for element in (1, 2, 3):
    print(element)

for key in {'one':1, 'two':2}:
    print(key)

for char in "123":
    print(char)


# for behind the scenes calls iter() on the container object, the function return iterator object that define the method __next__()
s = 'abc'
it = iter(s)

print(it)

print(next(it))
print(next(it))
print(next(it))


# Generator Expressions
ab = sum(i*i for i in range(10)) # sum of squares
print(ab)

xvec = [10, 20, 30]
yvec = [7, 5, 3]

abc = sum(x*y for x,y in zip(xvec, yvec))
print(abc)






squares = [1, 4, 9, 16, 25]
con = squares + [36, 49, 64, 81, 100]

print(con)




list = ['larry', 'curly', 'moe']
list.append('shemp')         ## append elem at end
list.insert(0, 'xxx')        ## insert elem at index 0
list.extend(['yyy', 'zzz'])  ## add list of elems at end
print(list)  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print(list.index('curly'))    ## 2

list.remove('curly')         ## search and remove that element
list.pop(1)                  ## removes and returns 'larry'
print(list)





# list build up

list1 = []          ## Start as the empty list
list1.append('a')   ## Use append() to add elements
list1.append('b')
print(list1)



# list slices

list2 = ['a', 'b', 'c', 'd']
print(list2[1:-1])   ## ['b', 'c']
list2[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
print(list2)         ## ['z', 'c', 'd']





# Python Sorting

list3 = [5, 1, 4, 3]
print(sorted(list3))  ## [1, 3, 4, 5]
print(list3)  ## [5, 1, 4, 3]


strs = ['aa', 'BB', 'zz', 'CC']
print(sorted(strs))  ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
print(sorted(strs, reverse=True))  ## ['zz', 'aa', 'CC', 'BB']



# custom sorting with key=

strs2 = ['ccc', 'aaaa', 'd', 'bb']
print(sorted(strs2, key=len))  ## ['d', 'bb', 'ccc', 'aaaa']

# "key" argument specifying str.lower function to use for sorting
print(sorted(strs2, key=str.lower))  ## ['aa', 'BB', 'CC', 'zz']


# own sort
# Say we have a list of strings we want to sort by the last letter of the string.
strs3 = ['xc', 'zb', 'yd', 'wa']

## Write a little function that takes a string, and returns its last letter.
## This will be the key function (takes in 1 value, returns 1 value).
def my_sort(s):
    return s[-1]

## Now pass key=my_sort to sorted() to sort by the last letter:
print(sorted(strs3, key=my_sort))  ## ['wa', 'zb', 'xc', 'yd']




# Tuples
# A tuple is a fixed size grouping of elements, such as an (x, y) co-ordinate

tuple = (1, 2, 'hi')
print(len(tuple))
print(tuple[2])
#tuple[2] = 'bye'  ## NO, tuples cannot be changed
tuple = (1, 2, 'bye')  ## this works
print(tuple)

# To create a size-1 tuple, the lone element must be followed by a comma.
tuple = ('hi',)   ## size-1 tuple
print(tuple)




# List Comprehensions (optional)
# The syntax is [ expr for var in list ] -- the for var in list looks like a regular for-loop, but without the colon (:).
# The expr to its left is evaluated once for each element to give the values for the new list.
# Here is an example with strings, where each string is changed to upper case with '!!!' appended:
nums = [1, 2, 3, 4]
squares5 = [ n * n for n in nums ]
print(squares5)



strs9 = ['hello', 'and', 'goodbye']
shouting = [ s.upper() + '!!!' for s in strs9 ]
print(shouting)


## Select values <= 2
nums2 = [2, 8, 1, 6]
small = [ n for n in nums2 if n <= 2 ]  ## [2, 1]
print(small)


## Select fruits containing 'a', change to upper case
fruits = ['apple', 'cherry', 'banana', 'lemon']
afruits = [ s.upper() for s in fruits if 'a' in s ]
print(afruits)





# Strings
# s.lower(), s.upper() -- returns the lowercase or uppercase version of the string
# s.strip() -- returns a string with whitespace removed from the start and end
# s.isalpha()/s.isdigit()/s.isspace()... -- tests if all the string chars are in the various character classes
# s.startswith('other'), s.endswith('other') -- tests if the string starts or ends with the given other string
# s.find('other') -- searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found
# s.replace('old', 'new') -- returns a string where all occurrences of 'old' have been replaced by 'new'
# s.split('delim') -- returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special case s.split() (with no arguments) splits on all whitespace chars.
# s.join(list) -- opposite of split(), joins the elements in the given list together using the string as the delimiter. e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc

s5 = 'a'
print(s5.upper())

s6 = 'hello world'
print(s6.replace('hello', 'welcome'))



# IF statement
# Any value can be used as an if-test. The "zero" values all count as false: None, 0, empty string, empty list, empty dictionary.
# There is also a Boolean type with two values: True and False (converted to an int, these are 1 and 0).
# Python has the usual comparison operations: ==, !=, <, <=, >, >=. Unlike Java and C, == is overloaded to work correctly with strings.
# The boolean operators are the spelled out words *and*, *or*, *not* (Python does not use the C-style && || !).
# Here's what the code might look like for a policeman pulling over a speeder
# -- notice how each block of then/else statements starts with a : and the statements are grouped by their indentation:



def write_ticket():
    print("You have a ticket")


mood = 'terrible'
speed =100
if speed >= 80:
    print('License and registration please')
    if mood == 'terrible' or speed >= 100:
      print('You have the right to remain silent.')
    elif mood == 'bad' or speed >= 90:
      print("I'm going to have to write you a ticket.")
      write_ticket()
    else:
      print("Let's try to keep it under 80 ok?")



if speed >= 80:
    print('You are so busted')
else:
    print('Have a nice day')


g1 = 200
g2 = 100
g3 = 150

if g1 > g2 and g3 < g1:
    print('Correct')