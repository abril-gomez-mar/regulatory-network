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

<br>

### 7. Archivo no existe

**Condición**
  La ruta del archivo es incorrecta o el archivo fue movido/eliminado.

**Qué se prueba**
 - Manejo de error al abrir archivo.

**Comportamiento esperado**
 - El programa muestra un mensaje claro - termina de forma controlada - no sigue ejecutándose como si el archivo existiera

  *Ejemplo esperado*

```
Error: archivo no encontrado data/raw/NetworkRegulatorGene.tsv
```
**Resultados**

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

<br>

### 9. Integración con el programa anterior

**Condición**
La lista interactions fue construida a partir del archivo.

**Qué se prueba**
 - Compatibilidad con el código previo

**Comportamiento esperado**
 - El programa anterior sigue funcionando sin cambios importantes.
 - Se obtienen estos datos: TF, total de genes regulados, número de genes activados, número de genes reprimidos  y tipo general del TF.

**Resultados** 
# justificar que la lógica subyacente no varió: se siguió usando un diccionario (pero ahora se escogió uno más robusto y que asignaba etiquetas a cada value de cada key) (puntualizar el manejo de las keys preexistentes)
# regulon = defaultdict(lambda: {"genes": [],"activados": 0,"reprimidos": 0}) (enfatizar que se preservó el uso de contadores para estudiar los roles de cada TF)
# se continuó usando el efecto de interactions para determinar el tipo de efecto regulatorio de cada TF sobre sus tgs
# para imprimir el archivo, se revisaron de nuevo las keys ordenadas del diccionario y se ordenaron sus respectivas listas de tgs, cuya cardinalidad también se calculó y a partir de esas estructuras de datos se crearon strings.

además, los valores finales de genes activados y reprimidos fueron considerados para definir el tipo de efecto regulatorio de cada T sobre sus genes correspondientes.
   
    for TF in sorted(regulon):
        data = regulon[TF]

        genes = sorted(data["genes"])
        total = len(genes)
        lista_genes = ', '.join(genes)
        activados = data["activados"]
        reprimidos = data["reprimidos"]

        if activados and reprimidos:
            efecto = 'Dual'

        elif activados and not reprimidos:
            efecto = 'Activador'
        else:
            efecto = 'Represor'

for TF, gene, effect in interactions:
    if TF not in regulon:
        regulon[TF] = []
    regulon[TF].append(gene)

for TF in sorted(regulon):
    genes = sorted(regulon[TF])
    total = len(genes)
    lista_genes = ", ".join(genes)    
    print(TF, total, lista_genes)




for TF, gene, effect in interactions:
    if TF not in regulon:
        regulon[TF] = []
    regulon[TF].append(gene)
    regulon[TF].append((gene, effect))

for TF in sorted(regulon):
    genes = sorted(regulon[TF])
    total = len(genes)
    lista_genes = ", ".join(genes)    
    print(TF, total, lista_genes)
    total_genes = 0
  genes_activados = 0
    genes_reprimidos = 0
    for gene, effect in regulon[TF]:
        total_genes += 1

       
        if effect == '+':
            genes_activados += 1
        else:
            genes_reprimidos += 1    

    if genes_reprimidos and genes_activados:
        efecto = 'Dual'

    elif genes_activados and not genes_reprimidos:
        efecto = 'Activador'    

    else:
        efecto = 'Represor'    

    # Se imprime el nombre del TF, sus correspondientes totales (genes regulados, genes activados y genes reprimidos) y su tipo de efecto sobre los target genes.
    print(TF, total_genes, genes_activados, genes_reprimidos, efecto) 

    

<br>