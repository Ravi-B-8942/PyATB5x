
class gf():
    key = "1-kg gold"

    def asset(self):
        print(self.key)
        print("Having an 1-BHK")

class f(gf):
    key1 = "2-Kg Gold"

    def asset1(self):
        print(self.key1)
        print("Having an 2-BHK")

class s(f):
    key2 = "Daimond"

    def asset2(self):
        print(self.key2)
        print("Having an villa")

gf_obj = gf()
gf_obj.asset()

print("------")

f_obj = f()
f_obj.asset()
f_obj.asset1()

print("------")

s_obj = s()
s_obj.asset()
s_obj.asset1()
s_obj.asset2()