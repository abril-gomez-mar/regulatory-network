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


## Actualización v1.1

1. Leer los datos desde un archivo.
 1.1 Cada línea del archivo contiene 6 o 7 columnas, y las que vamos a usar son regulatorName, regulatedName y function. 
 1.2 A partir de la información en esas hileras, se pretende generar este resumen:

| TF  | Total de genes  | Genes activados  | Genes reprimidos  | Tipo de efecto  | Lista de genes regulados |
|---|---|---|---|---|---|
|  AraC | 2 | 1 | 1 | Dual | araA, araB | 
|  CRP | 2 | 2 | 0 | Activador | lacY, lacZ |
|  LexA  | 1 | 0 | 1 | Represor | recA |

2. Los resultados deberán mandarse a un archivo de salida, cuyo formato será TSV. 

<br>

## Actualización v1.2

Problema:
El programa depende de rutas fijas (harcoded). 

Nuevo requisito:
El programa debe recibir 2 argumentos: el archivo de entrada y el archivo de salida. 

<br>

## Actualización v1.3

Problema:
El programa no permite filtrar los reguladores por un número mínimo de genes.

Nuevo requisito:
El programa debe permitir filtrar los TFs mostrando solo aquellos que tengan al menos un número mínimo de genes, definido por el argumento `--min_genes`.

<br>

## Actualización v1.4

Problema: Mejorar la robustez del programa actual. 

Nuevos requisitos: Debe incorporarse el manejo de errores en operaciones de entrada y salida; asimismo, es menester extender la validación del programa cuando sea necesario. 