import datetime


class Project(object):
    def __init__(self):
        self.users = []
        # stores logged in users
        self.session = {}
        # stores comments
        # self.comment = []

    def register(self, username, password):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        self.users.append({
            "username": username,
            "password": password
        })
        print("User successfully created")

    def login(self):
        user_name = input("Please Enter User Name")
        user_pass = input("Please Enter Your Password")

        if user_name in self.users:
            if user_pass == self.users[user_name]['password']:
                self.session.update(self.users)
