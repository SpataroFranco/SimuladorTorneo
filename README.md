# Simulador de Torneo de Fútbol Concurrente

## Descripción General

Este proyecto consiste en un simulador de torneos de fútbol desarrollado en Python como **Trabajo Práctico Final Integrador de Laboratorio de Programación II**.

El sistema consume datos reales de equipos mediante la **Football API**, genera estadísticas para cada club y ejecuta un campeonato completo utilizando Programación Orientada a Objetos, herencia, polimorfismo, clases abstractas, decoradores, generadores, manejo de excepciones personalizadas y concurrencia mediante el patrón **Productor–Consumidor**.

El torneo se desarrolla bajo el sistema **Round Robin**, donde todos los equipos se enfrentan entre sí. Cada partido es simulado utilizando atributos estadísticos de los equipos y factores aleatorios que aportan variabilidad a los resultados.

---

## Objetivos

- Aplicar Programación Orientada a Objetos
- Implementar herencia y polimorfismo
- Utilizar clases abstractas
- Consumir datos desde APIs externas
- Implementar concurrencia mediante hilos
- Aplicar el patrón Productor–Consumidor
- Utilizar decoradores personalizados
- Implementar generadores mediante `yield`
- Exportar resultados a archivos CSV

---

## Tecnologías Utilizadas

- Python 3
- Requests
- Python Dotenv
- Threading
- Queue
- CSV
- UUID
- Football API (API-Sports)

---

## Arquitectura del Proyecto

### Modelos

#### `Equipo` *(Clase Abstracta)*

Representa un equipo genérico.

**Atributos:**
- ID
- Nombre
- Ranking
- Ataque
- Defensa
- Resistencia
- Victorias
- Empates
- Derrotas
- Goles a favor
- Goles en contra

**Métodos principales:**
- `calcular_potencia()`
- `guardar_victoria()`
- `guardar_empate()`
- `guardar_derrota()`
- `get_puntos()`
- `get_diferencia_gol()`

---

#### `EquipoProfesional`

Hereda de `Equipo`.

**Atributo adicional:**
- Nivel de entrenamiento

**La potencia se calcula utilizando:**
- Ataque
- Defensa
- Resistencia
- Nivel de entrenamiento
- Factor aleatorio ±10%

También puede entrenar para mejorar sus estadísticas.

---

#### `EquipoAmateur`

Hereda de `Equipo`.

**Atributo adicional:**
- Estado físico

**La potencia se calcula utilizando:**
- Ataque
- Defensa
- Resistencia
- Estado físico
- Factor aleatorio ±20%

También puede recuperar condición física.

---

#### `Partido`

Representa un encuentro entre dos equipos.

**Responsabilidades:**
- Simular el partido
- Calcular goles
- Aplicar ventaja de local
- Actualizar estadísticas
- Registrar victorias, derrotas y empates

---

#### `Torneo`

Administra toda la competición.

**Responsabilidades:**
- Registrar equipos
- Generar fechas mediante Round Robin
- Mostrar tabla de posiciones
- Determinar campeón
- Exportar resultados a CSV

---

### Lógica

#### `Simulador`

Responsable de ejecutar los partidos concurrentemente.

**Implementa:**
- Threads
- Queue
- Lock
- Patrón Productor–Consumidor

---

### Herramientas

#### `ApiFootball`

Obtiene información real de equipos desde Football API.

**Información obtenida:**
- Ranking
- Nombre
- Goles a favor
- Goles en contra
- Estadísticas generales

---

### Decoradores

Incluye decoradores para medir tiempos de ejecución.

```python
@medir_tiempo
```

---

### Excepciones Personalizadas

El proyecto implementa excepciones específicas para:

- API Key inexistente
- Nombre inválido
- Ataque fuera de rango
- Defensa fuera de rango
- Resistencia fuera de rango
- Cantidad inválida de equipos
- Estado físico inválido
- Nivel de entrenamiento inválido

---

### Generadores

Las fechas del torneo son producidas mediante un generador utilizando:

```python
yield fecha
```

Esto permite generar cada jornada bajo demanda sin almacenar todas las fechas simultáneamente.

---

### Patrón Productor–Consumidor

El simulador implementa el patrón Productor–Consumidor utilizando `Queue`.

#### Productor
Genera los partidos de cada fecha y los coloca en una cola compartida.
```python
producir_fecha()
```

#### Cola Compartida
Coordina el acceso entre productores y consumidores.
```python
Queue()
```

#### Consumidores
Varios hilos recuperan partidos de la cola y ejecutan la simulación.
```python
consumidor()
```

#### Sincronización
Se utiliza `Lock()` para proteger la lista compartida de resultados.

---

## Flujo de Ejecución

1. Se consulta Football API
2. Se crean equipos profesionales y amateurs
3. Se genera el calendario mediante Round Robin
4. El generador produce una fecha
5. El productor coloca los partidos en la cola
6. Los consumidores simulan los encuentros concurrentemente
7. Se actualizan estadísticas
8. Se muestra la tabla de posiciones
9. Se determina el campeón
10. Se exportan resultados a CSV

---

## Exportación de Resultados

Al finalizar el torneo se genera:

```
src/datos/tabla_final.csv
```

Conteniendo:

| Posición | Equipo | PJ | PG | PE | PP | Puntos | GF | GC | DG |
|----------|--------|----|----|----|----|--------|----|----|----|

---

## Configuración

Crear un archivo `.env` en la raíz del proyecto:

```env
API_FOOTBALL_KEY=TU_API_KEY
```
---
# Demostración online
[https://spatarofranco.github.io/SimuladorTorneo/]
---

## Ejecución

Instalar dependencias:

```bash
pip install requests python-dotenv
```

Ejecutar:

```bash
python src/main.py
```

---

## Conceptos de la Materia Aplicados

- Programación Orientada a Objetos
- Encapsulamiento
- Herencia
- Polimorfismo
- Clases Abstractas
- Decoradores
- Generadores
- Excepciones Personalizadas
- Consumo de APIs
- Threads
- Productor–Consumidor
- Sincronización con Lock
- Exportación CSV

---

## Autores

### Aira Nicholas, Mokorel Valentin, Spataro Franco

## - Trabajo Práctico Final Integrador

## - Laboratorio de Programacíon II

## - Universidad Nacional de San Martín
