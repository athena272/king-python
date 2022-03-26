palavra = input()
letra = input()

cont = 0
ocorrencia = -1
for i in palavra:
    if i in letra:
        ocorrencia = cont
        break
    cont += 1

print(ocorrencia)