#Cabecalho
#Nome : Jailson
#Data : 25/05/2024
#Apresentar o total da soma obtida dos cem primeiros números inteiros (1+2+3+4+...+98+99+100).

contadora =1
acumuladora=0

while (contadora<101):
    acumuladora = acumuladora + contadora
    contadora +=1

print("A soma total corresponde a :",acumuladora)