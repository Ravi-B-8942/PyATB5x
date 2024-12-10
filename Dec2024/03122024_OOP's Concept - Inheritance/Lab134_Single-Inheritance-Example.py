
class parent:
    key = "2kg-Gold"

    def asset(self):
        print(self.key)
        print("2BHK,2-car")

class son (parent):
    key2 = "daimond"

    def asset1(self):
        print(self.key2)
        print("3BHK,3-car")

par_obj = parent()
par_obj.asset()

print("-------")

son_obj = son()
son_obj.asset()
son_obj.asset1()