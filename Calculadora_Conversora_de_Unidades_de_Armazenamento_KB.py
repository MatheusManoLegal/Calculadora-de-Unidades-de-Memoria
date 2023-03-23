valor_universal = 1024

def converterStringParaFloat(value):
    return float(value)

def byteParaKB(valorASerConvertido):
    print('Valor convertido de byte para KB')
    bitsCalculado = valorASerConvertido / valor_universal
    return bitsCalculado

print('Insira o valor a ser convertido de byte para KB')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = byteParaKB(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

def KBparabyte(valorASerConvertido):
    print('Valor convertido de KB para byte')
    bitsCalculado = valorASerConvertido * valor_universal
    return bitsCalculado

print('Insira o valor a ser convertido de KB para byte')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = KBparabyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)