escolhaAlice = int(input())
escolhaBeto = int(input())
escolhaClara = int(input())
               
aliceGanha = (escolhaAlice != escolhaBeto and escolhaAlice != escolhaClara)
betoGanha = (escolhaBeto != escolhaAlice and escolhaBeto != escolhaClara)
claraGanha = (escolhaClara != escolhaAlice and escolhaClara != escolhaBeto)

vencedor = '*'

if (aliceGanha):
    vencedor = 'A'
elif(betoGanha):
    vencedor = 'B'
elif(claraGanha):
    vencedor = 'C'
    
print(vencedor)

