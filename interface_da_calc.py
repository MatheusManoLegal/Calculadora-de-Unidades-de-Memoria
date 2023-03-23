from Calculadora_para_conversao_de_unidades_de_Memoria import converterStringParaFloat, bitParaByte, byteParaBit, byteParaKB, KBparabyte, KBParaMB, MBparaKB, MBparaGB, GBparaMB, GBparaTB, TBparaGB, TBparaPB, PBparaTB

print(' -Escreva 1 Bit para Byte \n -Escreva 2 Byte para Bit \n -Escreva 3 KB para Byte \n -Escreva 4 byte para KB \n -Escreva 5 KB para MB \n -Escreva 6 MB para KB \n -Escreva 7 MB para GB \n -Escreva 8 GB para MB \n -Escreva 9 GB para TB \n -Escreva 10  TB para GB \n -Escreva 11 TB para PB \n -Escreva 12 PB para TB')
funcEscolha = input()
if(funcEscolha == '1'):
    print('Insira o valor a ser convertido')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = bitParaByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '2'):
    print('Insira o valor a ser convertido')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = byteParaBit(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '3'):
    print('Insira o valor a ser convertido')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = KBparabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)
    
elif(funcEscolha == '4'):
    print('Insira o valor a ser convertido')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = byteParaKB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)
    
elif(funcEscolha == '5'):
    print('Insira o valor a ser convertido')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = KBParaMB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)
    
elif(funcEscolha == '6'):
    print('Insira o valor a ser convertido')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = MBparaKB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '7'):
    print('Insira o valor a ser convertido')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = MBparaGB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '8'):
    print('Insira o valor a ser convertido')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = GBparaMB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '9'):
    print('Insira o valor a ser convertido')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = GBparaTB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '10'):
    print('Insira o valor a ser convertido')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = TBparaGB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '11'):
    print('Insira o valor a ser convertido')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = TBparaPB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '12'):
    print('Insira o valor a ser convertido')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = PBparaTB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)    