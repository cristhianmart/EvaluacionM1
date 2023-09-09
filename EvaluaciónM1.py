notas_estudiantes = {
    'Juan': [3.2, 4.5, 5],
    'Maria': [4.2, 3.5, 4.3],
    'Pedro': [3.9, 2.5, 4.8]
}

def calcular_promedio (diccionario):
        resultado = 0
        for llave, valores in diccionario.items():
             total = sum(valores)
             promedio = total / 3
             print ("el promedio final del estudiante ", llave, "es de ", promedio)
           
                   
                        

calcular_promedio(notas_estudiantes)