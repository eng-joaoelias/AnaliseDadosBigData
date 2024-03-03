import csv
import datetime

ganhosPorHora = float(input("Quanto vc ganha por hora? R$"))
qtdHoraTrabalhadaMes = int(input("Quantas horas vc trabalhou esse mês? "))

salarioBruto = ganhosPorHora * qtdHoraTrabalhadaMes
impostoRenda = 0.15 * salarioBruto
INSS = 0.1 * salarioBruto
sindicato = 0.02 * salarioBruto
salarioLiquido = salarioBruto - (impostoRenda + INSS + sindicato)

tabelaSalario = [
    ['Salário Bruto (R$)', 'INSS (R$)', 'Sindicato (R$)', 'Salário Líquido (R$)'],
    [round(salarioBruto, 2), round(INSS, 2), round(sindicato, 2), round(salarioLiquido, 2)]
]

dia = datetime.date.today().day
mes = datetime.date.today().month
ano = datetime.date.today().year

output = str(dia) + "_" + str(mes) + "_" + str(ano) + "_" + "questao_1.csv"

# Abre o arquivo CSV em modo de escrita
with open(output, 'w', newline='') as arquivo_csv:
    # Cria um escritor CSV
    escritor_csv = csv.writer(arquivo_csv)
        
    # Escreve os dados no arquivo CSV
    for linha in tabelaSalario:
        escritor_csv.writerow(linha)

print("Arquivo salvo em >> {}".format(output))
