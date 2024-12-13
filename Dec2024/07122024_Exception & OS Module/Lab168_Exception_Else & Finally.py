try:
    num_1 = int(input("Enter num-1/n"))
    num_2 = int(input("Enter num-2/n"))
    result = num_1 + num_2
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("output is", result)
finally:
    print("The code is executed")