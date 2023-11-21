# Faça um programa que pergunte quanto você ganha por hora e
# o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no
# referido mês.
def salario():
    salarioA = float(input("Quanto vc ganha por hora? "))
    num = float(input("quantas horas voce trabalha por mês? "))
    salario = salarioA*num 
    print (f"seu salario é de {salario}")
salario()
