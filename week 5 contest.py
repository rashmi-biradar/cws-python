def get_factors(n):
    i = 2
    while i < n:
        if n % i == 0:
            i = i + 1
    return i


n = input("enter a number -> ")
x = get_factors(n)
print(x)
