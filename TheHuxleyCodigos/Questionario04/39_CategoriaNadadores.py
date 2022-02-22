idadeNadador = int(input())

categoria = 'Infantil A'

if(idadeNadador < 5):
    categoria = 'Idade invalida.'
elif(idadeNadador >= 8 and idadeNadador <= 10):
    categoria = 'Infantil B'
elif(idadeNadador >= 11 and idadeNadador <= 13):
    categoria = 'Juvenil A'
elif(idadeNadador >= 14 and idadeNadador <= 17):
    categoria = 'Juvenil B'
elif(idadeNadador >= 18 and idadeNadador <= 40):
    categoria = 'Adulto'
elif(idadeNadador >= 41):
    categoria = 'Master'

print(categoria)