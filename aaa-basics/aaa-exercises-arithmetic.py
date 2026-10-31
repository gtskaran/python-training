#swapping two numbers
print("== swapping two numbers ==")
val1 = 222
val2 = 333
print('Before swapping val1=', val1, ' , val2 =', val2)
val1 = val1 + val2
val2 = val1 - val2
val1 = val1 - val2
print('After swapping val1=', val1, ' , val2 =', val2)
print("== using temporary variable ==")
print('Before swapping val1=', val1, ' , val2 =', val2)
temp = val1
val1 = val2
val2 = temp
print('After swapping val1=', val1, ' , val2 =', val2)

print("== multiple assignment ==")
a, b, c = 55, 24, 78
print(f'before swapping a={a}, b={b}, c={c}')
a, b, c = c, a, b
print(f'after swapping a={a}, b={b}, c={c}')

#area of circle
print()
print("== calculate area of circle ==")
"""
carea = pi * radius * radius
carea - ouput variable - float
pi - input constant - float
radius - input variable - float
"""

pi = 3.1415
radius = 12
carea = pi * radius ** 2
print(f'Area of circle with radius "{radius:^10}" is {carea:10.2f}')
#formatted string, required format given aftet :, < left align, ^ center, > right
