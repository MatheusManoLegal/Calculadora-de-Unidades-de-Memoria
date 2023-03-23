valor_universal = 1024

def converterStringParaFloat(value):
    return float(value)

def MBparaGB(valorASerConvertido):
    print('Valor convertido de MB para GB')
    bitsCalculado = valorASerConvertido / valor_universal
    return bitsCalculado

print('Insira o valor a ser convertido de MB para GB')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = MBparaGB(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

#KB para Byte

def GBparaMB(valorASerConvertido):
    print('Valor convertido de GB para MB')
    bitsCalculado = valorASerConvertido * valor_universal
    return bitsCalculado

print('Insira o valor a ser convertido de GB para MB')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = GBparaMB(entradaDoTecladoValorASerConvertido)
print(valorConvertido)