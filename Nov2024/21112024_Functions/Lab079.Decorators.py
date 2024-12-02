# Decorators -

def add_security (func):
    def wrappers():
        print("Before riding the scooty take the necessary steps")
        print("those are taking helmet, license")
        func()
        print("After riding the scooty things to leave")
        print("Leave the helmet & license & park the vehicle")
    return wrappers()

@add_security
def driving_scooty():
    print("Driving is going on smooth")
    print("No accidents has been happened")

@add_security
def scooty_details():
    print("Having a scooty pep")
