class User(object):
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    def getUserDetail(self):
        return self.name, self.email, self.address


userList = []
i = 0
while i < 3:
    userList.append(User(input("name:  "), input("email:  "), input("address:  ")))
    i = i + 1
    print("............................................................................")

print(userList)
for users in userList:
    print(users.getUserDetail())


loginUser = User(input("name:  "), input("email:  "), input("address:  "))
for users in userList:
    if loginUser.getUserDetail() == users.getUserDetail():
        print(f"Welcome {loginUser.name}")
        break
    else:
        print(f"You are not registered yet")

