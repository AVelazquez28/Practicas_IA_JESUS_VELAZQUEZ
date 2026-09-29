# Sistema Experto de Diagnóstico Médico (forward chaining)

## Qué es esto
Es una práctica de sistema experto basado en reglas, usando la librería
`experta` de Python. El sistema recibe los síntomas de un paciente y,
aplicando encadenamiento hacia adelante, determina cuál de varias
posibles enfermedades coincide con esos síntomas.

## Archivos
- `hechos.py` — define los dos tipos de hechos que usa el sistema:
  `Sintoma` (los síntomas presentes) y `Diagnostico` (el resultado).
- `sistema_experto.py` — el motor de inferencia (`SistemaExperto`), con
  8 reglas de diagnóstico (4 originales + 4 del Ejercicio 1) y una
  regla de respaldo para cuando ningún síntoma coincide.
- `casos_prueba.py` — corre los 5 casos de la Parte 3 y los 4 casos
  nuevos del Ejercicio 1.
- `ejercicio2_conflicto.py` — corre el caso del Ejercicio 2, donde se
  activan dos reglas (Gripe y Alergia) al mismo tiempo.
- `reflexion.md` — respuestas a las preguntas de reflexión.

## Cómo ejecutarlo

1. Instalar la librería (solo la primera vez):
   ```
   pip install experta
   ```
   Nota: `experta` requiere Python 3.8 o 3.9. En versiones más nuevas
   (3.10+) puede dar errores de compatibilidad con el módulo
   `collections`.

2. Correr los casos de prueba:
   ```
   python casos_prueba.py
   ```

3. Correr el análisis de conflicto de reglas:
   ```
   python ejercicio2_conflicto.py
   ```

## Enfermedades que reconoce el sistema
| Enfermedad | Síntomas requeridos |
|---|---|
| Gripe | fiebre, tos, dolor de garganta |
| Migraña | fiebre, dolor de cabeza, náuseas |
| Alergia | estornudos, congestión nasal, picazón en los ojos |
| Gastroenteritis | dolor de estómago, diarrea, vómito |
| COVID-19 | fiebre, tos seca, pérdida de olfato |
| Resfriado común | congestión nasal, estornudos, tos leve |
| Bronquitis | tos persistente, flema, dificultad respiratoria |
| Anemia (propuesta propia) | fatiga, palidez, mareo |

## Nota sobre el Caso 5
La guía sugiere probar con "fiebre, tos, dolor de garganta, estornudos
y congestión nasal" como ejemplo de síntomas que activan más de una
regla. Al revisar las reglas, esa combinación en realidad solo activa
Gripe, porque Alergia necesita también `picazon_ojos=True`, que no
está en esa lista. Por eso, en `casos_prueba.py` el Caso 5 usa una
combinación distinta (fiebre, tos, dolor de garganta, dolor de cabeza
y náuseas) que sí activa dos reglas de verdad: Gripe y Migraña.
