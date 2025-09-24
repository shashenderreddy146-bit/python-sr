# dictionary
# syntax
# my_dict={
#     "key1":"value1",
#     "key2":"value1",
#     "key3":"value1",
#     "key4":"value1"
# }
# print(my_dict)

# characteristics of dictionary

# keys must be immutable:
# keys can be (valid keys):integer,float,string
# my_dict={
#     1:"value1"
#     10.2:"value2"
#     "key3":"value3"
#     "key4":"value4"
# }


# creating dictionary:
# normal dictionary:
# biodata = {
#     "Name":"shashi",
#     "Roll.No":"5G1",
#     "branch":"CSM AI&ML",
#     "place":"vikarabad"
# }
# print(biodata)

# dictionary using construtor:
# biodata1 = dict(Name="shashi",Roll_No="5G1",branch="CSM AI&ML",place="vikarabad")
# print(biodata1)

# empty dictionary:
# E_D = {}

# accessing the dictionary:
# biodata = {
#     "Name":"shashi",
#     "Roll.No":"5G1",
#     "branch":"CSM AI&ML",
#     "place":"vikarabad"
# }
# print(biodata["Name"])      #shashi
# print(biodata["Roll.No"])    #5G1
# print(biodata["place"])       #vikarabad
# print(biodata["branch"])       #CSM AI&ML

# # using get() method:
# print(biodata.get("Name"))     #shashi
# print(biodata.get("Roll.No"))     #5G1
# print(biodata.get("branch"))      #CSM AI&ML
# print(biodata.get("place"))      #vikarabad
# print(biodata.get("age"))      #None

# adding & updating:

# biodata = {
#     "Name":"shashi",
#     "Roll.No":"5G1",
#     "branch":"CSM AI&ML",
#     "place":"vikarabad"
# }
# biodata["age"] = 18       #adding the new key and values
# print(biodata)
# biodata["place"] = "damasthapur"        #changing or updating the existed key's value
# print(biodata)

# Removing in dictionary:

# biodata = {
#     "Name":"shashi",
#     "Roll.No":"5G1",
#     "branch":"CSM AI&ML",
#     "place":"vikarabad",
#     "role":"student"
# }

# # pop():removes the key value
# biodata.pop("Roll.No")
# print(biodata)

# # popitem():removes the last inserted item from the dictionary.
# biodata.popitem()
# print(biodata)

# # del(delete):
# del biodata["branch"]
# print(biodata)

# # clear():
# biodata.clear()
# print(biodata)

# dictionary methods:
# methods allows you to access dictionary data esily.
# keys(),values(),items():



# loops for dictionary:
# l=[4,6,3,5,3,6,7]
# for i in l:
#     print(i)

# biodata={
#     "Name":"shashi",
#     "Roll.No":"5G1",
#     "branch":"CSM AI&ML",
#     "place":"vikarabad",
#     "role":"student"
# }

# for i in biodata:
#     print(i)
# for i in biodata.keys():
#     print(i)
# for i in biodata.values():
#     print(i)
# for i in biodata.items():
#     print(i)

# nested dictionary:
 

biodata1={
    "s1":{"Name":"shashi","RollNo":"5G1"},
    "s2":{"Name":"raj","RollNo":"45"}
}

print(biodata1["s1"]["Name"])
print(biodata1["s1"]["RollNo"])
print(biodata1["s2"]["Name"])
print(biodata1["s2"]["RollNo"])