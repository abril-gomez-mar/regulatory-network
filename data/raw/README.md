# Dataset: Regulatory interactions (RegulonDB)

## Fuente
RegulonDB

## Archivo
NetworkRegultorGene.tsv

## Versión
v14.5

## Formato
TSV (tab-separated values)

## Columnas relevantes para este análisis
- regulatorName
- regulatedName
- function


## Observaciones
- El archivo contiene comentarios y en total está conformado por 7375 líneas.
- No parece haber líneas vacías, pero ciertas líneas tienen más columnas que el resto de los renglones. 
- Cada columna está asociada a un encabezado.
- Solo se usarán tres columnas en este proyecto: la segunda, la quinta y la sexta. 
- La columna que detalla los tipos de regulación puede tener alguno de estos valores: +, - o -+.