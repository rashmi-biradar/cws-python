try:
    a = int(input("enter num 1 = "))
    b = int(input("enter num 2 = "))
    print(a * b)
except ValueError:
    print("value is not the integer")
except:
    print("the error occured")
