<<<<<<< HEAD
Análisis de red regulatoria. 

1. Ejecución del programa

Si el usuario está ubicado en la raíz del repositorio, debe colocarse la ruta relativa 'src/regulon_summary.py' antes de uv run.
También podría cambiarse de carpeta a src, y luego ejecutar uv run sobre el programa.


2. Formato del archivo de salida
Es un archivo TSV, así que está separado por tabuladores.

3. Descripción de la salida
El documento describe la red regulatoria transcripcional de E. coli. Entonces, cada renglón contiene las siguientes columnas (de izquierda a derecha): nombre del TF, número de genes regulados, total de genes activados, cantidad de genes reprimidos, y tipo de efecto regulatorio del TF sobre sus respectivos target genes, cuyos nombres también se mencionan.