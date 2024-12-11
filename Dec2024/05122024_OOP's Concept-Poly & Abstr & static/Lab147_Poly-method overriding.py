
class parent:

    def home(self):
        print("2-BHK")

class son(parent):

    def villa(self):
        print("3_BHK")

    def home(self):
        print("10_BHK")

ref_obj = son()
ref_obj.home()
ref_obj.town()