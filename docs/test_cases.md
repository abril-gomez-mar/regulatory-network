# Casos de prueba

## Caso 1

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

## Caso 2

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

## Caso 3

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

## Caso adicional mencionado al final de la clase

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