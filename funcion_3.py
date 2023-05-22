# 3. Crear una función que se llame ordenarCaracteres que reciba una cadena de caracteres como parámetro  
# y su responsabilidad es ordenar los caracteres de manera ascendente dentro de la cadena. 
# Ejemplo si le pasamos "algoritmo" la deja como "agilmoort"

def ordenar_caracteres(cadena:str) -> str:
    """_summary_
    la funcion ordena la cadena recibida por parametros y la devuelve ordenada
    Args:
        cadena (str): cadena a ordenar

    Returns:
        str: devuelve la cadena ordenada de forma ascendente
    """
    caracteres = list(cadena)
    tam = len(caracteres)
    for i in range(tam - 1):
        for j in range(i + 1,tam):
            if (caracteres[i] > caracteres[j]):
                aux = caracteres[i]
                caracteres[i] = caracteres[j]
                caracteres[j] = aux

    cadena_ordenada = ''.join(caracteres)  # Unir los caracteres ordenados en una cadena
    return cadena_ordenada

print(ordenar_caracteres("algoritmo"))
