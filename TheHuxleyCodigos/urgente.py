#Texto de apresentação
print('=-' * 30)
print('Bem-Vindo ao Shopping Center Carvalho&Silva')
print('=-' * 30)
print('#' * 45)
print('EXEMPLO de horário a ser digitado: 17:53:18')
print('#' * 45)
#Recebimento do horario de entrada e saida
horarioEntrada = input('Informe o horário de entrada: ').split(':')
horarioSaida = input('Informe o horário de saída: ').split(':')
#Converte e capturar a hora, minuto e segundo da entrada
horaEntrada = int(horarioEntrada[0])
minutoEntrada = int(horarioEntrada[1])
segundoEntrada = int(horarioEntrada[2])
#Converte e capturar a hora, minuto e segundo da saida
horaSaida = int(horarioSaida[0])
minutoSaida = int(horarioSaida[1])
segundoSaida = int(horarioSaida[2])
#Converter horario da entrada passado em Segundos
tempoTotalEntrada = (horaEntrada * 3600) + (minutoEntrada * 60) + segundoEntrada
tempoTotalSaida = (horaSaida * 3600) + (minutoSaida * 60) + segundoSaida 
#Acha o tempo da estadia e converte em minutos
tempoEstadia = (tempoTotalSaida - tempoTotalEntrada) / 60
#Definir o valor a ser pago
valorPagar = 0

if(tempoEstadia >= 21 and tempoEstadia <= 60):
    valorPagar = 3

elif(tempoEstadia >= 61 and tempoEstadia <= 120):
    valorPagar = 6

elif(tempoEstadia >= 121 and tempoEstadia <= 180):
    valorPagar = 9

elif(tempoEstadia >= 181 and tempoEstadia <= 240):
    valorPagar = 12

elif(tempoEstadia > 240):
    valorPagar = 15
    
#Saida Final, o famoso recibo
print('#' * 15)
print('RECEBIDO ESTACIONAMENTO')
print('#' * 15)
print(f'Horário de Entrada: {horaEntrada}:{minutoEntrada}:{segundoEntrada}')
print(f'Horário de Saída: {horaSaida}:{minutoSaida}:{segundoSaida}')
print(f'Tempo de estadia no estacionamento: {tempoEstadia} minuto(s)')
print('Valor Total: R$ {:.2f}'.format(valorPagar))



