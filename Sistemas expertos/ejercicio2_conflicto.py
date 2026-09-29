"""
Ejercicio 2: Analisis de conflictos de reglas.

Se declara un conjunto de sintomas que activa simultaneamente Gripe Y
Alergia (las dos reglas que sugiere el enunciado), y se observa:
- cuantos diagnosticos se generan
- en que orden se disparan las reglas
- si ese orden coincide con el orden en que las reglas estan escritas
  dentro de la clase SistemaExperto (gripe, migrana, alergia,
  gastroenteritis, ...)
"""

from sistema_experto import SistemaExperto
from hechos import Sintoma, Diagnostico

motor = SistemaExperto()
motor.reset()

# Sintomas de Gripe (fiebre, tos, dolor_garganta) + sintomas de Alergia
# (estornudos, congestion_nasal, picazon_ojos) al mismo tiempo.
motor.declare(Sintoma(
    fiebre=True,
    tos=True,
    dolor_garganta=True,
    estornudos=True,
    congestion_nasal=True,
    picazon_ojos=True,
))

motor.run()

diagnosticos = [
    hecho["enfermedad"]
    for hecho in motor.facts.values()
    if isinstance(hecho, Diagnostico)
]

print("\n--- Resultado del analisis ---")
print(f"Cantidad de diagnosticos generados: {len(diagnosticos)}")
print(f"Diagnosticos: {diagnosticos}")
print(f"Orden real de activacion de las reglas: {motor.orden_de_activacion}")
print(
    "Orden en que las reglas estan escritas en la clase: "
    "['Gripe', 'Migrana', 'Alergia', 'Gastroenteritis', ...]"
)
print(
    "Compara las dos listas de arriba para responder si el orden de "
    "activacion coincide con el orden de definicion dentro de la clase."
)
