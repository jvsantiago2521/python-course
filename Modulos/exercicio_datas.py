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

emprestimo = 1_000_000
prazo_final = timedelta(days=1826)
data_inicio = datetime(2020, 12, 20)
data_final = data_inicio + prazo_final
lista_datas_vencimento = []
num_parcelas = 0
dias_corridos = timedelta(days=0)

print(f"DATA DO EMPRESTIMO: {data_inicio.strftime("%d/%m/%Y")}")
print()
print(f"DATA DO FINAL DO EMPRESTIMO: {data_final.strftime("%d/%m/%Y")}")
print()

while dias_corridos < prazo_final:
    dias_corridos += timedelta(days=1)
    dia_atual = data_inicio + dias_corridos

    if dia_atual.day == 20:
        num_parcelas += 1
        lista_datas_vencimento.append(f"[{dia_atual}]")

for data in lista_datas_vencimento:
    print(f"{data} -> R$ {emprestimo/num_parcelas}")

print()
print(f"Numero de parcelas = {num_parcelas}")

