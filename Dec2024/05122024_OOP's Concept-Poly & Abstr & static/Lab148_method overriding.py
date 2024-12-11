
class old_browser():

    def start_browser(self):
        print("IE is starting")
    def close_browser(self):
        print("IE is closing")

class new_browser(old_browser):

    def start_browser(self):
        super().start_browser()                # super is nothing but parent.
        print("chrome is getting launched")

    def close_browser(self):
        print("chrome is getting closed")

s_obj = new_browser()
s_obj.start_browser()
s_obj.close_browser()