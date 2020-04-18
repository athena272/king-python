#transformar Cº em Fº
Celcius = float(input('Informe a temperatura(°C): '))
formula = ((9*Celcius) / 5) + 32
print('A temperatura {:.1f}°C corresponde à {:.1f}°F'.format(Celcius, formula))