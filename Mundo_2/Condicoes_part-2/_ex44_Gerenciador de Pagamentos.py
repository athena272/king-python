preco = float(input('Digite o preço total do(s) produto(s): R$'))
print('\033[1;36m|Tabelinha do pagamento|\033[m'
      '\n\033[4;33mDigite [1] para \033[m \033[1;34m|A vista dinheiro ou cheque -- 10% de desconto|\033[m'
      '\n\033[4;33mDigite [2] para \033[m \033[1;34m|À vista no cartão -- 5% de desconto|\033[m'
      '\n\033[4;33mDigite [3] para \033[m \033[1;34m|Em até 2 vezes no cartão -- preço original|\033[m'
      '\n\033[4;33mDigite [4] para \033[m \033[1;34m|3 vezes ou mais no cartão -- 20% juros|\033[m'
      '\n')
escolha= int(input('Digite o número da escolha que o senhor/senhora deseja: '))
if (escolha == 1):
    novo_preco = preco - (preco*0.1)
    print('O senhor escolheu o pagamento \033[1;34m"a vista dinheiro ou cheque -- 10% de desconto"\033[m'
          '\n'
          '\nO produto que custuva R${:.2f} agora passa a valer R${:.2f}'.format(preco, novo_preco))
elif (escolha == 2):
    novo_preco = preco - (preco * 0.05)
    print('O senhor escolheu o pagamento \033[1;34m"a vista no cartão -- 5% de desconto"\033[m'
          '\n'
          '\nO produto que custuva R${:.2f} agora passa a valer R${:.2f}'.format(preco, novo_preco))
elif (escolha == 3):
    parcela= preco / 2
    print('O senhor escolheu o pagamento \033[1;34m"em até 2 vezes no cartão -- preço original"\033[m'
          '\n'
          '\nO produto que custuva R${:.2f} continua valendo R${:.2f}'
          '\nSó que ele será dividio em 2 parcelas de R${:.2f} cada SEM JUROS'.format(preco, preco, parcela))
elif (escolha == 4):
    novo_preco= preco + (preco * 0.2)
    parcelas = int(input('Quantas parcelas: '))
    parcela= novo_preco / parcelas
    print('O senhor escolheu o pagamento \033[1;34m"3 vezes ou mais no cartão -- 20% juros"\033[m'
          '\n'
          '\nO produto que custuva R${:.2f} agora passa a valer R${:.2f} com {} parcelas de R${:.2f} cada'.format(preco, novo_preco, parcelas, parcela))
else:
    print('\033[1;31mForma de pagamento INVÁLIDA, tente novamente, por favor!')

