"""
A Lambda Function in Python programming is an anonymous function 
or a function having no name. 

Systax: lambda <variable list>:expression
"""
from math import pi

print(lambda x, y: x + y)

def pf2f(f, x, y):
    return f(x, y)

t1 = (1,2,3,4,5)
t2 = (11,12,13,14,15)

list1 = [lambda x: 3*x*x + 5*x - 3 for x in t1]
print(list1)
# list1 = [x + y for x in t1 for y in t2]
# print(list1)

# f1 = lambda x, y: 3*x*x + 2* y
# list1 = [pf2f(f1, x, y) for x in t1 for y in t2]
# print(list1)

# f1 = lambda x,y:x+y
list2 = list(map(lambda x,y:x+y, t1, t2))
print(list2)
# t3 = tuple(map(lambda x,y: x+y, t1, t2))
# print(t3)

# t4 = tuple(filter(lambda x:x%2==1, t1))
# print(t4)

# area = lambda r: r**2 * pi # assign a function name area to lambda expression
# print(area(1))

# def circle_area(r):
#     return r * r * pi

# print(circle_area(1))

# # make complicated lambda expression possible
# a = lambda r: circle_area(r) # use existing function to define a lambda expression
# print(a(1))
# print(a(-2))


# area = lambda r: r**2 * pi  # anonymous function, lambda expression

# x = lambda y: y * y  # x is a function name

# for i in range(5):
#     print(x(i))

# def foo (f, x): # pass function to function
#     return f(x)

# for i in range(5):
#     print(foo(lambda x: x * x, i)) # pass lambda expression as a function

# for i in range(5):
#     print(foo(lambda x: x * x * x, i)) 

# # calculate circle area
# for i in range(5):
#     print(foo(a, i))

def add(n):
    return n + 10

f = lambda: add(5) # provide value at function define
print(f()) # run the function later, refer to 