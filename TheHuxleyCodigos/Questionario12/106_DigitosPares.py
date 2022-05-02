def contDigitosPares(num):
    if num == []:
        return 0
    else:
        if num[0] % 2 == 0:
            return 1 + contDigitosPares(num[1:])
        else:
            return 0 + contDigitosPares(num[1:])

num = input()
digitosNum = list()
for i in num:
    digitosNum.append(int(i))
print(contDigitosPares(digitosNum))