from abc import ABC, abstractmethod


class Excel_reader(ABC):

    @abstractmethod
    def set_gear(self):
        pass


class browser(Excel_reader):

    @abstractmethod
    def start(self):
        super().set_gear()
        pass

    @abstractmethod
    def stop(self):
        pass


class TC1():

    def start(self):
        print("Start browser")

    def stop(self):
        print("Stop browser")

    def set_gear(self):
        print("Gear box is ready to drive")

    def drive(self):
        self.start()
        self.stop()


s_obj = TC1()
s_obj.drive()
