# zerodivision error:
# try:
#     a=int(input("enter the numerator: "))
#     b=int(input("enter the denominator: "))
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print("Error: division by zero is not possible")


# valueError:
# try:
#     rollno=int(input("enter your rollno: "))
# except ValueError:
#     print("given value is not a integer datatype")


# indexError:
# try:
#     list=[1,2,3,4]
#     print(list[5])
# except IndexError:
#     print("given value is not a list")

# # keyEError:
# try:
#     dict={
#         "name":"shashi",
#         "rollno":"G1",
#         "name1":"shashi"
# }
#     print(dict["branch"])
# except KeyError:
#     print("given value is not in dict")

# typeError:
# try:
#     sum="3"+4
#     print(sum)
# except TypeError:
#     print("invalid type operation")

# nameerror:
# try:
#     print(Mult)
# except TypeError:
#     print("variable not decalared")

# filenotfounderror:
try:
    file=open("dertail.txt","r")
    print(file.read())
except FileNotFoundError:
    print("file is not in the system.")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
finally:
    print("program is exicuted")