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
uv run python regulon_summary.py NetworkRregulatorGene.tsv tf_summary.yxy

```

Resultado
El programa lee el archivo de entrada y genera el resultado con el nombre que se le pasó como argumento. 
