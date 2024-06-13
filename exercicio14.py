#Cabecalho
#Nome : Jailson
#Data : 25/05/2024
#Crie um programa que pergunte ao usuário a quantidade 
#de dias, horas, minutos e segundos, e calcule o total em segundos.

dia =int(input("Digite a quantidade de dias :"))
hora =int(input("Digite a quantidade de hora :"))
minutos =int(input("Digite a quantidade de minutos :"))
segundos =int(input("Digite a quantidade de segundos :"))
total = (dia*24*60*60)+(hora*60*60)+(minutos*60)+(segundos)
print("O total de segundos é : ",total)