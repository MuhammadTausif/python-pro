# 1. Basic Assignments and Naming

# 1.1 Create a variable named python_version and assign the version of Python you're using as a string. Print it.

import sys
python_version = sys.version
print("Python version on my computer:- ", python_version)

# 1.2 Try creating a variable starting with a number, like 3_variable. Observe the error you get. Write down why this error occurred.
# 3_variable = 12

'''
    3_variable = 12
     ^
SyntaxError: invalid decimal literal
'''

# 1.3 Assign two variables in a single line: x to 10 and y to 20. Print both.

x, y, z, s, n = 10, 20, 35, "This is String", [23,12, "Aslam"]

print("x: ", x , ", y: ", y, ", z: ", z, "s: ", s, "n is list: ", n)

x = 10
y = 20
z = 40

x, y, z, n = 10, 20, 40, "This is forth value"

# 2. Swapping and Multiple Assignments

# 2.1 Given a=5 and b=10, swap the values without using a third variable.
a, b = 5, 10

print("Swapping using third variable")
print("Before swapping: a: ", a, ", b: ", b)
c = a
a = b
b = c
print("After swapping: a: ", a, ", b: ", b)

print('____________________________________________\n')
print("Swapping withoug using third variable")
print("Before swapping: a: ", a, ", b: ", b)
a, b = b, a
print("After swapping: a: ", a, ", b: ", b)

# 2.2 Assign three variables, i, j, and k, in a single line the values 5.5, Hello, and 7 respectively.

float_string = "12.45"
float_act = float(float_string)
int_act = int(float_act)

s = "abc"

S = s.upper()

print(S)

print(id(S))
