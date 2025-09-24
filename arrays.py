# arrays in python:

# importing the array module
import array as arr

# creating an array:

numbers=arr.array('i',[1,2,3,4,5])
print(type(numbers))
print(numbers)

# accessing array elements:
print(numbers[0])
print(numbers[1])
print(numbers[-5])


# adding an element in array:
# append():
numbers.append(7)
print(numbers)


# insert():
numbers.insert(2,6)
print(numbers)

# extend():
numbers.extend([8,9])
print(numbers)


# deleting an element:
# remove():
numbers.remove(2)
print(numbers)

# pop():
numbers.pop()
print(numbers)

# looping through arrays:
for i in numbers:
    print(i)

# basicoperations on arrays:
# len():
print(len(numbers))
# max():
print(max(numbers))
# min():
print(min(numbers))
