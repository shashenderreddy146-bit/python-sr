#collection data types
# fruits=["apple","guava","mango","grapes","pineapple","banana"]
# list1=[1,2,3,4,5]
# list2=[10,1,20,2,30,3,40,4,50,5]
# list3=[True,False,False,True]
# list4=[10,20.8,"hello",True,"False"]
# output
# print(list4)
# list=(3,4,5,6,7,8,9,7,6)
# print(list[5])
# list=(20,30,50,70,110,130,170)
# print(list[1:3])
# print(list[2:6])
# print(list[1:5])
# print(list[0:3])
# print(list[5:6])

# list1=("Bat","Cat","Dog","Egg","Frog","Green")
# list1.append("Hat")
# list1.insert(3,"Sun")
# list1.extend(["bmw","fortuner","thar"])
# print(list1)

# a=(1,2)
# b=(3,4)
# c=a+b
# print(c)

# a = ["i love u"]
# n = int(input("enter the n value:"))
# b = a*n
# print(b)

# a = ["salaar devaratha raisar"]
# n = int(input("enter the n value"))
# b = a*n
# print(b)

#searching and checking:
# a=[1,3,5,7,9,11,13,15]
# if 1 in a:
#     print("yes item is present in the list ")
#not in operator
# print(2 not in a)    

#index():
# print(a.index(9))

#count:
# print(a.count(9))

#sorting:
# st=[8,45,33,7,1,63,18,93,10,12,999,5]
# st.sort()
# print(st)
# st.reverse()
# print(st)
# st.sort(reverse=True)
# print(st)

#copying the list:
# frnd1 = ["A","A","B","D","C","B","C","C","D","B","D","A"]
# frnd2 = frnd1.copy()
# print(frnd2)

#built-in funtions with loops:
# a=[1,3,5,7,9,11,13,15]
# a.sort()
# print(len(a))
# print(max(a))
# print(min(a))
# print(sum(a))

# multiple values using input data to the list:
# a=input("enter the multiple values:").split()
# print(a)
# a.sort()
# print(a)
# a=list(map(int,input("enter the mulyiple values:").split()))
# print(a)

#traversing a list:
# cars=["bmw","toyota","thar","range rover","audi"]
# for car in cars:
#     print("cars=",car)

#using index with for loops:
# a=len(cars)
# for i in range(0,a):
#     print("cars",i,cars[i])

#adding element using loops:
# list1=[]
# for list in range(0,7):
#     a = input("value:")
#     list1.append(a)
# print(list1)
# food=[]
# for list in range(0,10):
#     a = input ("value:")
#     food.append(a)
# print(food)

# give the input values to the lists from 0 to 10:
# list2=[]
# n = int(input("enter n value:"))
# for i in range(0,n):
#      list2.append(i)
# print(list2)

# list1=[90,80,70,60,50]
# sum=1
# for i in list1:
#     sum=sum*i
# print(sum)

#convert ["p","y","t","h","o","n"] to python
# n1=("p")
# n2=("y")
# n3=("t")
# n4=("h")
# n5=("o")
# n6=("n")
# print(n1+n2+n3+n4+n5+n6)
# print("python")               #fun
# print("c")

#find the maximum and minimum number from list without using max() and min().
# list12=[2,3,5,7,11,13,17]
# list12.sort()
# print(list12)
# print("maximum of list :",list12[6])
# print("minimum of list :",list12[0])


# max1=list12[0]
# min1=list12[0]
# for num in list12:
#     if num > max1:
#         max1 = num
#     if num < min1:
#         min1 = num

# print(max1)
# print(min1)


#searching for an element in a list:

# list1 = ("shashi","nani","sai","chintu")
# searching_name = input("enter the name to be found: ")
# found = False
# for i in list1:
#     if searching_name == i:
#        found = True

# if found:
#     print("yes")
# else:
#     print("no")


# #count even and odd numbers:

# numb = [45,63,33,18,7,5,99,93,10,2,11]

# evn_cnt = 0
# odd_cnt = 0
# for i in range(len(numb)):

#     if numb[i]%2 == 0:
#         evn_cnt += 1
#     else:
#         odd_cnt += 1
# print("no of even numb are: ",evn_cnt)
# print("no of odd numb are: ",odd_cnt)


 #reversing a list without reverse:

# list1 = [45,63,33,18,7,5,99,93,10,2,11]
# list1.reverse()
# print(list1)


#removing all negative numbers using loop:

# numb = [45,-63,-33,18,-7,5,99,93,-10,2,-11]
# positive_list = []
# for i in range(len(numb)):
#     if numb[i] > 0:
#         positive_list.append(numb[i])
# print(positive_list)


# multiply each element in the list:

# numbers = [1,2,3,4,5]
# multiplier = 2
# result = []
# for num in numbers:
#     result.append(num * multiplier)
# print(result)

# m = int(input("enter the number to be multiplied: "))
# After_multiplication = []
# for i in numbers:
#     After_multiplication.append(i*m)
# print(After_multiplication)
    
#AVERAGE
# list1 = [1,2,3]
# average = sum(list1) / len(list1)
# print(average)

#count how many +,-,0 are in list:
# numb = [45,-63,-33,18,-7,5,0,0,99,93,-10,2,-11]
# positive_cnt = 0
# negative_cnt = 0
# zero_cnt = 0
# for i in range(len(numb)):

#     if numb[i] > 0:
#         positive_cnt += 1
#     elif numb[i] < 0:
#         negative_cnt += 1
#     else :
#         zero_cnt += 1
# print("no of positive numb are: ",positive_cnt)
# print("no of negative numb are: ",negative_cnt)
# print("no of zeros are: ",zero_cnt)

# REMOVE DUPLICATE ELEMENTS FROM LIST:
numb = [45,-63,-33,18,-7,5,99,93,-10,2,-11]
# unique_numb = list(set(numb))
# print(unique_numb)

#NO OF EVEN & ODD:
evn_num = []
odd_num = []
for i in range(len(numb)):

    if numb[i]%2 == 0:
        evn_num += 1
    else:
        odd_num += 1
print("even numb are: ",evn_num)
print("odd numb are: ",odd_num)
