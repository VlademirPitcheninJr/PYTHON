#Exercicio 7

def converter_tempo(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = segundos % 60

    horas_str = str(horas)
    minutos_str = str(minutos)
    segundos_str = str(segundos)

    print(horas_str, ':', minutos_str, ':', segundos_str)
    
    return converter_tempo

