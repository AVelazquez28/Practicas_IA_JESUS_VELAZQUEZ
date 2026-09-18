"""
Comparacion de distintos valores de max_depth, incluyendo
el caso sin limite (max_depth=None). Esto sirve para la
actividad 2 y 3 de la guia (que responden con un parrafo
basandose en estos resultados).
"""

from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

vino = load_wine()
x, y = vino.data, vino.target
x_entreno, x_prueba, y_entreno, y_prueba = train_test_split(
    x, y, test_size=0.2, random_state=42
)

for profundidad in [1, 2, 3, 4, 5, 6, None]:
    arbol = DecisionTreeClassifier(max_depth=profundidad, random_state=42)
    arbol.fit(x_entreno, y_entreno)
    prediccion = arbol.predict(x_prueba)
    precision = accuracy_score(y_prueba, prediccion)
    print(
        f"max_depth={str(profundidad):<5} -> "
        f"profundidad real={arbol.get_depth():<3} "
        f"hojas={arbol.get_n_leaves():<3} "
        f"precision={precision:.4f}"
    )
