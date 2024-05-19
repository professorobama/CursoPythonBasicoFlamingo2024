#Calcule a area de um hexagono regular

# Importação d biblioteca Math
import math

lado = float(input("Digite o valor do lado de um hexagono para  calcular a sua area : "))
resultado= ((3*pow(lado,2)*math.sqrt(3))/2)
print ("A área do Hexagono é: ",round(resultado,2), " m²")
             