dct = dict()
numbers = "0139412831055230677798"
for i in range(1,10):
    dct[i] = numbers.count(str(i))

print(dct)