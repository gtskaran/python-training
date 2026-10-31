#data types
#Every data type in python is object and dynamic
#variable name - contains Captial and Small alphabets, numbers and _ and not start with number

#declaration - creating a variable
#initialization - value assigned during creation
#assignment - value assigned during execution of code

print("===numeric data types===")
print("===integer (int) - Whole numbers===")
i = int()
n = 123
print(type(i), i)
print(type(n), n)

print("===fractional numbers (float) - decimal numbers===")
f = float()
fn = 23.57
print(type(f), f)
print(type(fn), fn)

print("===complex number (complex)===")
c = complex()
cn = 4 + 2j
print(type(c), c)
print(type(cn), cn)

print("===sequence type (series of values)===")
#mutable, immutable
#indexing, slicing
#packing, unpacking
#iterator, iterable
print("===string (str) - word, name===")
s = str()
mystr = 'Welcome'
print(type(s), s)
print(type(mystr), mystr)

print("===list===")
mylist1 = list()
mylist2 = []
mylist3 = [23, 'ab', 8, 0, 2.5]
print(type(mylist1), mylist1)
print(type(mylist2), mylist2)
print(type(mylist3), mylist3)

print("===tuple===")
mytup1 = tuple()
mytup2 = ()
mytup3 = 1,2,3,6,7
mytup4 = (23,45,76)
print(type(mytup1), mytup1)
print(type(mytup2), mytup2)
print(type(mytup3), mytup3)
print(type(mytup4), mytup4)

print()
print("===Mapping Type===")
print("===dictionary (dict) - key : value pair ===")
mydict1 = {}
mydict2 = dict()
mydict3 = {'key':'value', 4:'Mylapore', 17:'T.Nagar', 'goal': 89}
print(type(mydict1), mydict1)
print(type(mydict3), mydict3)

print()
print("=== Other Types ===")
print("=== sets (set) - contain unique values ===")
myset1 = set()
myset2 = {1,4,8,3,5}
print(type(myset1), myset1)
print(type(myset2), myset2)

print()
print("=== boolean (bool) - hold True or False === ")
mystat = bool()
mystat1 = True
mystat2 = False
mystat3 = 0
mystat4 = -23
mystat5 = 'Hello'
mystat6 = ''
mystat7 = None
print(type(mystat), mystat)
print(type(mystat1), mystat1)
print(type(mystat2), mystat2)
print(type(mystat3), mystat3)
print(type(mystat4), mystat4)
print(type(mystat5), mystat5)
print(type(mystat6), mystat6, bool(mystat6))
print(type(mystat7), mystat7, bool(mystat7))

print()
print("=== bytes and bytearray (data is in binary format) ===")
mybytes = b'hello world'
print(type(mybytes), mybytes)

print()
print("=== range(start, stop, step)  - generates a range of numbers ===")
myrange = range(12)
print(type(myrange), myrange, [*myrange])
myrange = range(2, 9)
print(type(myrange), myrange, [*myrange])
myrange = range(2, 21, 2)
print(type(myrange), myrange, [*myrange])
