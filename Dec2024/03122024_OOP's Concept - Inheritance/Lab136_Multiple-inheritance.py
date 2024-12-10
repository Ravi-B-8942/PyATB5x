
class father:

    def f_money(self):
        return 5

class mother:

    def m_money(self):
        return 15

class son(father,mother):

    def s_money(self):
        print("son")


s = son()
print(s.f_money())
print(s.m_money())
print(s.f_money()+s.m_money())