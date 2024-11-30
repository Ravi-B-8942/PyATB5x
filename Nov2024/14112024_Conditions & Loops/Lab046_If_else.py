# max b/w 3 no's

# 1. i/p - num1, num2, num3
# 2. Rough logic - num1 > num2 and num1 > num3
#                - num2 > num1 and num2 > num3
#                - num
# 3. syntax - if , elseif , elseif , elseif , else
# 4. o/p - str

num1 = float(input("Enter the num1"))
num2 = float(input("Enter the num2"))
num3 = float(input("Enter the num3"))

if num1 > num2 and num1 > num3:
    print("Max no is",num1)
elif num2 > num1 and num2 > num3:
    print("Max no is",num2)
else:
    print("Max no is",num3)

# Edge cases - if num1 = num2, it will execute
#            - If it Alphanumeric, throws an error as can't convert str in to int or float, will learn in future
#            - If negative values given, will learn this in future.