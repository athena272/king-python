medida= float(input('Digite uma medida em metro (m):'))
kilometros = medida / 1000
hectometro = medida / 100
decametro= medida / 10
decimetro= medida * 10
centimetros= medida * 100
milimetros= medida * 1000
print(f"O valor de {medida}(m) vale:"
      f"\nKm: {kilometros}(km)"
      f"\nHm: {hectometro}(hm)"
      f"\nDam: {decametro}(dam)"
      f"\nDm: {decimetro}(dm)"
      f"\nCm: {centimetros}(cm)"
      f"\nMm: {milimetros}(mm)")