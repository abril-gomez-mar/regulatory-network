# Context

## Primera versión del programa

Este proyecto analiza una red de regulación genética.

Los datos contienen interacciones entre factores de transcripción (TF) y genes.

**Formato de los datos:**

TF gene effect

**Ejemplo**

AraC araA + 
AraC araB - 
LexA recA - 

**Objetivo del programa**

Generar una tabla que, para cada TF, indique los siguientes datos:

- Nombre del TF (esta columna debe estar ordenada)
- Total de genes regulados
- Lista de genes regulados (ordenada) 


<br>

## Segunda versión del programa

Además de la tabla anterior, queremos saber si cada TF es un activador, un represor o su efecto es dual. La siguiente tabla resume algunos conceptos claves:

| Tipo de efecto  | Regla | 
|---|---|
| Activador  | Solo tiene + | 
|  Represor | Solo posee - | 
|  Dual | Contiene + y - | 

Entonces, esta es la salida esperada:

| TF  | Total de genes  | Genes activados  | Genes reprimidos  | Tipo de efecto  |
|---|---|---|---|---|
|  AraC | 2 | 1 | 1 | Dual |
|  CRP | 2 | 2 | 0 | Activador |
|  LexA  | 1 | 0 | 1 | Represor |


