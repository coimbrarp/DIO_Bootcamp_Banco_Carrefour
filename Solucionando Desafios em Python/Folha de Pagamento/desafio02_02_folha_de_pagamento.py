emp_no = int(input('Insira o número do funcionário: '))
worked_hours = int(input('Insira a quantidade de horas trabalhadas: '))
receives_per_worked_hour = float(input('Insira o valor da hora trabalhada: '))

salary = worked_hours * receives_per_worked_hour

print("NUMBER = ", emp_no, end="\n")
print("SALARY = U$ %0.2f" %salary, end="\n")