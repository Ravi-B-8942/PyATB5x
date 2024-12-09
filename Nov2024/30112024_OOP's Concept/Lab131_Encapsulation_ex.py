from time import sleep


class bank():

    def __init__(self,account_no,balance):
        self.balance = balance # public
        self.__account_no = account_no # private

    def check_bal(self):
        print(self.balance)

    def deposit(self):
        self.balance = self.balance + self.deposit()

PKGB = bank(64146213428,45000)
print(PKGB.balance)