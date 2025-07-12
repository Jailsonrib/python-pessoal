class User:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age
    def great_user(self):
        full_name = f" Name: {self.name} last_name: {self.last_name} age: {self.age}".title()
        return full_name

user1 = User("jailson",'Ribeiro', 31)
print(user1.great_user())