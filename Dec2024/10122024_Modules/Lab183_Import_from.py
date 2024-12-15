from browser_package.Openbrowser import open_browser
from browser_package.Closebrowser import close_browser


class Test_Case:

    def test_case(self):
        open_browser()
        print("The browser is running")
        close_browser()


s_obj = test_case()
s_obj.test_case()

# in pyhton package is nothing but a directory only,
