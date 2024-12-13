from logging import exception

print("Start of program")
try:
    a = (int(input("Enter the num 1")))
    b = (int(input("Enter the num 2")))
    c = b / a
    print("Result div is", c)

except Exception as e:
    print(e)
print("End of the program")

# try & Except
