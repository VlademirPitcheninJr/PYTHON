#Exercicio 8

def valor_perfeito(numero):
    soma_divisores = 0
    divisor = 1

    while divisor < numero:
        if numero % divisor == 0:
            soma_divisores = soma_divisores + divisor
        divisor = divisor + 1

    return soma_divisores == numero

