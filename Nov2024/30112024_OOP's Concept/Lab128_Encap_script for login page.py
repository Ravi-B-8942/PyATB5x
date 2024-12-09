# web automation = selenium

class VM_login():

    def __init__(self,o_email,o_password):
        self.email = o_email
        self.password = o_password

    def login_confirm (self):
        if self.email == "Vm123@gmail.com" and self.password == "VM@123":
            print("Login Success")
        else:
            print("Login failed")

email = input("Enter the valid email\n")
password = input("Enter the valid password\n")

vmlog = VM_login("Vm123@gmail.com","VM@123")
vmlog.login_confirm()
