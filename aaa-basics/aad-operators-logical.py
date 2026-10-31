#python logical operators
#used to combine multiple boolean values
#typically combine the results of comparison operators
#these are keyword literals in python
"""
and  - all values must be true
or   - any one value must be true
not  - toggle the boolean value
"""
print("== Logical Operators ==")
print("and (all), or (any), not (exclude)")
req_price = 25
avl_price = 20
req_color = "blue"
avl_color = "blue"
print(f"comparing price avl_price <= req_price: {avl_price <= req_price}")
print(f"comparing color avl_color == req_color: {avl_color == req_color}")
cmp_price = avl_price <= req_price
cmp_color = avl_color == req_color
print(f"combining comparisons using 'and' cmp_price and cmp_color: {cmp_price and cmp_color}")
print(f"combining comparisons using 'or' cmp_price or cmp_color: {cmp_price or cmp_color}")
print(f"applying not on price comparison not cmp_price: {not cmp_price}")
print(f"applying not on color comparison not cmp_color: {not cmp_color}")



