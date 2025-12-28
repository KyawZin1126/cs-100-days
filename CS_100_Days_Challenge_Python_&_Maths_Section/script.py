number = 1 # Integer
number2 = 2.0 # Float
name = "K Zin" # String
Country = "Myanmar"
flag = True # Boolean

datatype = type(flag)
print(datatype)

# Arithmetic
a = 17
b = 10

add = a + b
sub = a - b
mul = a * b
div = a / b
mod = a % b
quo = a // b
exp = a ** b

print(add)
print(sub)
print(mul)
print(div)
print(mod)
print(quo)
print(exp)

# Relational Operator / Comparison Operator
greater = a > b
less = a < b
greater_equal = a >= b
less_equal = a <= b
not_equal = a != b

print(greater)
print(less)
print(greater_equal)
print(less_equal)
print(not_equal)

# Logical Operator
status1 = True
status2 = False

and_ = status1 and status2
or_ = status1 or status2
not_ = not status1

print(and_)
print(or_)
print(not_)

# F-String
age = 24
print("I am {age} year old.")
print(f"I am {age} years old.")

# Conditional Statement
if a < b:
    print("a is greater than b")
    print("a is not less than b")
else:
    print("a is less than b")

print("This is the sentence.")

print("a is greater than b") if a > b else print("a is not greater than b") # Short_Hand

result = a if a > b else b
print(result)

if a == 1:
    print("a is 1")
elif a == 2:
    print("a is 2")
elif a == 3:
    print("a is 3")
else:
    print("a is other.")

# Looping

currentDay = 1
while currentDay<=100:
    print(f"CS 100 Days Challenge Day {currentDay}")
    currentDay += 1

index = 1
while index < 10: print(f"CS 10 Days Challenge Day {index}"); index += 1  # Short_Hand