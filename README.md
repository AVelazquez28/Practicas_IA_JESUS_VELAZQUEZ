# Clasificación con Árbol de Decisión — Wine Dataset

## Qué hace este proyecto
`modelo.py` carga el dataset de vinos de scikit-learn, separa los datos en
entrenamiento (80%) y prueba (20%), entrena un árbol de decisión con
`max_depth=2` y muestra la precisión y las reglas que aprendió.

`experimento_max_depth.py` corre el mismo proceso pero probando distintos
valores de `max_depth` (1, 2, 3, 4, 5, 6 y sin límite) para comparar cómo
cambia el árbol.

## Resultados obtenidos

| max_depth | profundidad real | hojas | precisión |
|-----------|------------------|-------|-----------|
| 1         | 1                | 2     | 0.6667    |
| 2         | 2                | 4     | 0.8611    |
| 3         | 3                | 6     | 0.9444    |
| 4         | 4                | 7     | 0.9444    |
| 5         | 4                | 7     | 0.9444    |
| 6         | 4                | 7     | 0.9444    |
| None      | 4                | 7     | 0.9444    |

### Sobre el cambio de max_depth
Con `max_depth=2` el árbol solo alcanza el 86.11% de precisión porque le
faltan divisiones: agrupa varios vinos distintos en la misma hoja. Al
subir a `max_depth=3` la precisión sube a 94.44% porque el árbol puede
hacer una pregunta más para separar casos que antes se confundían. De
ahí en adelante (4, 5, 6 e incluso sin límite) el árbol deja de crecer
por sí solo en la profundidad 4, con 7 hojas: no hay más separaciones
útiles que hacer con estos datos, así que aumentar el límite no cambia
nada. La profundidad máxima real que este árbol necesita es 4.

### Sobre entrenar sin límite (max_depth=None)
La diferencia es que el árbol ya no se detiene por una regla externa,
sino que crece hasta que cada hoja queda "pura" o hasta que ya no puede
dividir más un grupo. En este dataset ese punto natural es la
profundidad 4, exactamente igual que si se hubiera puesto
`max_depth=4` a mano. Las reglas que aparecen son las mismas, solo que
se generan sin que nosotros forcemos el tope. Esto muestra que el Wine
dataset es "fácil" de separar: no hace falta un árbol enorme para
clasificarlo bien.

## Evaluación de la precisión
El mejor resultado en los datos de prueba fue **94.44%** de precisión,
alcanzado desde `max_depth=3` en adelante. Con solo 2 niveles de
profundidad el modelo ya funciona razonablemente bien (86.11%), lo cual
confirma que unas pocas características (como `color_intensity`,
`proline` y `flavanoids`) ya cargan casi toda la información necesaria
para distinguir los tres tipos de vino.

## Opinión sobre los resultados
El modelo funciona muy bien con este dataset, y no hace falta un árbol
complicado para lograrlo: con 3 o 4 niveles ya se llega al máximo de
precisión posible aquí. Eso dice mucho más del dataset que del
algoritmo: son datos limpios, ya medidos en laboratorio y bien
diferenciados entre clases.

## ¿El dataset cumple los requisitos para usarse con un árbol de decisión?
**Sí.** Un árbol de decisión funciona bien cuando las clases se pueden
separar con cortes claros sobre variables numéricas, y eso es justo lo
que pasa aquí: variables como `color_intensity`, `flavanoids` y
`proline` marcan diferencias bastante nítidas entre los tres tipos de
vino, como se ve en las reglas generadas. Además el dataset no tiene
valores faltantes y las clases están razonablemente balanceadas, lo
cual también ayuda a que el árbol no se sesgue hacia un solo tipo de
vino.

### Características fundamentales
- **color_intensity**: es la primera pregunta que usa el árbol en
  todos los casos, así que es la que más separa a los vinos.
- **proline**: aparece varias veces y ayuda a distinguir entre los
  vinos que ya comparten un color de intensidad parecido.
- **flavanoids**: separa claramente uno de los tres tipos de vino
  (clase 2) del resto.

¿Agregaría otras características? Con la precisión ya en 94.44% no
haría falta más para este ejercicio, pero en un caso real sí valdría
la pena añadir datos como la región exacta del cultivo, el año de
cosecha o el tipo de suelo, ya que eso podría ayudar a distinguir
mejor entre subtipos dentro de una misma clase.
