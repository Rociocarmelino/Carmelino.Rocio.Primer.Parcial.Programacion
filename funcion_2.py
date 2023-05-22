# 2. Crear una función que se llame reemplazarCaracteres que reciba una cadena de caracteres como primer parámetro,
# un carácter como segundo y otro carácter  como tercero,  la misma deberá reemplazar cada ocurrencia 
# del segundo parámetro por el tercero y devolver la cantidad de veces que se reemplazo ese carácter  en la cadena

def reemplazarCaracteres(cadena:str, caracter_a_reemplazar:str, caracter_nuevo:str) -> int:
    """_summary_
    la funcion reemplaza cada ocurrencia del caracter_a_reemplazar por el caracter_nuevo
    y devuelve la cantidad de veces que se reemplazo el caracter_original

    Args:
        cadena (_type_): cadena donde se hace el reemplazo 
        caracter_a_reemplazar (_type_): caracter que se va a reemplazar
        caracter_nuevo (_type_): caracter que va a reemplazar al caracter original

    Returns:
        _type_: _description_
    """
    cantidad_reemplazos = cadena.count(caracter_a_reemplazar)
    cadena_reemplazada = cadena.replace(caracter_a_reemplazar, caracter_nuevo)

    return cantidad_reemplazos