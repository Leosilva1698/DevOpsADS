def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero"

# Exemplo de uso
resultado = soma(5, 3)
print("Resultado da soma:", resultado)

resultado = subtracao(10, 4)
print("Resultado da subtração:", resultado)

resultado = multiplicacao(6, 2)
print("Resultado da multiplicação:", resultado)

resultado = divisao(8, 2)
print("Resultado da divisão:", resultado)