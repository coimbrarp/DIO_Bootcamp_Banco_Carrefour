v = int(input('Insira um valor menor ou igual a 51: '))

while v > 51:
  v = int(input('Insira um valor menor ou igual a 51: '))

vetor = [10]
vetor[0] = v

for i in range (0, 10):
  vetor.append(vetor[i]*2)
  print("N[%.d] = " %(i), vetor[i])