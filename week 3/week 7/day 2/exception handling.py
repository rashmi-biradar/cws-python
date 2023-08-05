"""
exception handling

"""
try:
    a = int(input("enter num 1 = "))
    b = int(input("enter num 2 = "))
    print(a * b)
except:
    print("value error")
else:
    print("this is a else statememnt")
finally:
    print("this is a fianl statememnt")
