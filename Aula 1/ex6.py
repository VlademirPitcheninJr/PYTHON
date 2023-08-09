#Exercício 6

def crescente(valor1, valor2, valor3):
    if valor1 < valor2 < valor3:
        print(valor1, valor2, valor3)
    if valor1 < valor3 < valor2:
        print(valor1, valor3, valor2)
    if valor2 < valor1 < valor3:
        print(valor2, valor1, valor3)
    if valor2 < valor3 < valor1:
        print(valor2, valor3, valor1)
    if valor3 < valor2 < valor1:
        print(valor3, valor2, valor1)
    if valor3 < valor1 < valor2:
        print(valor3, valor1, valor2)
    return crescente

