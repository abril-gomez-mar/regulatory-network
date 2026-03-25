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


## Tercera versión del programa (creación de la red a partir del archivo)

- Verificar que el archivo exista y pueda ser leído por el programa.
- Leer el archivo.
- Recorrer las líneas.
- Limpiar datos mediante la validación de las líneas. Primero se revisará que los renglones no estén en blanco. Luego, se verificará que no sean comentarios. Por último, se comprobará que cada línea tenga al menos 6 columnas, ya que al otear el archivo se observó que en algunos casos estaba vacía la hilera 'regulatorGeneName'.
- Prescindir del encabezado de cada columna, el cual solo puntualiza la clase de información albergada en cada hilera.
- Extraer información. Se usarán las columnas 2, 5 y 6, puesto que ellas proporcionan los nombres de los reguladores (TF), así como sus respectivos genes regulados (TG). También mencionan el tipo de efecto que cada TF ejerce sobre un TG.
- Construir las interacciones de la red. Se considerarán estos parámetros: nombre del TF, número de genes regulados, total de genes activados, cantidad de genes reprimidos, y tipo de efecto regulatorio del TF sobre sus respectivos target genes, cuyos nombres también se mencionan.
- Generar un archivo de salida.