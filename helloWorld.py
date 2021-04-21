# to print in terminal, command: py nameOfFile.py
#python uses lowercase only, no camelCase

#to print
print("this will be printed")

# four spaces is one indent, which is equivalent to {} in JS
x = 1
if x == 1: 
    print("x is", x)

#floats can be defined in one of two ways:
myfloat = 7.3
print(myfloat)
myfloat = float(7)
print(myfloat)

#strings can be defined by single or double quotation marks; double quotations allow you to use single quotation marks within the string
mystring = 'hello'
print(mystring)
mynewstring = "hello won't do"
print(mynewstring)

#lists are similar to arrays; can contain any type and number of variables
mylist = []
#use .append to add to an existing list
mylist.append(1)
mylist.append(2)
mylist.append(4)

#for loop utililzing lists
for x in mylist:
    if x == 2:
        print(x)
    else:
        print("nope")

#list data is accessed via index, exactly like arrays:
print(mylist[0])