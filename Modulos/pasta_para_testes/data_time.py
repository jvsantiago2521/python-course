from datetime import datetime, timedelta
#from pytz import timezone

string_date = "2024-04-20 07:49:23"
date_format = "%Y-%m-%d %H:%M:%S"

#Faz uma string virar uma data do type (datatime.datatime)
formated_date = datetime.strptime(string_date, date_format)
#print(f"{type(formated_date)}:{formated_date}")

#Cria uma data ja formatada com base nos parametros passados
data = datetime(2024, 7, 25, 15, 52)
#print(data)

#Obtem a data atual do timeset que vc escolher, sem parametro fica o padrao
#data_atual = datetime.now(timezone("Asia/Tokyo"))
#print(data_atual)

#Ajustar o formato de entrada e saida como vc quiser
formato = "%d/%m/%Y %H:%M:%S"

data1 = datetime.strptime("25/07/2024 16:38:10", formato)
data2 = datetime.strptime("22/06/2004 00:00:00", formato)
dias_a_mais = timedelta(days=10)
print(data1)
print(data2)
print(data1 + dias_a_mais)
diferenca_datas = data1 - data2
print(diferenca_datas)

#Formatando datas
data_gringa = datetime(2024, 7, 25)
data_br = data_gringa.strftime("%d/%m/%Y")
print(f"{data_gringa} -> {data_br}")
print(data_gringa.year)