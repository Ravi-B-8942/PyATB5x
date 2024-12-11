from abc import ABC, abstractmethod


class gear_box(ABC):

    @abstractmethod
    def set_gear(self):
        pass


class engine(gear_box):

    @abstractmethod
    def start(self):
        super().set_gear()
        pass

    @abstractmethod
    def stop(self):
        pass


class car(engine):

    def start(self):
        print("Start")

    def stop(self):
        print("Stop")

    def set_gear(self):
        print("Gear box is ready to drive")

    def drive(self):
        self.start()
        self.stop()


s_obj = car()
s_obj.drive()
