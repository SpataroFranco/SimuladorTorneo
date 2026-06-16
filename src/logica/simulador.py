import threading
import time
from queue import Queue
from herramientas.decoradores import medir_tiempo

class Simulador:
    def __init__(self):
        self._threads = []
        self._resultados = []
        self._lock = threading.Lock()
        self._cola = Queue()

    #Metodo que retorna el threads
    def get_threads(self):
        return self._threads

    #Metodo que retorna los resultados
    def get_resultados(self):
        return self._resultados
    
    #Limpia los resultados del simulador
    def limpiar(self):
        self._resultados.clear()
    
    #Metodo que realiza la simulacion del partido
    @medir_tiempo
    def simular_partido(self, partido):

        print(
            f"[{threading.current_thread().name}] "
            f"Simulando {partido}"
        )

        time.sleep(2)

        partido.jugar_partido()

        with self._lock:
            self._resultados.append(partido)

        print(
            f"[{threading.current_thread().name}] "
            f"Finalizado {partido}"
        )

    @medir_tiempo
    def ejecutar_fecha(self, fecha):
        self._threads = []
        cantidad_consumidores = 6

        # Crear consumidores
        for i in range(cantidad_consumidores):

            thread = threading.Thread(
                target=self.consumidor,
                name=f"Consumidor-{i+1}"
            )

            thread.start()
            self._threads.append(thread)

        # Productor carga los partidos
        self.producir_fecha(fecha)

        # Esperar que se procesen todos los partidos
        self._cola.join()

        # Señales de finalización
        for _ in range(cantidad_consumidores):
            self._cola.put(None)

        # Esperar consumidores
        for thread in self._threads:
            thread.join()

    def mostrar_resultados(self):
        print("\n========== RESULTADOS ==========")
        for partido in self._resultados:
            partido.mostrar_resultado()

    # Metodo productor
    def producir_fecha(self, fecha):
        for partido in fecha:
            self._cola.put(partido)

    #Metodo consumidor
    def consumidor(self):
        while True:
            partido = self._cola.get()

            if partido is None:
                self._cola.task_done()
                break

            self.simular_partido(partido)

            self._cola.task_done()

    def __str__(self):
        return f"Simulador con {len(self._threads)} hilos"