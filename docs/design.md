## Algoritmo
 
### Primera versión del programa

- Crear una lista u otra estructura de reguladores (sin repeticiones).

- Recorrer todas las interacciones (líneas).
 - Para cada interacción:
   - Obtener el TF.
   - Obtener el gen.
   - Si el TF no está guardado en la lista de reguladores, guardarlo.
   - Si el gen no está en la lista de genes vinculados a cada regulador, almacenarlo.

   - Recorrer toda la lista de reguladores (TF). Ellos deben estar ordenados.
     - Organizar de manera alfabética la lista de genes regulados por el TF.
     - Contar los elementos de aquella lista.
     - Imprimir el regulador, el susodicho conteo y la lista de genes.


## Segunda versión del programa (extensión)

- Crear una lista u otra estructura de reguladores (sin repeticiones).

- Recorrer todas las interacciones (líneas).
 - Para cada interacción:
   - Obtener el TF.
   - Obtener el gen.
   - Si el TF no está guardado en la lista de reguladores, guardarlo.
   - Si el gen no está en la lista de genes vinculados a cada regulador, almacenarlo junto con el efecto del TF sobre este gen.

   - Iterar sobre la lista de reguladores (TF). Ellos deben estar ordenados de forma alfabética. 
    - Por cada TF:
     - Inicializar en 0 tres contadores: total de genes regulados, genes activados y genes reprimidos. 
     - Analizar cada uno de los registros gen - efecto resguardados con anterioriadad:
       - A medida que se recorren esos binomios, el total de genes regulados va incrementándose una unidad.
       - Si el efecto solo corresponde a '+', aumentar el total de genes activados; si solo aparece '-' en ese parámetro, elevar el total de genes reprimidos. 
     - Interpretar los valores obtenidos: si ambos totales son mayores que uno, el TF tiene un efecto dual. En caso de que solo los genes activados rebasen a 0, el TF sería un activador; si el otro tipo de genes fuera el único total superior a 0, el TF sería un represor.
     - Imprimir 5 resultados: el nombre del TF, el número de genes regulados, el total de genes activados, la cantidad de genes reprimidos, y el tipo de efecto ejercido por el TF.
