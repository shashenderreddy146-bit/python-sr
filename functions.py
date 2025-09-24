# functions:
# syntax:
# def funcyion_name(parameters):
#     # functional body code
#     return value  #optional
# function_name()
# example:
# def greet():
#     print("hello world")


# callinga function:
# def greet():
#     print("hello world")
# greet()     #calling a function

# def greet(name,branch):
#     print("helllo world",name,branch)
# greet("Shashi","CSM AI&ML")


# passing parameters and arguments:
# example:
# def greet(name,rollno):
#     print("hello",name,"your rollno is",rollno)
# greet("Shashi","G1")

# name=input("enter your name: ")
# print("hello",name)

# types of functions arguments:

# 1. positional arguyments:
# def greet(rollno,name):
#     print("hello",name,"your rollno is",rollno)
# greet("G1","shashi")

# 2. keyword arguments:
# def greet(rollno,name):
#     print("hello",name,"your rollno is",rollno)
# greet(name="shashi",rollno="G1")


# 3. default argument:
# def greet(name="student"):
#     print("hello",name)
# greet()
# greet("shashi")

# 4. variable-length arguments:
# def sum1(*list1):
#     sum2 = 0
#     for i in range(len(list1)):
#         sum2 = sum2 + list[i]
#     print(sum2)
#     print(type(list1))
# sum1(10,20,30,40,50)


# **kwargs:
# def details(**info):
#     for i,j in info.items():
#         print(i,":",j)
# details(name="shashi",rollno="G1",branch="CSM")


# scope of the variable:
# x=10
# def var1():
#     y=5
#     print("inside var1 function",x,y)
# var1()
#     print("inside var2 function",x,y)
# var2()

# print("outside function",x,y)         #errorr


# lambda function:
# def sqe(a):
#     print(a*a)
# sqe(5)
# # lambda function:
# squ=lambda x:x*x
# print(squ(99))

# factorial:
def factorial(n):
    fact=1
    for i in range(n,0,-1):
        fact=fact*i
    print(fact)
factorial(5)
factorial(4)

# recursive:
def rfactorial(n):
    if n==0:
    else:
        return n * rfactorial(n-1)
rfactorial(5)

def greet():
    print+("hello")
    return greet()
greet()