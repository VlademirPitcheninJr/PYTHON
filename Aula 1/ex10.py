#Exercicio 10

def verifica_triangulo(x, y, z):
    if x < y + z and y < x + z and z < x + y:
        if x == y == z:
            print("Triangulo equilátero!")
        elif x == y or x == z or y == z:
            print("Triangulo isóceles!")
        else:
            print("Triangulo escaleno!")
    else:
        print("Não é um triângulo!")
    return verifica_triangulo

