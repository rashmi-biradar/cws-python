a = [1, 2, 3, 5, 6, 8]
i = 0
prime = 0
for i in range(0, 7):
    if prime == a[i] >= 1 and a[i] % a[i] == 0:
        print(a[i])
