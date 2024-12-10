
class father:

    def asset(self):
        print("1-BHK")

class kumar(father):

    def asset1(self):
        print("2-BHK")

class ravi(father):

    def asset2(self):
        print("3-BHK")

class akshatha(father):

    def asset3(self):
        print("No-house")

k_obj = kumar()
k_obj.asset()
k_obj.asset1()

print("-----")

r_obj = ravi()
r_obj.asset()
r_obj.asset2()

print("-----")

a_obj = akshatha()
a_obj.asset()