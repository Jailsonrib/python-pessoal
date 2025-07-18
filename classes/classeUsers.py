import datetime as dt
class User:
    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
    def great_user(self):
        self.birth_year = dt.datetime.now().year - self.birth_year
        full_name = f" Name: {self.name} last_name: {self.last_name} age: {self.birth_year}".title()
        print(full_name)
class Admin(User):

    def __init__(self, name, last_name, birth_year):

        super().__init__(name, last_name, birth_year)
        self.privilege = []

    def great_admin(self):
       print( f" Sir {self.name} welcome to the office")

    def show_privileges(self):

        if self.privilege:
            for privilege in self.privilege:
                print(privilege)
        else:
            print(" Privileges are empty")



user1 = Admin('jailson','Ribeiro', 1997)
user1.great_user()
user1.great_admin()
user1.privilege =['pode editar','pode deletar','pode mijar no chão do escritório a vontade']
user1.show_privileges()
