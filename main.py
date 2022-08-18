# class User(object):
#     def __init__(self, name, email, address):
#         self.name = name
#         self.email = email
#         self.address = address
#
#     def getUserDetail(self):
#         return self.name, self.email, self.address
#
#
# userList = []
# i = 0
# while i < 3:
#     userList.append(User(input("name:  "), input("email:  "), input("address:  ")))
#     i = i + 1
#     print("............................................................................")
#
# print(userList)
# for users in userList:
#     print(users.getUserDetail())
#
#
# loginUser = User(input("name:  "), input("email:  "), input("address:  "))
# for users in userList:
#     if loginUser.getUserDetail() == users.getUserDetail():
#         print(f"Welcome {loginUser.name}")
#         break
#     else:
#         print(f"You are not registered yet")

#
# from abc import ABC, abstractmethod
# class Product(ABC):
#     def __init__(self,id,name,color):
#         self.name = name
#         self.id = id
#         self.color = color
#
#
# class DigitalProduct(Product):
#     pass
# product1 = Product(2,"Bag","red")
# dP = DigitalProduct(1,"Watch","green")
# print(product1.name)

# def call():
#     print("calling")
#     return "calling"
#
# mynames = [
#     [1,2,3],
#     call(),
#     {"name":"Andrew", "age":24},
#     {"func":call()}
#            ]
# for name in mynames:
#     print(type(name),name)
#
# print(type(mynames[3]["func"]))
# print(type(call()))

# def acceptsYName(name):
#     print("this name starts with Y")
#     return name
#
# def collectList(names):
#     for name in names:
#         if str(name)[0] == "y":
#             acceptsYName(name)
#         else:
#             print(name)
#
# collectList(["kolawole","yinusa","Timgbasa","Yaradua","Femi Kuti"])
#
# names = ["kola","osagie","damilola","ooh"]
# def checkNamesLength(names):
#     i = 0
#     for name in names:
#         shortestName = names[i]
#         if len(str(shortestName)) < len(str(name[i])):
#             shortestName = name
#         i = i+1
#
#     print(shortestName)
#     return shortestName
#
# checkNamesLength(names)

# Binary Search in python


def binarySorter(startingPoint,endPoint,arr,x):
    print(f"Your Array is: {arr}")
    print("sorting Your Array.........................................................................")
    arr.sort()
    print(arr)
    while startingPoint <= endPoint:
        mid = startingPoint + (endPoint - startingPoint)//2
        if arr[mid]== x:
            print(f" {x} found at index {mid} ")
            return mid

        elif arr[mid] < x :
            startingPoint = mid + 1
        else:
            endPoint = mid- 1
    return -1

arr = [1,45,67,89,2,3,4,5,45,89,12,34,56]
binarySorter(0,len(arr)-1,arr,45)