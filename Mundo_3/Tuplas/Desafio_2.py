times = ('Athletico Paranaense',
'Atlético Mineiro',
'Avaí',
'Bahia',
'Botafogo',
'Ceará',
'Chapecoense',
'Corinthians',
'Cruzeiro',
'CSA',
'Flamengo',
'Fluminense',
'Fortaleza',
'Goiás',
'Grêmio',
'Internacional',
'Palmeiras',
'Santos',
'São Paulo',
'Vasco da Gama')
print('-=' *12)
print(f'Times ddo Brasileirão 2019: {times}')
print('-=' *12)
print(f'Os 5 primeiros times são: {times[:5]}')
print('-=' *12)
print(f'Os 4 últimos times são: {times[(len(times) - 4):]}')
print('-=' *12)
print(f'Os times em ordem alfabética ficam: {sorted(times)}')
print('-=' *12)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição')