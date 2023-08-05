# try:
#     name = input("enter the name = ")
#     password = input("enter the password = ")
#     if name == "rashmi" and password == "BTS":
#         print("u successfully logged in")
#     else:
#         raise Exception("wrong password")
# except Exception as r:
#     print(r)
# def foo():
#     try:
#         print(1)
#     finally:
#         print(2)


# foo()
try:
    num = int(input("enter a num = "))
    fact = 0
    for i in range(1, num + 1):
        if num % i == 0:
            fact = fact + 1
    if fact == 2:
        print("the num is prime")
    else:
        raise Exception("the num is not a prime num")
except ValueError:
    print("enter a correct num")
except Exception as p:
    print(p)
