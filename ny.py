def fibonacci(n):
  if n < 1:
      return n
  elif n == 1 or n == 2:
      return 1
  elif n > 2:
      return fibonacci(n - 1) + fibonacci(n - 2)

numCheck = int(input())
lista = []
pos = 0

while (fibonacci(pos) <= numCheck):
  lista.append(fibonacci(pos))
  pos = pos + 1

estarFibonacci = 'nao'
for i in lista:
  if numCheck == i:
    estarFibonacci = 'sim'
    break

print("Está em Fibonacci?:",estarFibonacci)
  