class cal:

    def sum(self, *args):
        for a in args:
            print(a)


cal_obj = cal()
result = cal_obj.sum(3, 4)
result1 = cal_obj.sum(3, 4, 5)
result2 = cal_obj.sum(3, 4, 5, 6)

