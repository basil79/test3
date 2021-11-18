


# f = open('workfile', 'w')


#with open('workfile') as f:
# read_data = f.read()
#f.closed



# f.read()
# f.readline()

#for line in f:
#print(line, end='')


#f.write('This is a test\n')


#import json
#json.dumps([1, 'simple', 'list'])
#'[1, "simple", "list"]'


# json serialization to file
# json.dump(x, f)

# To decode the object again, if f is a text file object which has been opened for reading:
#x = json.load(f)


# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# 'r' - open for reading (default)
# 'w' - open for writing, truncating the file first
# 'x' - open for exclusive creation, failing if the file already exists
# 'a' - open for writing, appending to the end of the file if it exists
# 'b' - binary mode
# 't' -text mode (default)
# '+' - open a disk file for updating (reading and writing)



with open('data.csv') as f:
    read_data = f.read()
    print(read_data)

