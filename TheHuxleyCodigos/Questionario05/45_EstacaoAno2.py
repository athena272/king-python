def EstacaoAno(hemisferio, dia, mes):
    if(hemisferio == 1):
        if(dia >= 21 and mes == 9) or (dia >= 1 and mes == 10 or mes == 11) or (dia <= 20 and mes == 12):
            return 'PRIMAVERA'
        elif(dia >= 21 and mes == 12) or (dia >= 1 and mes == 1 or mes == 2) or (dia <= 20 and mes == 3):
            return 'VERAO'
        elif(dia >= 21 and mes == 3) or (dia >= 1 and mes == 4 or mes == 5) or (dia <= 20 and mes == 6):
            return 'OUTONO'
        elif(dia >= 21 and mes == 6) or (dia >= 1 and mes == 7 or mes == 8) or (dia <= 20 and mes == 9):
            return 'INVERNO'
    else: 
        if(dia >= 21 and mes == 3) or (dia >= 1 and mes == 4 or mes == 5) or (dia <= 20 and mes == 6):
            return 'PRIMAVERA'
        elif(dia >= 21 and mes == 6) or (dia >= 1 and mes == 7 or mes == 8) or (dia <= 20 and mes == 9):
            return 'VERAO'
        elif(dia >= 21 and mes == 9) or (dia >= 1 and mes == 10 or mes == 11) or (dia <= 20 and mes == 12):
            return 'OUTONO'
        elif(dia >= 21 and mes == 12) or (dia >= 1 and mes == 1 or mes == 2) or (dia <= 20 and mes == 3):
            return 'INVERNO'

hemisferio = int(input())
dia = int(input())
mes = int(input())

print(EstacaoAno(hemisferio, dia, mes))