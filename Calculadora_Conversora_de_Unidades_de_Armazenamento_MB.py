valor_universal = 1024

def converterStringParaFloat(value):
    return float(value)

def KBParaMB(valorASerConvertido):
    print('Valor convertido de KB para MB')
    bitsCalculado = valorASerConvertido / valor_universal
    return bitsCalculado

print('Insira o valor a ser convertido de KB para MB')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = KBParaMB(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

def MBparaKB(valorASerConvertido):
    print('Valor convertido de MB para KB')
    bitsCalculado = valorASerConvertido * valor_universal
    return bitsCalculado

print('Insira o valor a ser convertido de MB para KB')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = MBparaKB(entradaDoTecladoValorASerConvertido)
print(valorConvertido)