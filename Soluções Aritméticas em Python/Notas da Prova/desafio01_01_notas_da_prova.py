nota = int(input('Insira uma nota de 0 a 100: '))

if 0 <= nota < 1:
    print('E')
elif 1 <= nota <= 35:
    print('D')
elif 36 <= nota <= 60:
    print('C')
elif 61 <= nota <= 85:
    print('B')
elif 86 <= nota <= 100:
    print('A')
else:
  print('Erro! Número inválido.')