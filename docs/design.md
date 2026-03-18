## Algoritmo
 
### Primera versión del programa

- Crear una lista u otra estructura de reguladores (sin repeticiones).

- Recorrer todas las interacciones (líneas).
 - Para cada interacción:
   - Obtener el TF.
   - Obtener el gen.
   - Si el TF no está guardado en la lista de reguladores, guardarlo.
   - Si el gen no está en la lista de genes vinculados a cada regulador, almacenarlo.

   - Recorrer toda la lista de reguladores (TF).
     - Contar los elementos de la lista de genes regulados por el TF.
     - Imprimir el regulador, el susodicho conteo y la lista de genes.
