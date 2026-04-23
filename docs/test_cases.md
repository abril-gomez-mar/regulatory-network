# Casos de prueba

## Primera versión del programa

### Caso 1

- Entrada:

```
interactions = [
    ("AraC", "araA", "+"),
    ("AraC", "araB", "-"),
    ("LexA", "recA", "-")
]
```

- Salida esperada:

| TF  |  Total de genes  | Lista de genes | 
|---|---|---|
| AraC  |  2 |  araA, araB |  
| LexA | 1  | recA |


- Resultados:
```
AraC 2 araA, araB
LexA 1 recA

```

¿Coinciden con la salida esperada? Sí.

<br>

### Caso 2

- Entrada:

```
interactions = [
    ("CRP", "lacZ", "+"),
    ("CRP", "lacY", "+"),
    ("CRP", "lacA", "+")
]
```

- Salida esperada:

| TF  |  Total de genes  | Lista de genes | 
|---|---|---|
| CRP  |  3 |  lacA, lacY, lacZ |  

- Resultados:
```
CRP 3 lacA, lacY, lacZ
```


¿Coinciden con la salida esperada? Sí.

<br>

### Caso 3

- Entrada:

```
interactions = [
    ("LexA", "recA", "-"),
    ("LexA", "umuC", "-"),
    ("AraC", "araE", "+"),
    ("AraC", "araA", "-")
]

```

- Salida esperada:

| TF  |  Total de genes  | Lista de genes | 
|---|---|---|
| AraC | 2 | araA, araE |  
| LexA | 2 | recA, umuC|

- Resultados:
```
AraC 2 araA, araE
LexA 2 recA, umuC
```


¿Coinciden con la salida esperada? Sí.

<br>

### Caso adicional mencionado al final de la clase

-Entrada:

```
interactions = [
    ("AraC", "araA", "+"),
    ("AraC", "araB", "-"),
    ("LexA", "recA", "-"),
    ("CRP", "lacZ", "+"),
    ("CRP", "lacY", "+")
]

```

- Salida esperada:

| TF  |  Total de genes  | Lista de genes | 
|---|---|---|
| AraC |  2 |  araA, araB |  
|  CRP |  2  | lacY, lacZ |
| LexA |  1 | recA |  

- Resultados:
```
AraC 2 araA, araB
CRP 2 lacY, lacZ
LexA 1 recA
```

¿Coinciden con la salida esperada? Sí.

<br>

## Segunda versión del programa (extensión)

Dado que se preservaron las dos versiones del código, se mostrarán los resultados completos al examinar cada caso de prueba.

### Primer caso

- Entrada:

```
interactions = [
    ("AraC", "araA", "+"),
    ("AraC", "araB", "-"),
    ("LexA", "recA", "-")
]
```

- Salida esperada:

| TF  |  Total de genes  | Genes activados | Genes reprimidos | Tipo de efecto | 
|---|---|---|---|---|
| AraC  | 2 | 1 | 1| Dual |  
| LexA | 1  | 0 | 1 | Represor |


- Resultados:
```
AraC 2 araA, araB
LexA 1 recA


AraC 2 1 1 Dual
LexA 1 0 1 Represor
```

¿Coinciden con la salida esperada? Sí.

<br>

### Segundo caso

- Entrada:

```
interactions = [
    ("CRP", "lacZ", "+"),
    ("CRP", "lacY", "+"),
    ("CRP", "lacA", "+")
]
```

- Salida extra esperada:

| TF  |  Total de genes  | Genes activados | Genes reprimidos | Tipo de efecto | 
|---|---|---|---|---|
| CRP  |  3 | 3 | 0 | Activador |  

- Resultados:
```
CRP 3 lacA, lacY, lacZ


CRP 3 3 0 Activador
```


¿Coinciden con la salida esperada? Sí.

<br>


### Tercer caso

- Entrada:

```
interactions = [
    ("LexA", "recA", "-"),
    ("LexA", "umuC", "-"),
    ("AraC", "araE", "+"),
    ("AraC", "araA", "-")
]

```

- Salida adicional esperada:

| TF  |  Total de genes  | Genes activados | Genes reprimidos | Tipo de efecto | 
|---|---|---|
| AraC | 2 | 1 | 1 | Dual |  
| LexA | 2 | 0 | 2 | Represor |

- Resultados:
```
AraC 2 araA, araE
LexA 2 recA, umuC


AraC 2 1 1 Dual
LexA 2 0 2 Represor
```


¿Coinciden con la salida esperada? Sí.

<br>

### Caso adicional

-Entrada:

```
interactions = [
    ("AraC", "araA", "+"),
    ("AraC", "araB", "-"),
    ("LexA", "recA", "-"),
    ("CRP", "lacZ", "+"),
    ("CRP", "lacY", "+")
]

```

- Salida adicional esperada:

| TF  |  Total de genes  | Genes activados | Genes reprimidos | Tipo de efecto | 
|---|---|---|---|---|
| AraC |  2 |  1 | 1 |  Dual |  
|  CRP |  2  | 2 | 0 | Activador |
| LexA |  1 | 0 | 1 | Represor |  

- Resultados:
```
AraC 2 araA, araB
CRP 2 lacY, lacZ
LexA 1 recA


AraC 2 1 1 Dual
CRP 2 2 0 Activador
LexA 1 0 1 Represor
```

¿Coinciden con la salida esperada? Sí.


## Command Line Interface (CLI)
# reminder: merge tests file with this one (one commit; explain logic to renconciliate names)

Caso: Correr el programa con paso de argumentos.

Entrada:

```bash

uv run python regulon_summary.py input.txt output.txt
uv run python regulon_summary.py NetworkRregulatorGene.tsv tf_summary.tsv

```

Resultado
El programa lee el archivo de entrada y genera el resultado con el nombre que se le pasó como argumento. 

<br>

## CLI — Filtro por número de genes

### Caso: uso de --min_genes.

Entrada:

```bash

python script.py input.tsv output.tsv --min_genes 2

```

Resultado esperado:

- Solo se incluyen TFs con al menos 2 genes.
- El archivo de salida refleja el filtrado correctamente.


**Resultados**

Para correr el programa, se utilizó esta instrucción:

```bash

uv run python .\src\regulon_summary.py .\data\raw\NetworkRegulatorGene.tsv results/output.tsv --min_genes 2
```

Luego, se ejecutó la siguiente línea para remover el encabezado del archivo de salida y aislar la columna 2 de ese documento (la cual muestra el número de genes regulados por cada TF). A continuación, se identificaron los valores únicos, se ordenaron de manera ascendente y se tomaron los cinco primeros resultados.

```bash

 awk -F '\t' 'NR>1{print $2}' results/output.tsv | sort -u | sort -n | head -5

```

Se obtuvieron estos valores:

´´´
2
3
4
5
6
´´´

Se demuestra que, tal como se pretendía, en el archivo no hay ningún TF que regule menos de dos genes, que fue el número especificado por el usuario mediante el argumento opcional *--min_genes*.

<br>

##  Manejo de errores

Enseguida se mostrarán los casos de prueba relacionados con alguna de las fallas que podrían presentarse al correr el programa. 

1. Equivocaciones relacionadas con la lectura del archivo de entrada

### Archivo inexistente (FileNotFoundError)

Entrada:

```bash

uv run python .\src\regulon_summary.py .\data\raw\documento.txt results/output.tsv --min_genes 2
```

Resultado esperado:
- Se imprime un mensaje de error.
- El programa termina de manera ordenada. 


**Resultados**

```
Error: el archivo de entrada no existe. Por favor, revise la ruta proporcionada e intente de nuevo.
```

¿Coinciden con la salida esperada? Sí.

<br>

### Falta de permisos (PermissionError)

Entrada (se intentó usar chmod 000 para bloquear el archivo, pero ese comando no funcionó):

```bash
touch data/bloqueado.tsv
```

```PowerShell
icacls .\data\bloqueado.tsv /deny --% %USERNAME%:(W)
```

```bash
uv run python .\src\regulon_summary.py .\data\bloqueado.tsv results/output.tsv --min_genes 2

```

Resultado esperado:
- Se arroja un mensaje para indicar que el usuario no puede leer el archivo.
- El programa finaliza de forma ordenada. 


**Resultados**

```
Error: no se puede acceder al archivo de entrada, ya que usted no tiene permisos de lectura.
```

¿Coinciden con la salida esperada? Sí.

<br>

### Ruta inválida (OSError)

Entrada:

```bash
uv run python .\src\regulon_summary.py .\data\fake\NetworkRegulatorGene.tsv  results/output.tsv --min_genes 2

```

Resultado esperado:
- Se imprime un mensaje para informar al usuario de que la ruta introducida no existe.
- El programa acaba de manera ordenada. 


**Resultados**

```
Error: la ruta especificada es errónea. Por favor, revise lo que tecleó e intente de nuevo.
```

¿Coinciden con la salida esperada? Sí.

<br>

### Errores al abrir o leer el archivo  (IOError, OSError)

Entrada:

```bash

mkdir data/raw/lost.tsv # Se crea un repositorio que, por error, fue nombrado como si fuera un archivo separado por tabuladores.

uv run python .\src\regulon_summary.py .\data\raw\lost.tsv results/output.tsv --min_genes 2 # El argumento posicional del archivo de entrada es erróneo y no se puede abrir o leer el documento. 

```

Resultado esperado:
- Se manda un mensaje para indicar que el archivo no puede abrirse.
- El programa finaliza de manera ordenada. 


**Resultados**

```
Error: la ruta especificada es un directorio, no un archivo. Por favor, revise la ruta proporcionada e intente de nuevo.
```

¿Coinciden con la salida esperada? Sí.

<br>

2. Errores asociados a la escritura del documento de salida 

### Rutas inválidas (OSError)

Entrada:

```bash
touch fake # Se crea un archivo, no un directorio. 

uv run python .\src\regulon_summary.py .\data\raw\NetworkRegulatorGene.tsv fake/output.tsv --min_genes 2

```

Resultado esperado:
- Se envía un mensaje para indicar que la ruta seleccionada no puede usarse.  
- El programa termina de manera ordenada. 

**Resultados**

```
Error al intentar escribir el archivo de salida. Ocurrió un error en el sistema operativo: [Errno 2] No such file or directory: 'C:\\Users\\cecil\\python_2026\\regulatory-network\\fake\\output.tsv'
```

¿Coinciden con la salida esperada? Sí.

<br>

### Carpetas inexistentes (FileNotFoundError)

Entrada:

```bash
uv run python .\src\regulon_summary.py .\data\raw\NetworkRegulatorGene.tsv salidas/output.tsv --min_genes 2

```

Resultado esperado:
- Se indica que la carpeta no existe.
- El programa finaliza de forma ordenada. 

**Resultados**

```
El directorio del archivo de salida no existe. Recuerde que debe emplear la carpeta 'results' para almacenar aquel archivo.
```

¿Coinciden con la salida esperada? Sí.

<br>

### Falta de permisos (PermissionError)


Entrada:

```bash
mkdir salida_bloqueada
```

```PowerShell
icacls salida_bloqueada /deny --% %USERNAME%:(W) 
```

```bash
uv run python .\src\regulon_summary.py .\data\raw\NetworkRegulatorGene.tsv salida_bloqueada/output.tsv --min_genes 2
```

Resultado esperado:
- Se comunica al usuario que no cuenta con el permiso de escribir el archivo de salida.
- El programa termina de manera organizada. 

**Resultados**

```
Error al intentar escribir el archivo de salida. Ocurrió un error en el sistema operativo: [Errno 13] Permission denied: 'C:\\Users\\cecil\\python_2026\\regulatory-network\\salida_bloqueada\\output.tsv'
```

¿Coinciden con la salida esperada? Sí.

<br>

### Errores al escribir el archivo (IOError, OSError)

Entrada:

```bash
uv run python .\src\regulon_summary.py .\data\raw\NetworkRegulatorGene.tsv results --min_genes 2 # No se indica el nombre del archivo de salida. 
```

Resultado esperado:
- Se imprime un mensaje que detalla el error encontrado.
- El programa acaba de forma ordenada.


**Resultados**

```
La ruta del archivo de salida es inválida, ya que no menciona el nombre del documento. Por favor, revise los datos proporcionados e intente de nuevo.
```
¿Coinciden con la salida esperada? Sí.

<br>

3. Validaciones adicionales 

### Líneas mal formadas en el archivo (ValueError)

Entrada:

```bash
touch data/raw/lineas_formato_err.tsv
nano data/raw/lineas_formato_err.tsv
```

Este será el contenido de ese archivo (son líneas modificadas del archivo original de entrada). Se aprecia que, para separar las columnas, se usan espaciadores en vez de tabuladores; por ello, puede aseverarse que las líneas no tienen la forma correcta:

```
RDBECOLIPDC00031 AcnB acnB RDBECOLIGNC02188	acnB + W 
RDBECOLIPDC00328 DicF dicF RDBECOLIGNC00341	ftsZ - S 
RDBECOLIPDC00328 DicF dicF RDBECOLIGNC00559	manX - S 
RDBECOLIPDC00328 DicF dicF RDBECOLIGNC00793	pykA - S 
RDBECOLIPDC00328 DicF dicF RDBECOLIGNC02444	xylR - S 

```

```bash
uv run python .\src\regulon_summary.py .\data\raw\lineas_formato_err.tsv results/filtered_output.tsv --min_genes 2
```


Resultados esperados:
- El usuario recibe un mensaje indicando que las líneas no tienen el formato apropiado.
- El programa termina de manera ordenada. 

**Resultados**


<br>

### Número incorrecto de columnas (validación manual)

Decisión: Solo se añadirá un mensaje para informarle al usuario que el archivo de entrada tiene menos columnas que las requeridas para construir interactions. Se llegó a esa resolución porque ya existe este fragmento en el programa:

```python
fields = line.split('\t') 

# Validación del número mínimo de columnas requeridas para procesar la información. 
    if len(fields) < 6:
        continue
```

Resultados esperados:
- El usuario recibe un mensaje si en algún momento el documento de entrada no cumple con el número mínimo de columnas para hacer el análisis (6, numerando desde el 0).

**Resultados**

<br>

### Valores inesperados en los campos (ValueError)

Entrada:

```bash
touch data/raw/lineas_raras.tsv
nano data/raw/lineas_raras.tsv
```

Este será el contenido de ese archivo (son líneas modificadas del archivo original de entrada). Se vislumbra que en el campo donde están los nombres de los factores de transcripción (la segunda columna) hay números, que representan caracteres anómalos. 

```
RDBECOLIPDC00031	Acn77B	acnB	RDBECOLIGNC02188	acnB	+	W 
RDBECOLIPDC00328	DicF	dicF	RDBECOLIGNC00341	ftsZ	-	S 
RDBECOLIPDC00328	Di55cF	dicF	RDBECOLIGNC00559	manX	-	S 
RDBECOLIPDC00328	Di9cF	dicF	RDBECOLIGNC00793	pykA	-	S 
RDBECOLIPDC00328	Di0cF	dicF	RDBECOLIGNC02444	xylR	-	S 

```

```bash
uv run python .\src\regulon_summary.py .\data\raw\lineas_raras.tsv results/filtered_output.tsv --min_genes 2
```


Resultados esperados:
- El usuario recibe un mensaje indicando que se identificaron valores inesperados en los campos. 
- El programa termina de manera ordenada. 

**Resultados**


<br>

### Argumento --min_genes negativo o inválido (ValueError)

Entrada:

```bash
uv run python .\src\regulon_summary.py .\data\raw\NetworkRegulatorGene.tsv results/filtered_output.tsv --min_genes -5
```

Resultados esperados:
- El usuario recibe un mensaje indicando que el valor de min_genes no puede ser negativo.
- El programa termina de manera ordenada. 

**Resultados**

<br>

### Argumentos incorrectos (argparse.ArgumentTypeError)

Entrada: 

Dado que el programa está diseñado para parsear un archivo TSV, puede añadirse una validación para que solo se acepten documentos que tengan ese formato. 

```bash
uv run python .\src\regulon_summary.py .\data\raw\formato_erroneo.pdf results/filtered_output.tsv --min_genes 2

```

Resultados esperados:
- El usuario recibe un mensaje indicando que el formato del archivo de entrada debe ser TSV. 
- El programa termina de forma ordenada. 

**Resultados**

<br>

### Archivo vacío (validación manual)

Entrada:

```bash
touch data/raw/vacio.tsv
uv run python .\src\regulon_summary.py .\data\raw\vacio.tsv results/filtered_output.tsv --min_genes 2
```

Resultados esperados:
- El usuario recibe un mensaje indicando que el archivo está vacío.
- El programa finaliza de manera ordenada. 

**Resultados**

<br>

### Tipos de datos incorrectos (TypeError)

Entrada:

```bash
touch data/raw/sin_cadenas.tsv
nano data/raw/sin_cadenas.tsv
```

Este será el contenido de ese archivo. Se constata que solo consiste en números, así que sobre este tipo de dato no podrán apicarse los métodos mostrados en el programa (p. ej., ".strip()", ".startswith()", entre otros).  

```
31	64	32		
38	21	09		
8	15	18		
03	86	27	
22  10	14	

```

```bash
uv run python .\src\regulon_summary.py .\data\raw\sin_cadenas.tsv results/filtered_output.tsv --min_genes 2
```

Resultados esperados:
- El usuario recibe un mensaje señalando que el archivo no tiene los tipos de datos adecuados.
- El programa termina de manera ordenada. s

**Resultados**


<br>

### Interactions está vacío, ya que el archivo de entrada solo tenía comentarios

Entrada:

```bash
touch data/raw/comentarios.tsv
nano data/raw/comentarios.tsv
```

Este será el contenido del documento:
```
# License
#	# RegulonDB is free for academic/noncommercial use
# User is not entitled to change or erase data sets of the RegulonDB
# database or to eliminate copyright notices from RegulonDB. Furthermore,
# User is not entitled to expand RegulonDB or to integrate RegulonDB partly
# or as a whole into other databank systems, without prior written consent
# from CCG-UNAM.
# Please check the license at https://regulondb.ccg.unam.mx/manual/aboutUs/terms-conditions
# Citation
#	# Heladia Salgado, Socorro Gama-Castro, et al., RegulonDB v12.0: a comprehensive resource of transcriptional regulation in E. coli K-12,
# Nucleic Acids Research, 2023;, gkad1072, https://doi.org/10.1093/nar/gkad1072
# RegulonDB Release: 14.5
# Contact
#	email:regulondb@ccg.unam.mx
#Date:
#	03-04-2026
## Columns:
## (1) regulatorId. Regulator identifier
## (2) regulatorName. Regulator Name
## (3) regulatorGeneName. Gene(s) coding for the TF
## (4) regulatedId. Gene ID regulated by the Regulator (regulated Gene)
## (5) regulatedName. Gene regulated by the Regulator (regulated Gene)
## (6) function. Regulatory Function of the Regulator on the regulated Gene (+ activator, - repressor, -+ dual, ? unknown)
## (7) confidenceLevel. RI confidence level based on its evidence (Values: Confirmed[C], Strong[S], Weak[W], Unknown[?])

```


```bash
uv run python .\src\regulon_summary.py .\data\raw\comentarios.tsv results/filtered_output.tsv --min_genes 2
```


Resultados esperados:
- El usuario recibe un mensaje indicando que el archivo de entrada solo tenía comentarios.
- El programa termina de manera ordenada. 

**Resultados**

<br>

### Hay líneas duplicadas en las columnas tomadas para construir interactions

Entrada:

```bash
touch data/raw/duplicados.tsv
nano data/raw/duplicados.tsv
```

Este será el contenido del nuevo archivo. Se tomaron algunos renglones del documento original y se duplicaron o incluso triplicaron (p. ej., el gen rbsK ahora aparece tres veces):

```
RDBECOLIPDC00358	DsrA	dsrA	RDBECOLIGNC00450	hns	-	S 
RDBECOLIPDC00358	DsrA	dsrA	RDBECOLIGNC00502	rpoS	+	W 
RDBECOLIPDC00358	DsrA	dsrA	RDBECOLIGNC00539	lrp	-	S 
RDBECOLIPDC00358	DsrA	dsrA	RDBECOLIGNC00804	rbsA	-	S 
RDBECOLIPDC00358	DsrA	dsrA	RDBECOLIGNC00805	rbsB	-	S 
RDBECOLIPDC00358	DsrA	dsrA	RDBECOLIGNC00806	rbsC	-	S 
RDBECOLIPDC00358	DsrA	dsrA	RDBECOLIGNC00807	rbsD	-	S 
RDBECOLIPDC00358	DsrA	dsrA	RDBECOLIGNC00808	rbsK	-	S 
RDBECOLIPDC00358	DsrA	dsrA	RDBECOLIGNC00808	rbsK	-	S 
RDBECOLIPDC00358	DsrA	dsrA	RDBECOLIGNC00808	rbsK	-	S 
RDBECOLIPDC00358	DsrA	dsrA	RDBECOLIGNC00809	rbsR	-	S 
RDBECOLIPDC00358	DsrA	dsrA	RDBECOLIGNC02853	rbsZ	-	S 
RDBECOLIPDC00425	DeaD	deaD	RDBECOLIGNC01227	ldtD	+	W 
RDBECOLIPDC00425	DeaD	deaD	RDBECOLIGNC01227	ldtD	+	W 
RDBECOLIPDC00501	Hfq	hfq	RDBECOLIGNC00559	manX	-	C 
RDBECOLIPDC00501	Hfq	hfq	RDBECOLIGNC01622	hpf	+	W 
RDBECOLIPDC00501	Hfq	hfq	RDBECOLIGNC01623	ptsN	-	W 

```

Se ocupará este comando para correr el programa:

```bash
uv run python .\src\regulon_summary.py .\data\raw\duplicados.tsv results/filtered_output.tsv --min_genes 2
```

Resultados esperados:
- La presencia de líneas duplicadas no altera la construcción del regulon.
- El archivo de salida no toma en cuenta las líneas duplicadas que brindan datos sobre los TFs.

**Resultados**


<br>