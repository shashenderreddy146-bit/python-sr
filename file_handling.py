file=open("student.txt","w")
# print("file created")
# file.close()


# types of read :

# 1. read() :
# file=open("student.text","r")
# content=file.read()
# print(content)
# file.close()

# 2. readline():
# file=open("student.txt","r")
# content=file.readline()
# content1=file.readline()
# content2=file.readline()
# print(content)
# print(content1)
# print(content2)

# 3. readlines() :
# file=open("student.text","r")
# content=file.read()
# print(content)
# file.close()
 
#  write, writelines:
file.write("hello c++\n")
file.write("hello python\n")
lines=["hello shashi\n","hello deva\n","hello world\n","hello python\n"]
file.writelines(lines)
file.close()
