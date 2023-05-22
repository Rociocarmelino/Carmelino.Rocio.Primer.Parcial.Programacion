# 1. Crear una función llamada aplicarAumento que reciba como parámetro el precio de un producto y 
# devuelva el valor del producto con un aumento del 5%. Realizar la llamada desde el main

def aplicar_aumento(precio:float) -> float:
    """_summary_
    calcula el precio final con el aumento aplicado del 5% 

    Args:
        precio (float): precio recibido 

    Returns:
        float: precio con aumento
    """
    aumento = precio * 0.05
    precio_con_aumento = precio + aumento

    return precio_con_aumento



    