from herramientas.excepciones import *
from models.equipo_profesional import EquipoProfesional
from models.equipo_amateur import EquipoAmateur

class Pruebas:
    @staticmethod
    def probar_nombre_vacio():
        try:
            equipo = EquipoProfesional(1,"",1,90,80,100,nivel_entrenamiento=50)
        except nombreEquipoError as e:
            print(e)

    @staticmethod
    def probar_ranking_invalido():
        try:
            equipo = EquipoProfesional(1,"Boca fc",-7,90,80,100,nivel_entrenamiento=50)
        except rankingError as e:
            print(e)
    
    @staticmethod
    def probar_ataque_invalido():
        try:
            equipo = EquipoProfesional(1,"Boca fc",7,-6,80,100,nivel_entrenamiento=50)
        except ataqueError as e:
            print(e)

    @staticmethod
    def probar_defensa_invalida():
        try:
            equipo = EquipoProfesional(1,"Boca fc",7,60,-80,100,nivel_entrenamiento=50)
        except defensaError as e:
            print(e)

    @staticmethod
    def probar_resistencia_invalida():
        try:
            equipo = EquipoProfesional(1,"Boca fc",7,60,80,-20,nivel_entrenamiento=50)
        except resistenciaError as e:
            print(e)

    @staticmethod
    def probar_nivel_entrenamiento_invalido():
        try:
            equipo = EquipoProfesional(1,"Boca fc",7,60,80,20,nivel_entrenamiento=-50)
        except nivelEntrenamientoError as e:
            print(e)

    @staticmethod
    def probar_estado_fisico_invalido():
        try:
            equipo = EquipoAmateur(1,"Chacarita FC",40,50,50,70,estado_fisico=-10)
        except estadoFisicoError as e:
            print(e)

    @staticmethod
    def ejecutar_pruebas():
        print("\n========== PRUEBAS METODOS DE EQUIPOS ==========")
        Pruebas.probar_nombre_vacio()
        Pruebas.probar_ranking_invalido()
        Pruebas.probar_ataque_invalido()
        Pruebas.probar_defensa_invalida()
        Pruebas.probar_resistencia_invalida()
        Pruebas.probar_nivel_entrenamiento_invalido()
        Pruebas.probar_estado_fisico_invalido()
        Pruebas.probar_entrenar_profesional()
        Pruebas.probar_recuperar_fisico_profesional()
        Pruebas.probar_recuperar_fisico_amateur()
        Pruebas.probar_desgastar_amateur()

    @staticmethod
    def probar_entrenar_profesional():
        equipo = EquipoProfesional(1,"Boca FC",7,60,70,80,nivel_entrenamiento=50)
        print(f"Antes -> Ataque: {equipo._ataque}, "
            f"Defensa: {equipo._defensa}, "
            f"Resistencia: {equipo._resistencia}, "
            f"Nivel entrenamiento: {equipo._nivel_entrenamiento}")

        equipo.entrenar()

        print(f"Después -> Ataque: {equipo._ataque}, "
            f"Defensa: {equipo._defensa}, "
            f"Resistencia: {equipo._resistencia}, "
            f"Nivel entrenamiento: {equipo._nivel_entrenamiento}")
    
    @staticmethod
    def probar_recuperar_fisico_profesional():
        print("\n--- Probar recuperar_fisico() profesional ---")

        equipo = EquipoProfesional(1,"River",5,70,75,90,nivel_entrenamiento=60)

        equipo._resistencia = 95

        print(f"Antes -> Resistencia: {equipo._resistencia}")

        equipo.recuperar_fisico()

        print(f"Después -> Resistencia: {equipo._resistencia}")

    @staticmethod
    def probar_recuperar_fisico_amateur():
        print("\n--- Probar recuperar_fisico() amateur ---")

        equipo = EquipoAmateur(1,"Chacarita",40,50, 50,70,estado_fisico=85)

        print(f"Antes -> Estado físico: {equipo._estado_fisico}")

        equipo.recuperar_fisico()

        print(f"Después -> Estado físico: {equipo._estado_fisico}")

    @staticmethod
    def probar_desgastar_amateur():
        print("\n--- Probar desgastar() amateur ---")

        equipo = EquipoAmateur(1,"Atlanta",35,55,50,70,estado_fisico=10)

        print(f"Antes -> Estado físico: {equipo._estado_fisico}")

        equipo.desgastar()

        print(f"Después -> Estado físico: {equipo._estado_fisico}")

if __name__ == "__main__":
    Pruebas.ejecutar_pruebas()