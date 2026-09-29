"""
Definicion de los tipos de hechos (Fact) que usa el sistema experto.
"""

from experta import Fact


class Sintoma(Fact):
    """Representa los sintomas presentes en el paciente.
    Se instancia con uno o mas atributos booleanos, por ejemplo:
    Sintoma(fiebre=True, tos=True, dolor_garganta=True)
    Cada atributo indica si ese sintoma especifico esta presente (True).
    """
    pass


class Diagnostico(Fact):
    """Representa un diagnostico generado por el sistema.
    Almacena el nombre de la enfermedad identificada en el atributo
    'enfermedad', por ejemplo: Diagnostico(enfermedad="Gripe")
    """
    pass
