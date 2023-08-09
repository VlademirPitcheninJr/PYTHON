#Exercício 4

def notas(tipo_calculo, nota1, nota2, nota3):
    if tipo_calculo == 'A':
        media_aritmetica = (nota1 + nota2 + nota3)/3
        return media_aritmetica
    else:
        media_ponderada = ((nota1*5) + (nota2*3) + (nota3*2))/10
        return media_ponderada