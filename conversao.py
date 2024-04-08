print   ("---------------------------")
print   ("         COTAÇÃO           ")
print   ("---------------------------")

def converter_dolar_para_real(valor_dolar, cotacao_dolar):
    valor_real = valor_dolar / cotacao_dolar
    return valor_real

valor_dolar = float(input('Quanto em dólares você deseja converter para reais? US$ '))
cotacao_dolar = float(input('Qual é a cotação do dólar em reais? '))

print(f'O valor em reais é R$ {converter_dolar_para_real(valor_dolar, cotacao_dolar):.2f}')