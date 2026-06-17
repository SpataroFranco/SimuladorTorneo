import random
from models.equipo import Equipo
from herramientas.excepciones import (estadoFisicoError)


class EquipoAmateur(Equipo):
    """
    Clase que crea un equipo amateur
    Hereda de Equipo y posee su atributo estado_fisico el cual influye en la potencia del equipo    
    Atributos:
        id_equipo: Identificador único del equipo
        nombre: Nombre del equipo
        ranking: Ranking del equipo
        ataque: Nivel de ataque del equipo
        defensa: Nivel de defensa del equipo
        resistencia: Nivel de resistencia del equipo
        _estado_fisico (int): Estado fisico del equipo, con valores entre 0 y 100

    Lanza estadoFisicoError() en caso de que el estado fisico no se encuentre en rangos aceptables
    """
    def __init__(
        self,
        id_equipo,
        nombre,
        ranking,
        ataque,
        defensa,
        resistencia,
        estado_fisico:int
    ):
        super().__init__(
            id_equipo,
            nombre,
            ranking,
            ataque,
            defensa,
            resistencia
        )

        self._validar_rango(estado_fisico,0,100,estadoFisicoError())
        self._estado_fisico = estado_fisico

    def calcular_potencia(self):
        """
        Metodo que calcula la potencia en base a sus atributos multiplicados por un peso y un factor suerte que afecta entre 20% por arriba o por abajo de su potencia
        Pesos utilizados:
            - Ataque: 25%
            - Defensa: 20%
            - Resistencia: 20%
            - Estado físico: 35%
        Retorna la potencia final del equipo (float)       
        """
        potencia_base = (
            self._ataque * 0.25 +
            self._defensa * 0.20 +
            self._resistencia * 0.20 +
            self._estado_fisico * 0.35
        )

        factor = random.uniform(0.8, 1.2)

        return potencia_base * factor
    
    def recuperar_fisico(self):
        """
        Metodo que recupera el estado físico del equipo en 10, el estado maximo es 100
        """
        self._estado_fisico += 10
        if (self._estado_fisico>100):
            self._estado_fisico=100