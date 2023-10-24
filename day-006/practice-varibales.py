# Python variable types: int(integer), float, str (string), list
# type: returns the type of any instance/veraibles
# len: returns the length of list, dict, str


x = "I am learning Python"
print(x)

print("type of x: ", type(x))

y = 12
print("type of y: ", type(y))

z = 10.0
print("type of z: ", type(z))

a = list([1,2,3,4])
print(a)
print("type of a: ", type(a))

b = [1,2,3,4]
print(b, ", type of b: ", type(b))

c = ['math', 'pythics', 'chemistery']
print(c)

d = [1, 'math', 5,  'pythics', 'chemistery', 10.5]
print(d)

print(d[3])

print(d[len(d)- 1])

print("length of list d: ", len(d))

print(x, ", Lenght of string 'x': ", len(x))

