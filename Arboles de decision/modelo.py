"""
Clasificacion con Arbol de Decision - Wine Dataset
Actividad: entrenar un arbol de decision, medir su precision
y ver como cambian las reglas segun la profundidad permitida.

Nota: los parametros como max_depth y random_state se dejan en
ingles porque son nombres fijos de la libreria scikit-learn, no
se pueden traducir. El resto de las variables si estan en espanol.
"""

from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. Cargar el dataset de vinos
vino = load_wine()
x, y = vino.data, vino.target

# 2. Separar en entrenamiento (80%) y prueba (20%)
x_entreno, x_prueba, y_entreno, y_prueba = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# 3. Entrenar el arbol con max_depth=2 (version base pedida en la guia)
arbol = DecisionTreeClassifier(max_depth=2, random_state=42)
arbol.fit(x_entreno, y_entreno)

# 4. Medir la precision contra los datos de prueba
prediccion = arbol.predict(x_prueba)
precision = accuracy_score(y_prueba, prediccion)
print(f"Precision del modelo (max_depth=2): {precision:.4f}")

# 5. Ver las reglas que aprendio el arbol
reglas = export_text(arbol, feature_names=list(vino.feature_names))
print("\nReglas del arbol:\n")
print(reglas)
