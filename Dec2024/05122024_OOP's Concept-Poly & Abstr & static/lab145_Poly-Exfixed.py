

class cal:

    def sum(self, a, b):
        return a + b

    def sum(self, a, b, c=2):
        return a + b + c


cal_obj = cal()
result = cal_obj.sum(3, 4)
print(result)
