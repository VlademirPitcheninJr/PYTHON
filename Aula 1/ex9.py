#Exercicio 9

def peso_ideal(altura, sexo):
    if sexo == "masculino":
        peso_ideal = 72.7 * altura - 58
    else:
        peso_ideal = 62.1 * altura - 44.7
    return peso_ideal

