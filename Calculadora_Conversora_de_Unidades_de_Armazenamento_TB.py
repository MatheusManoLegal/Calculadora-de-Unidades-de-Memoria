valor_universal = 1024

def converterStringParaFloat(value):
    return float(value)

def GBparaTB(valorASerConvertido):
    print('Valor convertido de GB para TB')
    bitsCalculado = valorASerConvertido / valor_universal
    return bitsCalculado

print('Insira o valor em GB para ser convertido em TB:')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = GBparaTB(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

def TBparaGB(valorASerConvertido):
    print('Valor convertido de TB para GB')
    bitsCalculado = valorASerConvertido * valor_universal
    return bitsCalculado

print('Insira o valor a ser convertido de TB para GB')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = TBparaGB(entradaDoTecladoValorASerConvertido)
print(valorConvertido)