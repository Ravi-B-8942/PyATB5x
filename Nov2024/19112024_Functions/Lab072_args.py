import args


def print_mul_arg(*args):
    for i in args:
        print(i)

print_mul_arg("Ravi")
print_mul_arg("Ravi",'10',True)
print_mul_arg("Geetha",'20',False)


