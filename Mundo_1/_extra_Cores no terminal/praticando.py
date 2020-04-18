#------------PADRÂO ANSI----------------
#Style [0] none
#Style [1] bold, negrito
#Style [4] sublinhado
#Style [7] negative(inverte fundo e letra)
#----------------------------------------
#text [30] branco
#text [31] vermelho
#text [32] verde
#text [33] amarelo
#text [34] azul
#text [35] lilas
#text [36] azul bebê
#text [37] cinza
#------------------------------------------
#back_ground [40] branco
#back_ground [41] vermelho
#back_ground [42] verde
#back_ground [43] amarelo
#back_ground [44] azul
#back_ground [45] lilas
#back_ground [46] azul bebê
#back_ground [47] cinza
print('\033[0;30;41mTESTE\033[m')
print('\033[4;33;44mTESTE\033[m')
print('\033[1;35;43mTESTE\033[m')
print('\033[30;42mTESTE\033[m')
print('\033[mTESTE\033[m')
print('\033[7;30mTESTE\033[m')
print('--------------')
print('\033[4;30;45mHello World\033[m')