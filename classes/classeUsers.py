class User:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age
    def great_user(self):
        full_name = f" Name: {self.name} last_name: {self.last_name} age: {self.age}".title()
        print(full_name)
class Admin(User):

    def __init__(self, name, last_name, age):

        super().__init__(name, last_name, age)
        self.privilege = []

    def great_admin(self):
       print( f" Sir {self.name} welcome to the office")

    def show_privileges(self):

        if self.privilege:
            for privilege in self.privilege:
                print(privilege)
        else:
            print(" Privileges are empty")



user1 = Admin("jailson",'Ribeiro', 31)
user1.great_user()
user1.great_admin()
user1.privilege =['pode editar','pode deletar']
user1.show_privileges()
