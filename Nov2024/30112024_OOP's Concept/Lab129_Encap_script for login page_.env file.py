# web automation = selenium
from dotenv import load_dotenv
import os

class VM_login():

    def __init__(self,o_email,o_password):
        self.email = o_email
        self.password = o_password

    def login_confirm (self):
        if self.email == "Vm123@gmail.com" and self.password == "VM@123":
            print("Login Success")
        else:
            print("Login failed")

load_dotenv()

email = os.getenv("Email")
password = os.getenv("password")

print(email,password)

vmlog = VM_login(email,password)
vmlog.login_confirm()
