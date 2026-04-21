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


<br>

### Falta de permisos (PermissionError)

Entrada:

```bash
touch data/raw/bloqueado.tsv
chmod 000 data/raw/bloqueado.tsv
uv run python .\src\regulon_summary.py .\data\bloqueado.tsv results/output.tsv --min_genes 2

```

Resultado esperado:
- Se arroja un mensaje para indicar que el usuario no puede leer el archivo.
- El programa finaliza de forma ordenada. 


**Resultados**




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

<br>

### Falta de permisos (PermissionError)


Entrada:

```bash
mkdir salida_bloqueada
chmod 000 salida_bloqueada
uv run python .\src\regulon_summary.py .\data\raw\NetworkRegulatorGene.tsv salida_bloqueada/output.tsv --min_genes 2

```

Resultado esperado:
- Se comunica al usuario que no cuenta con el permiso de escribir el archivo de salida.
- El programa termina de manera organizada. 

**Resultados**

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


<br>
