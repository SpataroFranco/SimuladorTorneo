import requests
from herramientas.excepciones import errorApi

class ApiFootball:

    def __init__(self, api_key):
        self._api_key = api_key
        self._base_url = "https://v3.football.api-sports.io"

    def obtener_datos_equipos(self, liga, temporada):
        """
        Metodo que obtiene equipos y tabla de posiciones de una liga real y los convierte en estadisticas para determinar los puntos del simulador
        Recibe liga y año de la temporada temporada
        Retorna una lista de diccionarios con equipos y sus atributos
        """

        headers = {"x-apisports-key": self._api_key}

        response = requests.get(
            f"{self._base_url}/standings",
            headers=headers,
            params={
                "league": liga,
                "season": temporada
            }
        )
        data = response.json()

        if data.get("errors"):
            raise Exception(f"Error API Football: {data['errors']}")
        if not data["response"]:
            raise errorApi()
        data = response.json()
        tabla = data["response"][0]["league"]["standings"][0]

        max_gf = max(e["all"]["goals"]["for"] for e in tabla)
        max_gc = max(e["all"]["goals"]["against"] for e in tabla)
        min_gc = min(e["all"]["goals"]["against"] for e in tabla)
        max_pts = max(e["points"] for e in tabla)

        equipos = []

        for fila in tabla:
            #Calcula ranking: mejor posición => ranking más alto
            ranking = max(1, 101 - fila["rank"])

            #Define el ataque en base a: goles convertidos/(maxima cantidad de goles en la liga*100)
            #A mayor cantidad de goles convertidos, mayor es el ataque
            ataque = int(fila["all"]["goals"]["for"] / max_gf * 100)

            #Define la defensa en base a: goles recibidos/(equipo que más goles recibio-equipo que menos goles recibio)
            #A menor goles recibidos mejor defensa
            if max_gc == min_gc:
                defensa = 100
            else:
                defensa = int((max_gc - fila["all"]["goals"]["against"]) / (max_gc - min_gc)* 100)

            #Calcula la resistencia en base a: puntos del equipo/(puntos del lider*100)
            #A mayor puntos mayor resistencia
            resistencia = int(fila["points"] / max_pts * 100)

            equipos.append({
                "id": str(fila["team"]["id"]),
                "nombre": fila["team"]["name"],
                "ranking": ranking,
                "ataque": ataque,
                "defensa": defensa,
                "resistencia": resistencia
            })
        return equipos