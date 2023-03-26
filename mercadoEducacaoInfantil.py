qtd_transacoes = int(input("Digite a quantidade de transações realizou: "))
total_transacoes = 0

for x in range(qtd_transacoes):
    transacoes = float(input("Digite o valor da transação {}: ".format(x+1)))
    total_transacoes += transacoes
    media_transacoes = total_transacoes / qtd_transacoes

print("O valor total das transações realizadas: {}\nA média do valor das transações: {}".format(total_transacoes,media_transacoes))