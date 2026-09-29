"""
Ejecuta los casos de prueba de la Parte 3 y del Ejercicio 1.
Cada caso crea una NUEVA instancia del motor, la reinicia, declara los
sintomas correspondientes y corre el motor de inferencia.
"""

from experta import Fact
from sistema_experto import SistemaExperto
from hechos import Sintoma, Diagnostico


def ejecutar_caso(nombre_caso, sintomas):
    """Crea un motor nuevo, declara los sintomas dados y lo ejecuta."""
    print(f"\n{'=' * 60}")
    print(f"{nombre_caso}")
    print(f"Sintomas declarados: {sintomas}")
    print("-" * 60)

    motor = SistemaExperto()
    motor.reset()
    motor.declare(Sintoma(**sintomas))
    motor.run()

    diagnosticos = [
        hecho["enfermedad"]
        for hecho in motor.facts.values()
        if isinstance(hecho, Diagnostico)
    ]
    print(f"Diagnosticos generados: {diagnosticos or 'ninguno'}")
    print(f"Orden de activacion de reglas: {motor.orden_de_activacion}")
    return diagnosticos, motor.orden_de_activacion


if __name__ == "__main__":

    # --- Parte 3: casos de prueba originales -------------------------

    ejecutar_caso(
        "Caso 1: Gripe",
        {"fiebre": True, "tos": True, "dolor_garganta": True},
    )

    ejecutar_caso(
        "Caso 2: Alergia",
        {"estornudos": True, "congestion_nasal": True, "picazon_ojos": True},
    )

    ejecutar_caso(
        "Caso 3: Gastroenteritis",
        {"dolor_estomago": True, "diarrea": True, "vomito": True},
    )

    ejecutar_caso(
        "Caso 4: Sintomas sin regla definida",
        {"cansancio": True, "mareo": True},
    )

    # Nota sobre el Caso 5: la guia sugiere como ejemplo la combinacion
    # "fiebre, tos, dolor de garganta, estornudos y congestion nasal",
    # pero con las reglas tal como estan definidas eso solo activa
    # Gripe (Alergia necesita ademas picazon_ojos=True, que no esta en
    # esa combinacion). Para que el caso realmente active DOS reglas al
    # mismo tiempo, como pide el enunciado, se usa en su lugar una
    # combinacion que satisface Gripe y Migrana a la vez (ambas
    # comparten el sintoma fiebre).
    ejecutar_caso(
        "Caso 5: combinacion que activa mas de una regla (Gripe + Migrana)",
        {
            "fiebre": True,
            "tos": True,
            "dolor_garganta": True,
            "dolor_cabeza": True,
            "nauseas": True,
        },
    )

    # --- Ejercicio 1: probar las reglas nuevas ------------------------

    ejecutar_caso(
        "Ejercicio 1 - COVID-19",
        {"fiebre": True, "tos_seca": True, "perdida_olfato": True},
    )

    ejecutar_caso(
        "Ejercicio 1 - Resfriado comun",
        {"congestion_nasal": True, "estornudos": True, "tos_leve": True},
    )

    ejecutar_caso(
        "Ejercicio 1 - Bronquitis",
        {
            "tos_persistente": True,
            "flema": True,
            "dificultad_respiratoria": True,
        },
    )

    ejecutar_caso(
        "Ejercicio 1 - Anemia (enfermedad propuesta)",
        {"fatiga": True, "palidez": True, "mareo": True},
    )
