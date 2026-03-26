# Casos de prueba de la tercera versión del programa 

### 1. Archivo válido (caso feliz)

**Condición** 
  El archivo existe, se puede leer y contiene datos con el formato esperado.

**Qué se prueba**
 - Lectura línea por línea.
 - Limpieza básica.
 - Extracción de columnas correctas.
 - Construcción de interactions.

**Comportamiento esperado**
- El programa procesa el archivo sin errores.
- Construye correctamente la lista de interacciones.
- El resto del programa puede usar esa lista sin modificarse.
- Se genera el archivo de salida.

**Resultados**
- El programa no arrojó ningún error. 
- La lista de interacciones se contruye de manera apropiada.
- El programa, sin modificar su lógica subyacente, puede usar la lista.
- Se genera el archivo de salida.

Ejemplo del archivo generado:

```
TF	Total genes	Activados	Reprimidos	Tipo de efecto regulatorio	Lista de genes
ATP-dependent RNA helicase DeaD	3	3	0	Activador	mntR, sdiA, uvrY
AaeR	3	3	0	Activador	aaeA, aaeB, aaeX

```

<br>

### 2. Líneas de comentario

**Condición**
  El archivo contiene líneas que comienzan con '#'.

**Qué se prueba**
 - Que el programa distingue metadatos de datos reales.

**Comportamiento esperado**
- Esas líneas se ignoran completamente.
- No se intentan separar en columnas.
- No generan errores.


**Resultados**
- Las susodichas líneas se omiten y por ende no se fragmentan en columnas.
- No surge ningún error.

Para lograr lo anterior, se colocó esta validación:

```python
 if line.startswith('#'):
      continue 
```

El resultado se corrobora porque, tal como se esperaba, el siguiente comando no regresó ningún resultado:

```bash

 grep "#" results/regulon_summary.tsv
``` 

<br>

### 3. Encabezado presente

**Condición**
  El archivo contiene una línea con nombres de columnas.

**Qué se prueba**
 - Que el encabezado no se procese como una interacción

**Comportamiento esperado**
 - El encabezado se ignora y no aparece como parte de interactions.


**Resultados**
- El encabezado no se tomó en cuenta y por lo tanto no figura en el archvio final.

Para remover aquella línea, se usó esta validación:

```python
 if line.startswith('1)regulatorId'):
     continue 
```

El resultado se comprueba porque, al ejecutar este comando, la cadena seleccionada no apareció en el archivo.

```bash

 grep "regulatorId" results/regulon_summary.tsv
``` 

<br>

### 4. Línea vacía

**Condición**
  El archivo contiene una o más líneas vacías.

**Qué se prueba**
 - Limpieza de entrada.
 - Manejo de líneas sin contenido.

**Comportamiento esperado**
 - Las líneas vacías se ignoran y no provocan errores.
 - No agregan elementos incorrectos a interactions.


 **Resultados**
- Las líneas en blanco se omitieron en este análisis.
- Interactions no tiene ningún espacio vacío, lo cual se refleja en que todos los renglones del archivo de salida tienen la misma cantidad de columnas. 

Para quitar las líneas problemáticas, se recurrió a esta validación:

```python
 if not line:
        continue
```

El resultado se valida porque, al ejecutar este comando para buscar espacios en blanco, no se obtuvo ningún output:

```bash

 grep "^\s*$" results/regulon_summary.tsv
 ```


<br>

### 5. Valor inválido en effect

**Condición**
  Una fila tiene un valor distinto de '+', '-' o '+-' en la columna de efecto (es la número 5 si se empieza a contar desde 0).

**Qué se prueba**
 - Validación de contenido.

**Comportamiento esperado**
 - Esa fila no se incluye en interactions.
 - El programa continúa con el resto del archivo.

**Resultados**
- El análisis solo contempló las líneas que albergaran los caracteres mencionados.
- El programa siguió adelante con el resto del documento.

Para aislar las líneas correctas, se ocupó esta estrategia:

```python
 fields = line.split('\t') 
 effect = fields[5]
 if effect not in ('+', '-', '-+'):
    continue
```

El resultado se valida porque, al ejecutar el comando mostrado enseguida, se observan tres valores (que corresponden al significado biológico de '+', '-' y '-+'). Cabe destacar que el primer registro del documento se omitió porque en esa sección se especifica el tipo de información preservada en cada columna.

```bash

awk -F  "\t" 'NR>1{print $5}' results/regulon_summary.tsv | sort -u
```

```
Activador
Dual
Represor
```
<br>

### 6. Número insuficiente de columnas

**Condición**
  Una fila tiene menos columnas de las necesarias.

**Qué se prueba**
 - Validación de estructura antes de acceder a los índices.

**Comportamiento esperado**
 - Esa línea se descarta.
 - El programa no falla con IndexError.
 - Las demás líneas válidas siguen procesándose.

  *Ejemplo de línea problemática*

```
  AraC    araA 
```

**Resultados**

- Se descartaron los renglones cuyo total de columnas fuera inferior a la cantidad aceptable: 6. 
- El programa no arrojó ningún error y continuó procesando las restantes líneas válidas.

Para cortar las columnas, contarlas y verificar que fueran suficientes para este análisis, se empleó este código:

```python
 fields = line.split('\t') 

 if len(fields) < 6:
    continue
```



<br>

### 7. Archivo no existe

**Condición**
  La ruta del archivo es incorrecta o el archivo fue movido/eliminado.

**Qué se prueba**
 - Manejo de error al abrir archivo.

**Comportamiento esperado**
 - El programa muestra un mensaje claro. 
 - Termina de forma controlada. 
 - No sigue ejecutándose como si el archivo existiera.

  *Ejemplo esperado*

```
Error: archivo no encontrado data/raw/NetworkRegulatorGene.tsv
```
**Resultados**
- Se establece la ruta del archivo de entrada y, si él no existe allí, se muestra un mensaje al usuario. Además, gracias a sys.exit(1), el programa finaliza de manera controlada.

Lo anterior se logró mediante este fragmento de código:

```python
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)

# Información sobre el archivo de entrada.
data_dir = os.path.join(project_root, 'data', 'raw')
filename = os.path.join(data_dir, 'NetworkRegulatorGene.tsv')

try:
    with open(filename) as f:

# Si open(filename) no desencadenó ningún error, se comienza a construir interactions.

except FileNotFoundError:
    print(f'Error: archivo {filename} no encontrado')
    sys.exit(1)

```

<br>


### 8. Archivo sin permisos de lectura

**Condición**
  El archivo existe, pero el programa no tiene permisos para leerlo.

**Qué se prueba**
  - Manejo de errores de acceso.

**Comportamiento esperado**
  - Se informa claramente el problema.
  - El programa termina de forma controlada.


**Resultados**
- Se define la ruta del archivo de entrada y, en caso de que él esté allí pero no pueda ser leído, el usuario será alertado sobre esta situación; por añadidura, el problema terminará de forma controlada.

Ese resultado se alcanzó gracias a este fragmento de código:

```python
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)

# Información sobre el archivo de entrada.
data_dir = os.path.join(project_root, 'data', 'raw')
filename = os.path.join(data_dir, 'NetworkRegulatorGene.tsv')

try:
    with open(filename) as f:

# Si open(filename) no generó ningún error, se comienza a construir interactions.

except FileNotFoundError:
    print(f'Error: archivo {filename} no encontrado')
    sys.exit(1)

except PermissionError:
    print(f'Error: permiso denegado para leer el archivo {filename}')    
    sys.exit(1)    

```

<br>

### 9. Integración con el programa anterior

**Condición**
La lista interactions fue construida a partir del archivo.

**Qué se prueba**
 - Compatibilidad con el código previo

**Comportamiento esperado**
 - El programa anterior sigue funcionando sin cambios importantes.
 - Se obtienen estos datos: TF, total de genes regulados, número de genes activados, número de genes reprimidos, tipo general de regulación ejercida por el TF, y la lista de target genes.

**Resultados** 
- La lógica subyacente del programa no varió: con base en una lista de tuplas, la cual en este caso se creó a partir del archivo, se elaboró un diccionario cuyas keys eran los TFs y los valores, acomodados en una lista, eran los genes regulados (target genes).  
- También se preservó el ulterior cálculo de la longitud de dicha lista; ello elucidó el total de genes regulados por cada TF. Después, como se hacía en la versión pasada del programa, ellos se ordenaron de manera alfabética en una cadena.
- Aunado a lo anterior, se respetó el uso de contadores de genes activados y reprimidos. Estos valores numéricos se aprovecharon para clasificar el tipo de regulación documentada entre cada TF y sus target genes.

En ese sentido, la principal diferencia entre la versión previa del código y la presente actualización es la presencia de defaultdict, que proviene del módulo *collections* de Python y es un diccionario más elegante y robusto. Conforme se recorren las tuplas almacenadas en interactions, se revisa si cada TF ya forma parte del diccionario; en el escenario de que esa condición sea falsa, se crea un diccionario con 3 campos: la lista de nombres de los target genes, la cantidad de genes activados y el total de genes reprimidos. Esta información se recaba, organiza y complementa conforme el programa hace parsing sobre el archivo de entrada.

- Como se ilustra más abajo, el programa obtiene los seis datos solicitados:

```python

interactions = []

# Creación de tuplas que sintetizan las interacciones en la red regulatoria.
      interactions.append((TF, gene, effect))

regulon = defaultdict(lambda: {"genes": [],"activados": 0,"reprimidos": 0})
for TF, gene, effect in interactions:
    data = regulon[TF]
    data['genes'].append(gene)

    if effect == '+':
        data['activados'] += 1

    elif effect == '-':
        data['reprimidos'] += 1    

    # Se agregó esta línea para contabilizar los genes cuyo efecto es '-+', ya que el código inicial asumía que solo existían los efectos '+' y '-'.
    else:
        data['activados'] += 1
        data['reprimidos'] += 1 

# La información recopilada se plasma en el archivo de salida. Un tabulador separa cada dato. Se escribe la primera línea del documento.
with open(output_file, 'w') as outfile:
    outfile.write('TF\tTotal genes\tActivados\tReprimidos\tTipo de efecto regulatorio\tLista de genes\n')

    for TF in sorted(regulon):
        data = regulon[TF] # Primer dato: nombre del TF.

        genes = sorted(data["genes"]) 
        total = len(genes) # Segundo dato: total de target genes del TF.
        lista_genes = ', '.join(genes) # Tercer dato: nombres de dichos genes.
        activados = data["activados"] # Cuarto dato: cantidad de genes activados.
        reprimidos = data["reprimidos"] # Quinto dato: número de genes reprimidos.

        # Sexto dato: tipo de regulación del TF sobre sus target genes.
        if activados and reprimidos:
            efecto = 'Dual'

        elif activados and not reprimidos:
            efecto = 'Activador'
        else:
            efecto = 'Represor'

        outfile.write(f'{TF}\t{total}\t{activados}\t{reprimidos}\t{efecto}\t{lista_genes}\n')

```

<br>