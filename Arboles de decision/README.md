# Práctica: Árbol de Decisión con el Wine Dataset

## De qué trata
Para esta práctica usé el dataset de vinos que ya viene incluido en
scikit-learn (`load_wine`). Tiene 178 vinos con 13 características
químicas cada uno (alcohol, ácido málico, flavonoides, etc.) y están
clasificados en 3 tipos según la región donde se cultivaron.

El objetivo era entrenar un árbol de decisión que aprendiera a
clasificar el tipo de vino a partir de esas características, y luego
ver qué tanto cambia el modelo si le doy más o menos "libertad" para
hacer preguntas (max_depth).

## Qué hice
1. Cargué el dataset y lo dividí en 80% para entrenar y 20% para
   probar el modelo con datos que nunca vio.
2. Entrené un primer árbol con `max_depth=2` (o sea, solo dejándolo
   hacer 2 preguntas seguidas como máximo).
3. Medí qué tan bien clasificó los vinos de prueba.
4. Repetí el entrenamiento probando distintos valores de max_depth
   (1, 2, 3, 4, 5, 6 y sin límite) para comparar.

## Resultados

| max_depth | profundidad real | hojas | precisión |
|-----------|------------------|-------|-----------|
| 1         | 1                | 2     | 66.67%    |
| 2         | 2                | 4     | 86.11%    |
| 3         | 3                | 6     | 94.44%    |
| 4         | 4                | 7     | 94.44%    |
| 5         | 4                | 7     | 94.44%    |
| 6         | 4                | 7     | 94.44%    |
| Sin límite| 4                | 7     | 94.44%    |

Con `max_depth=2` el árbol apenas alcanza el 86.11% de precisión,
porque le faltan preguntas para separar bien los casos más difíciles.
Al dejarlo llegar a 3 niveles sube a 94.44%, que fue lo máximo que se
pudo sacar. De ahí para arriba (4, 5, 6, o sin poner límite) ya no
mejora nada, porque el árbol se detiene solo en la profundidad 4:
ya no encuentra más divisiones que le sirvan.

## Qué pasó al entrenar sin límite (max_depth=None)
Pensé que sin límite el árbol iba a crecer muchísimo más, pero no fue
así. Llegó exactamente a la misma profundidad (4) y sacó la misma
precisión que si le hubiera puesto `max_depth=4` a mano. Lo que
entendí de esto es que el árbol no crece "porque sí" hasta el
infinito, se detiene solo cuando ya no hay forma de separar mejor los
datos que le quedan. Esto también me dice que el dataset de vinos es
bastante "fácil" de clasificar, no hace falta un árbol gigante.

## Mi opinión sobre los resultados
Me pareció que el modelo funcionó bien desde muy pocos niveles de
profundidad, lo cual creo que se debe más a que el dataset está muy
bien organizado (sin datos faltantes, y con clases que sí se
diferencian bastante entre sí) que a que el algoritmo sea
especialmente poderoso. Con solo 3 niveles ya se logra casi el
máximo posible.

## ¿El dataset sirve para usarse con un árbol de decisión?
Yo creo que sí. Un árbol de decisión funciona mejor cuando hay
variables numéricas que marcan diferencias claras entre las clases,
y en este caso eso se cumple: variables como `color_intensity`,
`proline` y `flavanoids` separan bastante bien los tres tipos de
vino, como se ve en las reglas que generó el árbol. Además no hay
datos faltantes y las tres clases tienen una cantidad razonable de
ejemplos cada una, así que no está sesgado hacia un solo tipo.

**Características que me parecieron más importantes:**
- `color_intensity`: es la primera pregunta que usa el árbol siempre,
  así que es la que más ayuda a separar.
- `proline`: aparece varias veces para distinguir vinos que ya se
  parecen en color.
- `flavanoids`: separa muy bien uno de los tres tipos de vino del
  resto.

¿Agregaría más características? Con 94.44% de precisión ya no creo
que hiciera falta para esta práctica, pero si fuera un caso real sí
podría ayudar agregar cosas como la región exacta del cultivo o el
año de cosecha, para distinguir mejor entre vinos muy parecidos.
