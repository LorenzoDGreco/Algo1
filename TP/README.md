# Trabajo práctico: Parte N°1.
Este repositorio está creado con fines educactivos para la Facultad de Ingeniería de Buenos Aires.

En este proyecto se trabajará en un juego: el [ahorcado](https://es.wikipedia.org/wiki/Ahorcado_(juego)).

---
## ESTRATEGIA Y MODALIDAD.
Para realizar este trabajo planteamos la necesidad de realizar encuentros virtuales.
La estrategía de desarrollo utilizada fue la creación de un grupo de [Discord](https://discord.com/): una plataforma centrada en la creación de salas virtuales en las cuales diferentes usuarios tienen la opción de unirse y a través de su micrófono, auriculares y cámara comunicarse con otros usuarios comentando y así también compartiendo la imagen de sus escritorios.

A través de esta plataforma decidimos la utilización de un [IDE](https://es.wikipedia.org/wiki/Entorno_de_desarrollo_integrado) en común: [VScode](https://code.visualstudio.com/). Esto nos ayudaría a resolver y unificar las dudas que irían saliendo acerca de su utilización, personalización, etc.
Dicho entorno nos proporcionaba diversos complementos, entre ellos el más significativo fue [LiveShare](https://visualstudio.microsoft.com/services/live-share/) una herramienta de colaboración de código en tiempo real que nos facilitó [programar entre pares](https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/pair-programming/), una estrategia de desarrollo ágil en la cual dos (o más) personas trabajan en el mismo código a la vez y poseen diferentes roles.

Finalmente, para estructurar el [control de versiones](https://developer.mozilla.org/es/docs/Learn/Tools_and_testing/GitHub) del proyecto, utilizamos dos herramientas para colaborar de formar organizada y no tener problemas de sobre escritura de código y evitar la pérdida de código.
Mientras que Git suministró el control de versiones, historial de cambios, etc; Github nos permitió alojar el código en un repositorio remoto.

Herramientas utilizadas:
- Discord
- IDE VSCode
- LiveShare
- Github
- Git


---
## AHORCADO: REGLAS.
Inicialmente, comenzaremos por mostrar tantos signos de preguntas como letras
componen la palabra a adivinar, y a continuación pediremos el ingreso de una letra.
Un jugador puede tener como máximo 7 desaciertos por palabra a adivinar, de tal
modo que el jugador ganará si adivinó la palabra y tuvo menos de 8 desaciertos, o
perderá si llegó al 8vo. desacierto.
En cada interacción se debe pedir al jugador el ingreso de una letra, si la letra se
encuentra en la palabra a adivinar, se debe mostrar en las posiciones que se
encuentra.
A continuación se debe solicitar el ingreso de otra letra. Si el jugador vuelve a
ingresar una “a”, debería recibir un mensaje de “Letra ya ingresada”.

Si la letra ingresada por el jugador es una letra inexistente en la palabra, entonces,
se debe sumar su desacierto y además mostrar a continuación de la cantidad la
cadena de las letras desacertadas.

La cantidad de desaciertos, deben mostrarse las letras que el jugador fue ingresando y que no forman parte de la palabra.
Los ingresos de letras deberían terminar ó porque se alcanzó la cantidad máxima de
desaciertos, ó porque el jugador adivinó la palabra.
También se debe poder abandonar el ingreso, si el usuario en lugar de ingresar una
letra, ingresa el valor “0”, ó la palabra “FIN”.
Se debe validar que el ingreso sea una letra, cualquier otro caracter o una mayor
cantidad de letras, debe ser no tenido en cuenta, advirtiendo el hecho, con el
mensaje “Ingreso Inválido”, y se debe volver a solicitar una letra.

---
## CONDICIONES DE ENTREGA.
1. Cada función que forma parte del código debe tener debajo de su firma, una
descripción corta de cuál es su objetivo y quien es el autor ó responsable de
dicha función.
2. El código correspondiente a la Parte 1, debe ser subido al campus. El nombre a
dar al archivo será TP1_NombreGrupo.py. Deberán reemplazar NombreGrupo,
por el nombre dado a su grupo. Si la entrega está compuesta por más de un
archivo .py, generar un .zip con todos los archivos .py, y nombrarlo de igual
modo, pero con extensión zip.
3. Deberán grabar 2 videos y subirlos a un canal de Youtube, ó a Google Drive.
El primer video, cada integrante del equipo, deberá contar mostrando el
código, qué parte estuvo bajo su responsabilidad y los puntos de solución dados,
que considere más relevantes. El video total no debe superar los 10 minutos.
Comenzar cada uno de los relatos, diciendo el nombre y apellido.
Las exposiciones se deben entender y ver claramente; y deben intentar que sean
homogéneas.
4. Deberán grabar un segundo video, en el que se muestre al menos una jugada
completa, y que contemple distintos casos que muestran que la aplicación
responde según lo esperado. Deberán ir relatando los eventos de la jugada. En
este caso el video puede estar realizado por 1 único integrante y no debe
superar los 10 minutos.