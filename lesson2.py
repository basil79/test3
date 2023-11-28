

name = "Basil"
age = 42
wife_name = "Anna"

# comma seperator, no need spaces
print("My name is", name, "and years", age, "and my wife name is", wife_name)

# format
print(f"{name}")
# format
print("Hello my age is {}, and name is {}".format(age, name))



# tuple
# Кортежи и последовательности
t = 12345, 54321, 'hello!'
z = (1,2,3,4,5)
print(t)
print(z)

y = t, z
print(y)

for v in t:
    print(v)
