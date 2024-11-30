# Grade cal
#  A = 90 - 100
#  B = 80 - 89
#  C = 70 - 79
#  D = 60 - 69
#  E = 50 - 59
#  F = Fail

Num = int(input("Enter the marks\n"))

if Num > 90 and Num < 100:
    print("Student obtained Grade-A", Num)
elif Num > 80 and Num < 89:
    print("Student obtained Grade-B", Num)
elif Num > 70 and Num < 79:
    print("Student obtained Grade-C", Num)
elif Num > 60 and Num < 69:
    print("Student obtained Grade-D", Num)
elif Num > 50 and Num < 59:
    print("Student obtained Grade-E", Num)
elif Num > 100 and Num < 0:
    print("Invalid marks", Num)
else:
    print("Student has been failed")

# Edge cases -
#            - If it Alphanumeric, throws an error as can't convert str in to int or float, will learn in future
#            - If negative values & more than 100 - Handled.
