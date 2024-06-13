#Cabecalho
#Nome : Jailson
#Data : 25/05/2024
#Faça um programa que receba um número inteiro e retorne se é primo ou não.
#Um número inteiro é primo quando ele é divisível apenas por 1 e por ele mesmo.
#Exemplo: 2, 3, 5, 7, 11, 13, 17, 19, 23
numero =int(input("Digite um número inteiro para saber se é primo :"))
if numero<=1:
        print("O número não é primo")
elif numero%2==0 and numero!=2:
        print("O número não é primo")
elif numero%3==0 and numero!=3 or numero%5==0 and numero!=5 or numero%7==0 and numero!=7:
    print("O número não é primo")
else:
       print("O número é primo")
