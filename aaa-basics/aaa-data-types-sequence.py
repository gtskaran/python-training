#sequence (iterables) data types
#str - string
#list - list of objects
#tuple - list of immutable objects

mystr = 'Tamilnadu' #string - sequence of characters
mylist = [2,5,7,8,9,'an', '98', 73.55] #sequence of objects (mutable)
mytuple = (28, 39, 48, 47, 64) #sequence of objects (immutable)

#indexing and slicing
#mutable and immutable
#packing and unpacking

#len function
print()
print("== len - global function ==")
print("length of string", mystr, len(mystr))
print("length of list ", mylist, len(mylist))
print("length of tuple", mytuple, len(mytuple))

#indexing
print("== indexing - position of a value or object in a sequence ==")
print("value at position 0 in string is", mystr[0])
print("value at position 5 in string is", mystr[5])
print("value at position 1 in mylist is", mylist[1])
print("value at position 3 in mylist is", mylist[3])
print("value at position 0 in mytuple is", mytuple[0])
print("value at position 2 in mytuple is", mytuple[2])
print()
print("== negative indexing (right to left) ==")
print("value at position -1 in string is", mystr[-1])
print("value at position -6 in string is", mystr[-6])

#slicing
#[start:end:step]
print()
print("== slicing - returns a set of values ==")
print("Sliced string from 1 to 5 = ", mystr[1:6])
print("Sliced string from 1 to end with step 2 = ", mystr[1::2])
print("Reversed string using slicing", mystr, mystr[::-1])
print("Reversed tuple using slicing with step -2", mytuple, mytuple[::-2])

#mutable - changes to the values/items in the sequence are allowed
print()
print("List is mutable. Item 2 before change", mylist[2], mylist)
mylist[2] = 22
print("List is mutable. Item 2 after change", mylist[2], mylist)

#immutable - change to the values are NOT allowed
print()
print('String and Tuple are immutable.')
print('Before: tuple', mytuple, ' string', mystr)

#mytuple[2] = 22 #Error
#mystr[2] = 'CDM' #Error
#print('After: ???')

#packing - sequences can be packed with multiple values
print()
print('== Packing sequences ==')
newlist = [mystr, mytuple, mylist]
print('Packing: New list', newlist)
print()
print("== Unpacking - values in sequence are assigned to individual objects ==")
s, t, l = newlist
print("Unpacked:", "string", s, " tuple", t, " list", l)

