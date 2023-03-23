valor_universal = 1024

def converterStringParaFloat(value):
    return float(value)

def TBparaPB(valorASerConvertido):
    print('Valor convertido de TB para PB')
    bitsCalculado = valorASerConvertido / valor_universal
    return bitsCalculado

print('Insira o valor a ser convertido de TB para PB')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = TBparaPB(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

def PBparaTB(valorASerConvertido):
    print('Valor convertido de PB para TB')
    bitsCalculado = valorASerConvertido * valor_universal
    return bitsCalculado

print('Insira o valor a ser convertido de PB para TB')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = PBparaTB(entradaDoTecladoValorASerConvertido)
print(valorConvertido)