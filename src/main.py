import uuid

from models.torneo import Torneo
from models.equipo_profesional import EquipoProfesional
from models.equipo_amateur import EquipoAmateur
from herramientas.apiFootball import ApiFootball
from logica.simulador import Simulador
from herramientas.excepciones import (errorApiKey)

from dotenv import load_dotenv
import os
load_dotenv()


API_KEY = os.getenv("API_FOOTBALL_KEY")
if not API_KEY:
    raise errorApiKey()


def main():

    api = ApiFootball(API_KEY)

    #Recojo los datos de la liga argentina temporada 2022
    datos = api.obtener_datos_equipos(
        liga=128,
        temporada=2022
    )
    #Creo torneo
    torneo = Torneo(
        uuid.uuid4(),
        "Liga Simulada"
    )

    equipos = []
    #Recorre los equipos 
    for i, dato in enumerate(datos):
        #Crea mitad profesionales, mitad amateurs
        if i % 2 == 0:
            equipo = EquipoProfesional(dato["id"],dato["nombre"],dato["ranking"],dato["ataque"],dato["defensa"],dato["resistencia"],85)
        else:
            equipo = EquipoAmateur(dato["id"],dato["nombre"],dato["ranking"],dato["ataque"],dato["defensa"],dato["resistencia"],75)

        equipos.append(equipo)
        torneo.agregar_equipo(equipo)

    print(f"Equipos cargados: {len(equipos)}")

    # Si la cantidad es impar, sacar uno
    if len(torneo.get_equipos) % 2 != 0:
        eliminado = torneo.get_equipos.pop()
        print(f"Se eliminó {eliminado.get_nombre()} "
             f"para tener cantidad par de equipos.")
    #Inicia el simulador
    simulador = Simulador()

    #Recorre las fechas y las juega
    for numero_fecha, fecha in enumerate(torneo.generar_fechas(),start=1):
        print(f"\n========== FECHA {numero_fecha} ==========")
        #Limpia las fechas anteriores
        simulador.limpiar()
        #Simula la fecha
        simulador.ejecutar_fecha(fecha)
        #Muestra los resultados de la fecha
        simulador.mostrar_resultados()
        #Muestra la tabla de puntos 
        torneo.mostrar_tabla()

    campeon = torneo.obtener_campeon()
    print("\n========== CAMPEÓN ==========")
    print(f"Equipo: {campeon.get_nombre()}")
    print(f"Puntos: {campeon.get_puntos()}")
    print(f"Diferencia de gol: {campeon.get_diferencia_gol()}")

    torneo.guardar_tabla_csv("src/datos/tabla_final.csv")
    print()
    print("Tabla final guardada correctamente")

if __name__ == "__main__":
    main()