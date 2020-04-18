print('\033[34m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[m'
      '\n        \033[35mAlistamento miliar\033[m'
      '\n\033[34m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[m')
jovem=int(input('Olá jovem, qual a sua idade?: '))
if jovem < 18:
    fatla = 18 - jovem
    print('\033[32mVocê ainda vai se alistar! após completar 18 anos, ainda faltam {} ano(s) \033[m'.format(fatla))
elif jovem == 18:
    print('\033[33mEstá na hora de fazer o alistamento militar! você já tem 18 anos jovem\033[m')
else:
    passou= jovem - 18
    print('\033[31mO tempo ideal do seu alistamento já passou à {} ano(s)! Você tem idade superior a 18 anos\033[m'.format(passou))