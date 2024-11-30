# i/p is 3 no's
# o/p is shld display as type of triangle whether it is Equilateral = 10,10,10, isosceles = 10,10,8 or scalar = 4,5,6


side1 = int(input("Length of side1\n"))
side2 = int(input("Length of side2\n"))
side3 = int(input("Length of side3\n"))

if side1 == side2 and side3 == side1:
    print("It's an Equilateral Triangle")
elif (side1 == side2) and (side1 != side3):
    print("It's an Isosceles Triangle")
elif side1 <= 0 and side2 <= 0 and side3 <= 0:
    print("Invalid length")
else:
    print("It's an Scalar Triangle")


"""
side1 = int(input("enter the side1 \n"))
side2 = int(input("enter the side2 \n"))
side3 = int(input("enter the side3 \n"))

if (side1==side2) and (side1==side3) :
    print ("the triangle is equilateral (all sides are equal)")
elif (side1==side2) and (side1!=side3) :
    print("isosceles (exactly two sides are equal)")
else:
    print("scalene (no sides are equal)")
"""