Programa de k-mers.
1. Descripción del problema
A partir de un conjunto de asociaciones TF - target gene en una red regulatoria, se desea crear tablas que mencionen esta información por cada TF: número y nombre de los genes que regula, cantidad de genes activados, total de genes reprimidos, y tipo de efecto del TF sobre sus TGs.

2. Objetivo del software
Esclarecer, dada una red regulatoria, las relaciones existentes entre los TFs y sus TGs.

3. Requisitos funcionales (de la versión final del programa)
- Leer una lista de interacciones regulatorias.
- Identificar los TFs únicos y almacenarlos en una estructura.
- Asociar a cada TF sus respectivos TGs.
- Ordenar los TFs y, por cada uno de ellos, almacenar el número de genes regulados y sus nombres, los cuales también deberán estar ordenados.
- Imprimir la información anterior.
- Más adelante, se debe determinar el número de interacciones activadoras y represoras de cada TF sobre sus genes.
- Establecer el tipo de efecto global de cada TF sobre sus genes.  
- Imprimir los datos previos.


4. Requisitos no funcionales
La red debe introducirse como una lista de tuplas.
El código debe ser legible y seguir convenciones básicas de estilo, según PEP-8.

5. Supuestos y limitaciones
Solo puede procesarse la red regulatoria si ella está introducida como una lista de tuplas con estas estructuras: nombre del TF, nombre del gen, tipo de efecto del TF.

6. Análisis del problema
Para facilitar el análisis, conviene usar un diccionario para estructurar las interacciones TF: target gene como keys: values.

7. Diseño de la solución

- Crear una lista u otra estructura de reguladores (sin repeticiones).

- Recorrer todas las interacciones (líneas).
 - Para cada interacción:
   - Obtener el TF.
   - Obtener el gen.
   - Si el TF no está guardado en la lista de reguladores, guardarlo.
   - Si el gen no está en la lista de genes vinculados a cada regulador, almacenarlo junto con el efecto del TF sobre este gen.
   - Por cada TF, señalar el número de genes que regula y sus nombres, mismos que deberán estar organizados.

   - Iterar sobre la lista de reguladores (TF). Ellos deben estar ordenados de forma alfabética. 
    - Por cada TF:
     - Inicializar en 0 tres contadores: total de genes regulados, genes activados y genes reprimidos. 
     - Analizar cada uno de los registros gen - efecto resguardados con anterioriadad:
       - A medida que se recorren esos binomios, el total de genes regulados va incrementándose una unidad.
       - Si el efecto solo corresponde a '+', aumentar el total de genes activados; si solo aparece '-' en ese parámetro, elevar el total de genes reprimidos. 
     - Interpretar los valores obtenidos: si ambos totales son mayores que uno, el TF tiene un efecto dual. En caso de que solo los genes activados rebasen a 0, el TF sería un activador; si el otro tipo de genes fuera el único total superior a 0, el TF sería un represor.
     - Imprimir 5 resultados: el nombre del TF, el número de genes regulados, el total de genes activados, la cantidad de genes reprimidos, y el tipo de efecto ejercido por el TF.
