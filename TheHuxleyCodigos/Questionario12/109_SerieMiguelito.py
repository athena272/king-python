def serieMiguelito(num):
    if num <= 1:
        return 3
    elif num == 2:
        return 3 + 4
    elif num == 3:
        return 3 + 4 + 1
    else:
        if num %2 == 0:
            return 4 + serieMiguelito(num-1)
        else:
            return 1 + serieMiguelito(num-1)
        
numeroMiguelito = int(input())        
print(serieMiguelito(numeroMiguelito))