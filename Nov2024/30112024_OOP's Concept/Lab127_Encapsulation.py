class car:

    def __init__(self,o_name,o_make,o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("Start the engine with name" + " -> " + self.name)
        print("Start the engine with make" + " -> " +self.make)
        print("Start the engine with model" + " -> " +self.model)

lambo = car("Lambo","V6","2023")
lambo.start_engine()

print("-------")

XUV = car("Mahindra_XUV","1.5T","700")
XUV.start_engine()