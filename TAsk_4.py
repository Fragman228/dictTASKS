dck = {
    "1": "one",
    '2': "two",
    "3": "three",
    "4": "four",
    "5": "five"
}
print(dck)
dck.pop("5")
print(dck)
dck.update(dck.popitem())