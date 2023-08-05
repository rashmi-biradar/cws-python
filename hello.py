a = [7, 5, -2, -1, 5, 6, -3]
i = 0
total = 0
product = 1
for i in range(0, 7):
    if a[i] > 0:
        total = total + a[i]
    else:
        product = product * a[i]
print(total)
print(product)
