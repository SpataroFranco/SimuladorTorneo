import random
from models.equipo import Equipo
from herramientas.excepciones import (nivelEntrenamientoError)

class EquipoProfesional(Equipo):
    """
    Clase que crea un equipo profesional
    Hereda de Equipo y posee su atributo nivel_entrenamiento el cual influye en la potencia del equipo.
    Atributos:
        id_equipo: Identificador único del equipo
        nombre: Nombre del equipo
        ranking: Ranking del equipo
        ataque: Nivel de ataque del equipo
        defensa: Nivel de defensa del equipo
        resistencia: Nivel de resistencia del equipo
        _nivel_entrenamiento (int): Nivel de entrenamiento del equipo, con valores entre 0 y 100.

    Lanza nivelEntrenamientoError() en caso de que el nivel de entrenamiento no se encuentre en rangos aceptables
    """
    def __init__(
        self,
        id_equipo,
        nombre,
        ranking,
        ataque,
        defensa,
        resistencia,
        nivel_entrenamiento:int
    ):

        super().__init__(
            id_equipo,
            nombre,
            ranking,
            ataque,
            defensa,
            resistencia
        )

        self._validar_rango(nivel_entrenamiento,0,100,nivelEntrenamientoError())
        self._nivel_entrenamiento = nivel_entrenamiento

    def calcular_potencia(self):
        """
        Metodo que calcula la potencia en base a sus atributos multiplicados por un peso y un factor suerte que afecta entre 10% por arriba o por abajo de su potencia
        Pesos utilizados:
            - Ataque: 30%
            - Defensa: 25%
            - Resistencia: 20%
            - Estado físico: 25%
        Retorna la potencia final del equipo (float)       
        """
        potencia_base = (
            self._ataque * 0.30 +
            self._defensa * 0.25 +
            self._resistencia * 0.20 +
            self._nivel_entrenamiento * 0.25
        )

        factor = random.uniform(0.9, 1.1)

        return potencia_base * factor
    
    def entrenar(self):
        """
        Metodo para aumentar ataque,defensa y nivel de entrenamiento (el maximo es 100)
        Ademas:
            - Ataque: suma como maximo 2 puntos
            - Defensa: suma como maximo 2 puntos
            - Nivel de entrenamiento: suma como maximo 2 puntos
            - resistencia: el entrenamiento consume entre 1 y 3 de resistencia
        """
        self._ataque = min(100, self._ataque + random.randint(0, 2))
        self._defensa = min(100, self._defensa + random.randint(0, 2))
        self._nivel_entrenamiento = min(100,self._nivel_entrenamiento + random.randint(0, 2))
        self._resistencia = max(0,self._resistencia - random.randint(1, 3))

    def recuperar_fisico(self):
        """
        Recupera parte de la resistencia del equipo profesional.
        """
        self._resistencia = min(100,self._resistencia + random.randint(4, 8))