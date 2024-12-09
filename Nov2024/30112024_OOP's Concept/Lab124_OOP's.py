a = 10  # Global variable


class person:
    b = 11  # Instance variable


def print_info(self):
    c = 20  # Local Variable
    print(c)
    print(self.b)
    global a
    print(a)


object_ref = person()
object_ref.print_info()
