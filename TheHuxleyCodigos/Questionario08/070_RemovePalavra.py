palavra = input()
palavraRemover = input()
palavraAparecer = ''
for letra in palavra:
    if(letra not in palavraRemover):
        palavraAparecer += letra
    
            
print(palavraAparecer)