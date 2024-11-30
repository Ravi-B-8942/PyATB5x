# find max b/w 2 no's

num1 = float(input("Enter the num1"))
num2 = float(input("Enter the num2"))

if num1 > num2 :
    print("Max no is",num1)
else:
    print("Min no is",num2)

# Edge cases - if num1 = num2, it will execute
#            - If it Alphanumeric, throws an error as can't convert str in to int or float, will learn in future
#            - If negative values given, will learn this in future.