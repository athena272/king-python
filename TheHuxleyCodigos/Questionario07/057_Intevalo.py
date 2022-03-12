valorReal = float(input())

intervalo = 'Intervalo [0,25]'
if(valorReal > 25 and valorReal <= 50):
    intervalo = 'Intervalo (25,50]'
elif(valorReal > 50 and valorReal <= 75):
    intervalo = 'Intervalo (50,75]'
elif(valorReal > 75 and valorReal <= 100):
    intervalo = 'Intervalo (75,100]'
elif(valorReal < 0 or valorReal > 100):
    intervalo = 'Fora de intervalo'

print(intervalo)