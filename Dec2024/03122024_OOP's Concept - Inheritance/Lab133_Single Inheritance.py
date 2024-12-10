
class father:
    Key = "2BHK"

    def car(self):
        print(self.Key)
        print("Having an ALto car")


class son(father):
    key2 = "3BHK"

    def car2(self):
        print(self.key2)
        print("Having a TATA HARRIER car")


father_obj = father()
father_obj.car()

print("-------")

son_obj = son()
son_obj.car2()
son_obj.car()

