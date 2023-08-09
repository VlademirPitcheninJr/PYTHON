from ex1 import *
from ex2 import *
from ex3 import *
from ex4 import *
from ex5 import *
from ex6 import *
from ex7 import *
from ex8 import *
from ex9 import *
from ex10 import *

exercicio = input("Digite o exercício (Ex.: 'ex6') que quer resolver ou 'sair' para encerrar:")

while exercicio != "sair":
    if exercicio == 'ex1':

        valor = int(input("Digite um valor:"))

        print(verifica_positivo(valor))

    if exercicio == 'ex2':

        valor = int(input("Digite um valor:"))

        positivo_negativo(valor)

    if exercicio == 'ex3':

        valor_impar_par = int(input("Digite um valor:"))
        
        impar_par(valor_impar_par)

    if exercicio == 'ex4':
        
        tipo_calculo = input("Digite o tipo de média ('A' para aritmética e 'P' para ponderada):")
        nota1 = float(input("Digite a nota 1:"))
        nota2 = float(input("Digite a nota 2:"))
        nota3 = float(input("Digite a nota 3:"))

        print(notas(tipo_calculo, nota1, nota2, nota3))

    if exercicio == 'ex5':
        
        anos = int(input("Digite sua idade em anos:"))
        meses = int(input("Digite sua idade em meses:"))
        dias = int(input("Digite sua idade em dias:"))

        print(idade(anos, meses, dias))

    if exercicio == 'ex6':
        
        valor1 = int(input("Digite o valor 1:"))
        valor2 = int(input("Digite o valor 2:"))
        valor3 = int(input("Digite o valor 3:"))

        crescente(valor1, valor2, valor3)

    if exercicio == 'ex7':
        
        segundos = int(input("Digite em segundos:"))

        converter_tempo(segundos)

    if exercicio == 'ex8':
        
        numero = int(input("Digite um número:"))
        resultado = valor_perfeito(numero)

        if resultado:
            print(numero, "é um número perfeito.")
        else:
            print(numero, "não é um número perfeito.")

    if exercicio == 'ex9':
        
        sexo = input("Digite o sexo:")
        altura = float(input("Digite a altura:"))

        print(peso_ideal(altura, sexo))
    if exercicio == 'ex10':
        
        x = int(input("Digite o valor X:"))
        y = int(input("Digite o valor Y:"))
        z = int(input("Digite o valor Z:"))

        verifica_triangulo(x, y, z)

    exercicio = input("Digite o exercício que quer resolver ou 'sair' para encerrar:")