from abc import ABC, abstractmethod


class father(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass

class son(father):

    def loan(self):
        print("Loan has been cleared by Ravi")


d_obj = son("Ravi")
d_obj.loan()
