def binario_para_decimal(binario):
    decimal = 0
    for digito in binario:
        decimal = decimal * 2 + int(digito)
    return decimal

def converter_binario_decimal():
    binario = input("Digite um número binário: ")
    decimal = binario_para_decimal(binario)
    print(f"Binário: {binario} -> Decimal: {decimal}")

converter_binario_decimal()