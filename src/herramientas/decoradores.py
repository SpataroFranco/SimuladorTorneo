import time
from functools import wraps

def medir_tiempo(func):
    """
    Metodo que de registra en un txt logs los tiempos que tarda en ejecutarse las simulaciones
    Recibe una funcion 
    Retorna el tiempo que tarda en ejecutarse
    """
    @wraps(func)
    def wrapper(*args, **kwargs):

        inicio = time.perf_counter()

        resultado = func(*args, **kwargs)

        fin = time.perf_counter()

        with open("src/datos/logs.txt", "a", encoding="utf-8") as archivo:
            archivo.write(
                f"{func.__name__}: {fin - inicio:.4f} segundos\n"
            )

        return resultado

    return wrapper