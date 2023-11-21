# Crie um programa que leia o valor de um produto e imprima o
# valor com desconto, tendo em vista que o desconto aplicado é de 10%.
def produto():
    preco = float(input("Qual o valor do produto sem o desconto? "))
    desconto = preco * 10 / 100
    final = preco - desconto
    print(f"o produto com 10% de desconto fica por {final}")
produto()