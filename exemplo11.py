idade = int(input("Digite a sua idade :"))
print("Você não pode votar") if idade < 16 else print("Voto opcional") if idade <18 else print("Voto obrigatório")