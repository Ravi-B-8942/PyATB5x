
class O:

    @staticmethod
    def sum(a,b):                # for static method no need to create an obj
        return a+b

    def sub(self,a,b):                 # for Non-static need to create an obj for result
        return b-a

print(O.sum(3,4))

print("-------")

s_obj = O()
result = s_obj.sub(4,3)
print(result)