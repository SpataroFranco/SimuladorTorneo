import threading
import time
from queue import Queue
from herramientas.decoradores import medir_tiempo

class Simulador:
    """
    Clase que se encarga de simular los partidos de una fecha utilizando hilos mediante el patron Productor-Consumidor.
    Atributos:
        _threads: lista con los hilos consumidores
        _resultados: lista con los partidos ya simulados
        _lock: bloquea para proteger el acceso a la lista de resultados
        _cola: cola compartida entre productor y consumidores
    """
    def __init__(self):
        self._threads = []
        self._resultados = []
        self._lock = threading.Lock()
        self._cola = Queue()

    #Metodo que retorna el threads
    def get_threads(self):
        return self._threads

    #Metodo que retorna los partidos simulados
    def get_resultados(self):
        return self._resultados
    
    #Metodo que limpia los resultados del simulador
    def limpiar(self):
        self._resultados.clear()
    
    @medir_tiempo
    def simular_partido(self, partido):
        """
        Metodo que simula un partido
        Muestra que hilos se estan simulando en el encuentro
        Ejecuta un partido y almacena el resultado de forma segura
        """
        print(
            f"[{threading.current_thread().name}] "
            f"Simulando {partido}"
        )

        # Simula el tiempo de procesamiento del partido
        time.sleep(2)

        # Ejecuta la logica interna del partido
        partido.jugar_partido()
        # Se protege el acceso a la lista compartida
        # para evitar condiciones de carrera
        with self._lock:
            self._resultados.append(partido)

        print(
            f"[{threading.current_thread().name}] "
            f"Finalizado {partido}"
        )

    @medir_tiempo
    def ejecutar_fecha(self, fecha):
        """
        Metodo que simula los partidos de una fecha utilizando el patron Productor-Consumidor
        Crea los hilos consumidores, el Productor carga los partidos en la cola, espera a que sean procesados,
        envia señales de finalizacion a los consumidores y espera a que los hilos terminen
        """
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

        # Productor carga los partidos a la cola
        self.producir_fecha(fecha)

        # Espera que se procesen todos los partidos de la cola
        self._cola.join()

        # Envia señales de finalización a cada consumidor
        for _ in range(cantidad_consumidores):
            self._cola.put(None)

        # Espera a que los consumidores terminen
        for thread in self._threads:
            thread.join()

    def mostrar_resultados(self):
        """
        Metodo que muestra por pantalla el resultado de todos los partidos simulados.
        """
        print("\n========== RESULTADOS ==========")
        for partido in self._resultados:
            partido.mostrar_resultado()

    def producir_fecha(self, fecha):
        """
        Metodo productor que inserta todos los partidos de una fecha en la cola compartida
        Recibe una coleccion de partidos a simular
        """
        for partido in fecha:
            self._cola.put(partido)

    def consumidor(self):
        """
        Metodo consumidor que obtiene partidos de la cola y los simula
        Se ejecuta indefinidamente hasta recibir None que indica su finalizacion
        """
        while True:
            partido = self._cola.get()

            if partido is None:
                self._cola.task_done()
                break

            self.simular_partido(partido)

            self._cola.task_done()

    def __str__(self):
        return f"Simulador con {len(self._threads)} hilos"