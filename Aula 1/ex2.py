#Exercicio 2

def positivo_negativo(valor):
    if valor > 0:
        print(f"O valor {valor} é positivo")
    elif valor == 0:
        print(f"O valor {valor} é zero!")
    else:
        print(f"O valor {valor} é negativo!")
    return valor