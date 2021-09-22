x = int(input('Insira um valor: '))
vetor = [10]
vetor[0] = x

for i in range (0, 10):
  vetor.append(vetor[i]*2)
  print("N[%.d] = " %(i), vetor[i])