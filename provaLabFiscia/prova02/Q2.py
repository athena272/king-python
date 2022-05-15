from sympy import symbols, Eq, solve 

dados = input().split()

tempInicialM = float(dados[0])
tempA = float(dados[1])
tempB = float(dados[2])
tempC = float(dados[3])
massaMetal = float(dados[4])
massaAgua = float(dados[5])

a, b = symbols('a,b') 

eq1 = Eq((a*5 + b), tempA) 
 
eq2 = Eq((a*15 + b), tempB) 
  
resultadoEqLinear = solve((eq1, eq2), (a, b))

eqLinear = resultadoEqLinear[a]*20 + resultadoEqLinear[b]

calorAgua = 1
tempInicialS = eqLinear
tempFinal = tempC

deltaS = tempFinal - tempInicialS
deltaM = tempFinal - tempInicialM

calorMetal = -(((massaAgua*calorAgua)*(deltaS))/(massaMetal*(deltaM)))

print('O calor específico do metal:', '%.2f' % 
calorMetal)

erroPercentual = ((calorMetal - 0.22) / 0.22) * 100

print('O erro percentual absoluto:', '%.2f' % erroPercentual,'%' ) 