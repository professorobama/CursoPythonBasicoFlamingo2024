#Cabeçalho
#Nome do Curso Python Básico
#Nome do Professor: Jailson Costa dos Santos
#Data de Criação: 10/10/2022
#Data de Atualização: 10/10/2022

def soma():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    soma=num1+num2
    print("A soma dos dois números é: ",soma)

def subtracao():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    subtracao=num1-num2
    print("A soma dos dois números é: ",subtracao)

def multiplicacao():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    multiplicacao=num1*num2
    print("A soma dos dois números é: ",multiplicacao)

def divisao():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    divisao=num1/num2
    print("A soma dos dois números é: ",divisao)

print("Aqui será exibido as 4 operações matemáticas básicas: ")
soma()
subtracao()
multiplicacao()
divisao()