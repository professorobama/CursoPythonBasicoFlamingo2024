#Cabecalho
#Nome : Jailson
#Data : 11/05/2024
#Faça um programa que pergunte ao usuário o valor do produto e o percentual de desconto, e retorne o valor final após o desconto.

valorDoProduto = float(input("Digite o valor do produto :"))
valorDesconto = float(input("Digite o percentual de desconto :"))
valorFinal = valorDoProduto - (valorDoProduto * (valorDesconto/100))
print("O valor do produto final é :",valorFinal)