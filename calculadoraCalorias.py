qtd_alimentos = int(input("Digite a quantidade de alimentos que você consumiu no dia: "))
total_calorias = 0

for x in range(qtd_alimentos):
    calorias = float(input("Digite as calorias do alimento {}: ".format(x+1)))
    total_calorias += calorias
print("Total de calorias consumidas no dia: ", total_calorias)
