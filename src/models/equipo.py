from abc import ABC, abstractmethod
from herramientas.excepciones import (ataqueError,defensaError,resistenciaError,rankingError,nombreEquipoError)

class Equipo(ABC):
    """
    Clase abstracta que representa un equipo de fútbol
    Define los atributos y comportamientos comunes a todos los tipos de equipos del simulador.} 
    No puede instanciarse directamente, sino que debe heredarse e implementar el método calcular_potencia()
    Atributos:
        _id (str): Identificador único del equipo
        _nombre (str): Nombre del equipo
        _ranking (int): Ranking del equipo entre 1 y 100
        _ataque (int): Nivel de ataque entre 0 y 100
        _defensa (int): Nivel de defensa entre 0 y 100
        _resistencia (int): Nivel de resistencia entre 0 y 100
        _victorias (int): Cantidad de partidos ganados
        _empates (int): Cantidad de partidos empatados
        _derrotas (int): Cantidad de partidos perdidos
        _goles_favor (int): Goles convertidos
        _goles_contra (int): Goles recibidos

    Lanza los errores:
        nombreEquipoError: Si el nombre está vacío
        ataqueError: Si el ataque está fuera del rango permitido
        defensaError: Si la defensa está fuera del rango permitido
        rankingError: Si el ranking no está entre 1 y 100
        resistenciaError: Si la resistencia está fuera del rango permitido
    """
    def __init__(self, id_equipo:str, nombre:str, ranking:int, ataque:int, defensa:int, resistencia:int):
        self._validar_nombre(nombre,nombreEquipoError())
        self._validar_rango(ataque,0,100,ataqueError())
        self._validar_rango(defensa,0,100,defensaError())
        self._validar_rango(ranking,1,100,rankingError())
        self._validar_rango(resistencia,0,100,resistenciaError())
        self._id = id_equipo
        self._nombre = nombre
        self._ranking = ranking
        self._ataque = ataque
        self._defensa = defensa
        self._resistencia = resistencia
        self._victorias = 0
        self._empates = 0
        self._derrotas = 0
        self._goles_favor = 0
        self._goles_contra = 0

    #Metodo privado que valida las entradas para lanzar la excepcion
    def _validar_rango(self,valor, minimo, maximo, excepcion):
        if (valor < minimo or valor > maximo):
            raise excepcion
        
    #Metodo privado que valida el nombre del equipo
    def _validar_nombre(self,nombre,excepcion):
        if nombre.strip() == "":
            raise excepcion

    #Metodo que se encarga de calcular la potencia de un equipo
    @abstractmethod
    def calcular_potencia(self):
        pass

    #Metodo para setear el ataque
    def setAtaque(self,ataque):
        self._validar_rango(ataque,0,100,ataqueError())
        self._ataque = ataque

    #Metodo para setear la defensa
    def setDefensa(self,defensa):
        self._validar_rango(defensa,0,100,defensaError())
        self._defensa = defensa

    #Metodo para setear la resistencia
    def setResistencia(self, resistencia):
        self._validar_rango(resistencia,0,100,resistenciaError())
        self._resistencia = resistencia

    #Metodo para aumentar las victorias del equipo
    def guardar_victoria(self):
        self._victorias+=1

    #Metodo que muestra los stats del equipo
    def mostrar_estadisticas(self):
        print("Equipo: ",self._nombre)
        print("Victorias: ",self._victorias)
        print("Empates: ",self._empates)
        print("Derrotas: ",self._derrotas)
        print("Goles a favor: ",self._goles_favor)
        print("Goles en contra: ",self._goles_contra)

    #Metodo para aumentar y guardar la cantidad de empates en 1
    def guardar_empate(self):
        self._empates += 1
    #Metodo para aumentar y guardar la cantidad de derrotas en 1
    def guardar_derrota(self):
        self._derrotas += 1
    #Metodo para aumentar y guardar la cantidad de goles a favor en 1
    def agregar_goles_favor(self, goles):
        self._goles_favor += goles
    #Metodo para aumentar y guardar la cantidad de goles en contra en 1
    def agregar_goles_contra(self, goles):
        self._goles_contra += goles

    # Getters
    def get_nombre(self):
        return self._nombre

    def get_victorias(self):
        return self._victorias

    def get_empates(self):
        return self._empates

    def get_derrotas(self):
        return self._derrotas
    
    def get_partidos_jugados(self):
        return self._victorias+self._derrotas+self._empates

    def get_goles_favor(self):
        return self._goles_favor

    def get_goles_contra(self):
        return self._goles_contra

    def get_puntos(self):
        return self._victorias * 3 + self._empates

    def get_diferencia_gol(self):
        return self._goles_favor - self._goles_contra
    
    def __str__(self):
        return (
            f"{self._nombre} | "
            f"Ranking: {self._ranking} | "
            f"Ataque: {self._ataque} | "
            f"Defensa: {self._defensa} | "
            f"Resistencia: {self._resistencia}"
        )