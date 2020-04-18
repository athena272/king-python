hora_oficial= 0
minuto_oficial= 0
hi, mi, hf, mf= input('Informe os valores da HORA INICIAL, MINUTO INICIAL, HORA FINAL, MINUTO FINAL (0h---24h): ').split()
hi= int(hi)
mi= int(mi)
hf= int(hf)
mf= int(mf)
#começo do código
if (hi == hf):
    hora_oficial= 24
