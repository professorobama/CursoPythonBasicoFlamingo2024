#Cabecalho
#Nome : Jailson
#Data : 11/05/2024
#Crie um programa que solicite ao usuário sua altura e peso, e calcule seu índice de massa corporal (IMC).

altura = float(input("Digite a sua altura :"))
peso = float(input("Digite o seu peso :"))
imc = peso / (altura*altura)
print ("O IMC do paciente é : ",round(imc,2))