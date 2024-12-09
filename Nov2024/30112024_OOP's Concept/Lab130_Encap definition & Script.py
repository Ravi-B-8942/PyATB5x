# Encapsulation - hiding the data members(Class variables or instance variables)
# by using only the methods

class car():

    def __init__(self):
        self.password = "Ravi@123" # public password
        self.__password_secure = "Gee@894" # Private password

    def change_password(self):
        print(self.password)

object_ref = car()
print(object_ref.password)
print(object_ref.__password_secure)