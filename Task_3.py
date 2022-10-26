dck = dict()
while True:
    a = input('Введите имя исполнителя')
    if a == 'off':
        break
    b = input('Введите название трека')
    dck[a] = b

print(dck)