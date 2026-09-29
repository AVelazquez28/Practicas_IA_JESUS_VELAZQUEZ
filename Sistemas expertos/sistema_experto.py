"""
Sistema experto de diagnostico medico simple.
Usa encadenamiento hacia adelante (forward chaining) con la libreria experta.
"""

from experta import KnowledgeEngine, Rule, NOT
from hechos import Sintoma, Diagnostico


class SistemaExperto(KnowledgeEngine):
    """Motor de inferencia con las reglas de diagnostico.

    Cada regla revisa una combinacion especifica de sintomas y, si se
    cumple, declara un hecho Diagnostico y muestra una recomendacion.
    La lista self.orden_de_activacion registra en que orden se disparo
    cada regla, para poder analizarlo despues (Ejercicio 2).
    """

    def __init__(self):
        super().__init__()
        self.orden_de_activacion = []

    # --- Reglas originales (Parte 2) ---------------------------------

    @Rule(Sintoma(fiebre=True, tos=True, dolor_garganta=True))
    def gripe(self):
        self.orden_de_activacion.append("Gripe")
        self.declare(Diagnostico(enfermedad="Gripe"))
        print("Diagnostico: Gripe")
        print("Recomendacion: reposo, hidratacion abundante y control de "
              "la fiebre con antipireticos; acudir a consulta si los "
              "sintomas empeoran o se prolongan mas de una semana.")

    @Rule(Sintoma(fiebre=True, dolor_cabeza=True, nauseas=True))
    def migrana(self):
        self.orden_de_activacion.append("Migrana")
        self.declare(Diagnostico(enfermedad="Migrana"))
        print("Diagnostico: Migrana")
        print("Recomendacion: descansar en un lugar oscuro y silencioso, "
              "evitar pantallas, y consultar a un medico si los episodios "
              "son frecuentes o muy intensos.")

    @Rule(Sintoma(estornudos=True, congestion_nasal=True, picazon_ojos=True))
    def alergia(self):
        self.orden_de_activacion.append("Alergia")
        self.declare(Diagnostico(enfermedad="Alergia"))
        print("Diagnostico: Alergia")
        print("Recomendacion: evitar el alergeno sospechoso, considerar un "
              "antihistaminico de venta libre y consultar a un alergologo "
              "si los sintomas son recurrentes.")

    @Rule(Sintoma(dolor_estomago=True, diarrea=True, vomito=True))
    def gastroenteritis(self):
        self.orden_de_activacion.append("Gastroenteritis")
        self.declare(Diagnostico(enfermedad="Gastroenteritis"))
        print("Diagnostico: Gastroenteritis")
        print("Recomendacion: mantener hidratacion con sales orales, dieta "
              "blanda, y buscar atencion medica si hay signos de "
              "deshidratacion o los sintomas duran mas de 2 dias.")

    # --- Reglas nuevas (Ejercicio 1) ----------------------------------

    @Rule(Sintoma(fiebre=True, tos_seca=True, perdida_olfato=True))
    def covid19(self):
        self.orden_de_activacion.append("COVID-19")
        self.declare(Diagnostico(enfermedad="COVID-19"))
        print("Diagnostico: COVID-19 (sospecha)")
        print("Recomendacion: aislarse, realizar una prueba especifica "
              "cuanto antes y contactar a un servicio de salud para "
              "confirmar el diagnostico y recibir indicaciones.")

    @Rule(Sintoma(congestion_nasal=True, estornudos=True, tos_leve=True))
    def resfriado_comun(self):
        self.orden_de_activacion.append("Resfriado comun")
        self.declare(Diagnostico(enfermedad="Resfriado comun"))
        print("Diagnostico: Resfriado comun")
        print("Recomendacion: reposo relativo, liquidos calientes y "
              "descongestionantes de venta libre; suele resolverse solo "
              "en 7 a 10 dias.")

    @Rule(Sintoma(tos_persistente=True, flema=True, dificultad_respiratoria=True))
    def bronquitis(self):
        self.orden_de_activacion.append("Bronquitis")
        self.declare(Diagnostico(enfermedad="Bronquitis"))
        print("Diagnostico: Bronquitis")
        print("Recomendacion: evitar irritantes como el humo, mantenerse "
              "hidratado y acudir al medico si la dificultad respiratoria "
              "aumenta o la fiebre persiste.")

    @Rule(Sintoma(fatiga=True, palidez=True, mareo=True))
    def anemia(self):
        self.orden_de_activacion.append("Anemia")
        self.declare(Diagnostico(enfermedad="Anemia"))
        print("Diagnostico: Anemia (sospecha)")
        print("Recomendacion: acudir a consulta para un analisis de "
              "sangre que confirme el diagnostico; puede requerir ajuste "
              "de dieta o suplementacion con hierro.")

    # --- Regla de respaldo ---------------------------------------------
    # salience=-1 hace que esta regla se evalue al final, despues de que
    # las demas reglas hayan tenido oportunidad de declarar un
    # Diagnostico. Si alguna lo declara, esta regla se desactiva sola
    # (mantenimiento de verdad de experta), y por eso no se dispara.

    @Rule(NOT(Diagnostico()), salience=-1)
    def sin_diagnostico(self):
        self.orden_de_activacion.append("Sin diagnostico")
        print("No se pudo determinar un diagnostico con los sintomas "
              "proporcionados. Se recomienda consultar a un medico.")
