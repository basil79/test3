
# Python 3

x = 1
y = 3


print(x+y)


tax = 12.5 / 100
price = 100.50
total = price * tax

print(total)


print(f"Total is: {total}")


print("Total is {}".format(total))



def foo(x, y = 9):
    return x + y

print(foo(5))

print(foo(5,8))

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b =  b, a + b
    print()

fib(1000)


a = [1, 2, 3, 4]

# for loop on a list
for b in a:
    print(b, end=' ')
print()



# for loop on a list
numbers = [2, 4, 6, 8]
product = 1
for number in numbers:
    print(number)
    product = product * number

print('The product is:', product)



# Python 3: List comprehensions
fruits = ['Banana', 'Apple', 'Lime']
for fruit in fruits:
    print(fruit)

loud_fruits = [fruit.upper() for fruit in fruits]
print(loud_fruits)

# list and the enumerate function
print(list(enumerate(fruits)))




print("Hello, I'm Python!")

# input, assignment
name = input('What is your name?\n')

print('Hi, %s.' % name) # %s formatter

print("Hi, {}.".format(name))

print("Hi,", name)

print("Hi, " + name + ".")



# Python 3: Simple arithmetic
print(1 / 2)
print(2 * 3)
print(2 ** 3)
print(17 / 3) # classic division returns a float
print(17 // 3) # floor division


# input -> int() return an Integer value from Number or String, if no arguments was given return 0
x = int(input("Please enter an integer: "))

# if statement
if x < 0:
    x = 0
    print('Negative change to zero')
# else if in Python -> elif
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('None')

print('Value of x was:', x)




# for Statement
words = ['cat', 'window', 'defenestrate']
for word in words:
    print(word, len(word))

# Loop over a slice copy of the entire list.
for word in words[:]:
    if len(word) > 6:
        words.insert(0, word)

print(words)


# range function

for i in range(5):
    print(i)
    # print(i, end=' ')


my_range = range(5, 10) # starts from 5 until 10 -> 10 not include
for r in my_range:
    print(r)


a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])


print(range(10))

# list it creates lists from iterables:
print(list(range(5)))




for n in range(2, 10):  # 2, 3, 4, 5, 6, 7, 8, 9
    print(n)

# break and continue Statements, and else Clauses on Loops
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')



for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)






# Defining Functions
# keyword def introduces a function definition
def foo1():
    return "Hello World!!!"


print(foo1())



def foo2(a, l=[]):
    l.append(a)
    return l

print(foo2(1))
print(foo2(2))
print(foo2(3))



def foo3(a, l=None):
    if l is None:
        l = []
    l.append(a)
    return l

print(foo3(1))
print(foo3(2))
print(foo3(3))





# Keyword Arguments
def foo4(a, b = 3, c = 4, d = 10):
    return a + b + c + d


print(foo4(1))
print(foo4(a=1))
print(foo4(1, c=5))


# function with N arguments

def foo5(kind, *args):
    print(kind)
    for arg in args:
        print(arg)


foo5('Basil', 'Germany', 'Frankfurt', 'Munich')


# function with args + keywords
def foo6(kind, *args, **keywords):
    print(kind)
    for arg in args:
        print(arg)

    print('-' * 40)

    for keyword in keywords:
        print(keyword, ":", keywords[keyword])


foo6('Basil', 'Germany', 'Frankfurt', 'Munich', client='John Cleese', phone='004935442555')



# Arbitrary Argument Lists
def foo7(seperator, *args):
    return seperator.join(args)


print(foo7('/', 'earth', 'mars', 'venus'))





# Name your classes and functions consistently; the convention is to use UpperCamelCase for classes
# and lowercase_with_underscores for functions and methods


# strings

s = '"Isn\'t," they said.'
print(s)



s2 = 'Hello World!!!'

print(s2)
print(s2[0:2])
print(s2[:2])
print(s2[2:4])
print(s2[2:])
print(s2[-2:])

# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
#-6  -5  -4  -3  -2  -1


print(len(s2))



# lists

squares = [1, 4, 9, 16, 25]
print(squares)

print(squares[0])
print(squares[-1])
print(squares[-3:]) # do slicing and returns a new list

# list also support operations like concatenation

con = squares + [36, 49, 64, 81, 100]

print(con)


cubes = [1, 8, 27, 65, 125] # something's wrong here
print(cubes)

fix = 4 ** 3 # the cube of 4 is 64, not 65!
cubes[3] = fix
print(cubes)

cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7

print(cubes)



# letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

# replace some values
letters[2:5] = ['j', 'k', 'z']
print(letters)

# now remove them
letters[2:5] = []
print(letters)

# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)
print(len(letters))


# It is possible to nest lists (create lists containing other lists), for example:
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)



table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(name, phone)




