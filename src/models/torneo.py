from models.partido import Partido
from herramientas.excepciones import cantidadEquiposError
from herramientas.decoradores import medir_tiempo
import uuid
import csv

class Torneo:
    def __init__(self, id_torneo, nombre):
        self._id = id_torneo
        self._nombre = nombre
        self._equipos = []
        self._campeon = None

    @property
    def get_nombre(self):
        return self._nombre

    @property
    def get_equipos(self):
        return self._equipos
    

    def agregar_equipo(self, equipo):
        self._equipos.append(equipo)

    #Metodo que genera las fechas del torneo
    @medir_tiempo
    def generar_fechas(self):
        if len(self._equipos) < 2:
            raise cantidadEquiposError()

        if len(self._equipos) % 2 != 0:
            raise cantidadEquiposError()

        equipos = self._equipos[:]
        cantidad_fechas = len(equipos) - 1

        for _ in range(cantidad_fechas):
            fecha = []

            for i in range(len(equipos) // 2):
                local = equipos[i]
                visitante = equipos[-(i + 1)]

                partido = Partido(
                    uuid.uuid4(),
                    local,
                    visitante
                )

                fecha.append(partido)

            yield fecha

            equipos = (
                [equipos[0]]
                + [equipos[-1]]
                + equipos[1:-1]
            )

    #Metodo que devuelve la tabla de resultados ordenada por puntos, diferencia de gol y goles a favor
    def mostrar_tabla(self):
        tabla = sorted(self._equipos,key=lambda e: (e.get_puntos(),e.get_diferencia_gol(),e.get_goles_favor()),reverse=True)

        print("\nPOS | EQUIPO | PTS | DG")
        #Recorre la tabla de posiciones y la imprime con formato alineado
        for pos, equipo in enumerate(tabla, start=1):
            print(
                f"{pos:>2} | "
                f"{equipo.get_nombre():<25} | "
                f"{equipo.get_puntos():>3} | "
                f"{equipo.get_diferencia_gol():>3}"
            )
    #Metodo que devuelve al campeon en base a los puntos, diferencia de gol y goles a favor
    def obtener_campeon(self):
        self._campeon = max(self._equipos,key=lambda e: (e.get_puntos(),e.get_diferencia_gol(),e.get_goles_favor()))
        return self._campeon
    
    #Metodo que guarda la tabla de resultados en un archivo csv 
    @medir_tiempo
    def guardar_tabla_csv(self, archivo_csv):
        tabla = sorted(self._equipos,key=lambda e: (e.get_puntos(),e.get_diferencia_gol(),e.get_goles_favor()),reverse=True)
        with open(archivo_csv,"w",newline="",encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["Pos","Equipo","PJ","PG","PE","PP","Pts","GF","GC","DG"])

            for pos, equipo in enumerate(tabla, start=1):
                escritor.writerow([pos,equipo.get_nombre(),equipo.get_partidos_jugados(),equipo.get_victorias(),equipo.get_empates(),
                                   equipo.get_derrotas(),equipo.get_puntos(),equipo.get_goles_favor(),equipo.get_goles_contra(),equipo.get_diferencia_gol()])

    def __str__(self):
        return f"Torneo: {self._nombre}"