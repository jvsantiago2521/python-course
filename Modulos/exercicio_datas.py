# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime, timedelta

emprestimo = 1000000
prazo_final = timedelta(days=1826)
data_inicio = datetime(2020, 12, 20)
data_final = data_inicio + prazo_final

def mostra_vencimentos_e_valores():
    num_parcelas = 0
    aux = 0

    print("Segue as datas de vencimento e os valores das parcelas:")

    while 1:

        aux += 1
        data_vencimento = data_inicio + timedelta(days=aux)

        if data_vencimento.day == 20:
            num_parcelas += 1
            print(f"[{data_vencimento}]")

        if aux > 1826:
            print[num_parcelas]
            break
        #data_vencimento = data_inicio + timedelta(days=aux)
        #if data_vencimento == data_final:
        #    break


print(f"DATA DO EMPRESTIMO: {data_inicio.strftime("%d/%m/%Y")}")
print()
print(f"DATA DO FINAL DO EMPRESTIMO: {data_final.strftime("%d/%m/%Y")}")
print()
mostra_vencimentos_e_valores()

