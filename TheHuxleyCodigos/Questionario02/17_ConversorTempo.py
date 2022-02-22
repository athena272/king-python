tempoSegundos = int(input())

horas = (tempoSegundos // 3600)  #So me interessa a parte inteira
segundosRestantes = (tempoSegundos % 3600) #Pega os segundos que sobraram

minutos = (segundosRestantes // 60) #Transforma eles em minutos

segundos = (segundosRestantes % 60) #Pega os segundos que sobraram 

print(str(horas) + ':' + str(minutos) + ':' + str(segundos))

