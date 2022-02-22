tempoSegundos = int(input())

dias = (tempoSegundos // (3600 * 24))#So me interessa a parte inteira
segundosRestantes = (tempoSegundos % (3600 * 24))#Pega os segundos que sobraram

horas = (segundosRestantes // 3600)  #So me interessa a parte inteira
segundosRestantes = (tempoSegundos % 3600) #Pega os segundos que sobraram

minutos = (segundosRestantes // 60) #Transforma eles em minutos

segundos = (segundosRestantes % 60) #Pega os segundos que sobraram 

print(f'{dias}\n{horas}\n{minutos}\n{segundos}')
