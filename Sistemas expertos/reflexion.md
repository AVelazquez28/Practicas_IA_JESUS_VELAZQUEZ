# Preguntas de reflexión

## 1. ¿Qué limitaciones observé en este enfoque?

Lo primero que noté es que las reglas son muy rígidas: tienen que
coincidir exactamente. Si al paciente le falta uno solo de los tres
síntomas que pide una regla, esa regla simplemente no se activa, sin
importar que el resto se parezca muchísimo a esa enfermedad. Tampoco
hay manera de decir "un poco de fiebre" o "dolor de cabeza fuerte";
todo es sí o no.

También me di cuenta de que el sistema depende completamente de lo
que uno haya programado de antemano. Si aparece una enfermedad que no
está en las reglas, el programa no la va a "adivinar" por más lógica
que tenga el patrón de síntomas, simplemente cae en la regla de
respaldo diciendo que no sabe. Y con solo 8 reglas ya se siente que
hay que estar pendiente de todas al escribir cada una; me imagino que
un sistema real con cientos de enfermedades sería bastante más difícil
de mantener a mano. Otra cosa que me pareció importante: el sistema no
aprende nada, siempre va a hacer exactamente lo que digan las reglas,
ni más ni menos.

## 2. ¿Cómo podría manejarse la incertidumbre en los síntomas?

Creo que una forma sería no usar solo `True` o `False`, sino un número
que diga qué tan seguro se está de que el síntoma está presente, por
ejemplo del 0 al 1 (algo así como un "70% seguro de que tiene fiebre").
Las reglas entonces podrían combinar esos porcentajes para dar una
certeza total del diagnóstico, en vez de una respuesta tajante.

También existe algo llamado lógica difusa, que funciona parecido:
en vez de "fiebre: sí/no" se maneja algo como "fiebre: 0.7", para que
el sistema pueda trabajar con síntomas que no están completamente
claros. Y otra opción sería usar probabilidades (como las redes
bayesianas), calculando qué tan probable es cada enfermedad según los
síntomas que sí se confirmaron, aunque no se tenga el cuadro completo.

## 3. En el Ejercicio 2, ¿qué implicaciones tiene que se activen varias reglas a la vez?

### Lo que observé al correrlo

Con los síntomas de Gripe y Alergia declarados juntos, el sistema
generó los dos diagnósticos: primero se disparó Gripe y después
Alergia. Eso en principio coincidió con el orden en que escribí las
reglas en la clase (gripe está antes que alergia en el código).

Pero antes, en el Caso 5, había pasado algo distinto: con Gripe y
Migraña activadas juntas, se disparó primero Migraña y después Gripe,
aunque en el código gripe está escrita antes que migrana. Entonces
comparando los dos casos, me di cuenta de que el orden en que se
disparan las reglas no siempre es el mismo en que las escribí. A veces
coincidió y a veces no, así que no es algo en lo que se pueda confiar
solo por cómo se acomodó el código.

### Por qué esto importa

Pienso que en un sistema experto de verdad (por ejemplo uno médico de
verdad) esto podría ser un problema serio. Si el sistema solo mostrara
el primer diagnóstico que se le ocurrió activar, sin ningún criterio
claro detrás, alguien podría terminar creyendo que tiene una
enfermedad menos urgente cuando en realidad también aplicaba otra más
grave, nada más porque esa regla se disparó después.

Por eso creo que un sistema real necesitaría alguna forma de decidir
qué diagnóstico priorizar, y no dejarlo al azar del orden interno.
Algunas ideas:

- Ponerle una prioridad a cada regla (algo como el `salience` que usé
  en la regla de respaldo), para que las enfermedades más urgentes se
  revisen primero.
- Que el sistema le pregunte algo más al usuario para desempatar entre
  los posibles diagnósticos, en vez de quedarse con el que salió
  primero.
- Mostrar todos los diagnósticos posibles a la vez, en vez de
  quedarse solo con uno, para que sea la persona (o un médico) quien
  decida.
