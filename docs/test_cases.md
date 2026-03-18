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
| LexA | recA  | - |


- Resultados:
```

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
| CRP  |  3 |  lacZ, lazY, lacA |  

- Resultados:
```

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
| LexA |  2 | recA, umuC |  
|  AraC | 2 | araE, araA |

- Resultados:
```

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

```


¿Coinciden con la salida esperada? Sí.