from models.equipo_profesional import EquipoProfesional
from models.equipo_amateur import EquipoAmateur
import random

class Partido:
    """
    Clase que se encarga de simular el encuentro utilizando
    la potencia calculada por cada equipo, determinar el resultado,
    actualizar las estadísticas y almacenar la cantidad de goles convertidos por cada participante
    Atributos:
        _id: Identificador único del partido
        _local: Equipo que juega como local
        _visitante: Equipo que juega como visitante
        _goles_local (int): Goles convertidos por el local
        _goles_visitante (int): Goles convertidos por el visitante
    """
    def __init__(self, id_partido, local, visitante):

        self._id = id_partido
        self._local = local
        self._visitante = visitante

        self._goles_local = 0
        self._goles_visitante = 0

    #Metodo que se encarga de la simulacion de un partido 
    def jugar_partido(self):
        """
        Metodo que simula el desarrollo de un partido
        1. Calcula la potencia de ambos equipos
        2. Otorga una ventaja del 5% al equipo local
        3. Genera una cantidad inicial de goles aleatoria
        4. Ajusta los goles según la diferencia de potencias
        5. Actualiza las estadísticas de ambos equipos
        6. Determina si hubo victoria, derrota o empate
        """

        # Equipo local: entrena y recupera fisico pre partido si es profesional, si es amateur recupera solo fisico
        if isinstance(self._local, EquipoProfesional):
            self._local.entrenar()
            self._local.recuperar_fisico()
        elif isinstance(self._local, EquipoAmateur):
            self._local.recuperar_fisico()

        # Equipo visitante: entrena y recupera fisico pre partido si es profesional, si es amateur recupera solo fisico
        if isinstance(self._visitante, EquipoProfesional):
            self._visitante.entrenar()
            self._visitante.recuperar_fisico()
        elif isinstance(self._visitante, EquipoAmateur):
            self._visitante.recuperar_fisico()

        #Calcula la potencia de cada equipo
        potencia_local = self._local.calcular_potencia()
        potencia_visitante = self._visitante.calcular_potencia()

        # Ventaja al equipo local del 5%
        potencia_local *= 1.05

        diferencia = potencia_local - potencia_visitante

        #El partido comienzan ambos entre 0 y 2 goles
        self._goles_local = random.randint(0, 2)
        self._goles_visitante = random.randint(0, 2)

        #Genera los goles en base a la diferencia de potencias
        if diferencia > 15:
            self._goles_local += random.randint(1, 3)

        elif diferencia > 5:
            self._goles_local += random.randint(0, 2)

        elif diferencia < -15:
            self._goles_visitante += random.randint(1, 3)

        elif diferencia < -5:
            self._goles_visitante += random.randint(0, 2)

        #Actualizar goles a favor del local
        self._local.agregar_goles_favor(self._goles_local)
        #Actualiza goles en contra del visitante
        self._local.agregar_goles_contra(self._goles_visitante)
        #Actualiza goles a favor del visitante
        self._visitante.agregar_goles_favor(self._goles_visitante)
        #Actualiza goles en contra del local
        self._visitante.agregar_goles_contra(self._goles_local)

        # Determina el resultado en base a los goles de cada equipo
        if self._goles_local > self._goles_visitante:
            self._local.guardar_victoria()
            self._visitante.guardar_derrota()

        elif self._goles_local < self._goles_visitante:
            self._visitante.guardar_victoria()
            self._local.guardar_derrota()

        else:
            self._local.guardar_empate()
            self._visitante.guardar_empate()

        #Al finalizar el partido los equipos amateur tienen un desgaste
        if isinstance(self._local, EquipoAmateur):
            self._local.desgastar()

        if isinstance(self._visitante, EquipoAmateur):
            self._visitante.desgastar()

    def mostrar_resultado(self):
        print(
            f"{self._local.get_nombre()} "
            f"{self._goles_local} - "
            f"{self._goles_visitante} "
            f"{self._visitante.get_nombre()}"
        )

    def __str__(self):
        return (
            f"{self._local.get_nombre()} "
            f"vs "
            f"{self._visitante.get_nombre()}"
        )