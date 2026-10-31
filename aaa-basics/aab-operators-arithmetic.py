#Python Operators
#arithmetic operators
print(
'''
+  addition
-  subtraction
*  multiplication
/  division
%  modulus
** exponent
// floor division
'''
)

val1 = 245
val2 = 7

print("Addition",val1, "+", val2, val1 + val2)
print("Subtraction",val1, "-", val2, val1 - val2)
print("Multiplication",val1, "*", val2, val1 * val2)
print("Division",val1, "/", val2, val1 / val2)
print("Modulo",val1, "%", val2, val1 % val2)
print("Exponent",val1, "**", val2, val1 ** val2)
print("Floor division",val1, "//", val2, val1 // val2)

#BODMAS (Brackets, Order of (power of), Division, Multiplication, Addition, Subtraction)

#bin, oct, hex - decimal conversion functions
print('Binary of ', val1, '=', bin(val1))
print('Octal of ', val1, '=', oct(val1))
print('Hexadecimal of ', val1, '=', hex(val1))

print()
print("==Escape Characters==")
#\t tab
#\n new line
#\b backspace
print("\t \n \b \" \\ ")

print()
print("==Character Conversion==")
#ascii
#chr, ord
print('chr function', chr(80), chr(97), chr(118), chr(121), chr(97))
print('ord (ordinal) function', ord('P'), ord('a'), ord('v'), ord('y'), ord('a'))

print()
print("== 10's with numbers ==")
print(val1, ' multiply by 10', val1 * 10)
print(val1, ' divided by 10', val1 / 10)
print(val1, ' modulus by 10', val1 % 10)
print(val1, ' exponent by 10', val1 ** 10)
print(val1, ' floor divide by 10', val1 // 10)

