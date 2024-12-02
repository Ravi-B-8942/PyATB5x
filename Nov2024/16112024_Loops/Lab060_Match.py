
browser_name = input("Enter the browser name\n")
match browser_name:
    case "firefox":
        print("Browser name is firefox")
    case "Chrome":
        print("Browser name is chrome")
    case "Edge":
        print("Browser name is Edge")
    case "Internet_Explorer":
        print("Browser name is Internet_Explorer")
    case _:
        print("Browser not found")
