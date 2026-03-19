# Lista de interacciones en la red regulatoria. Cada tupla incluye el nombre del TF, su target gene, y el efecto sobre dicho gen.
interactions = [
("AraC", "araA", "+"),
("AraC", "araB", "-"),
("LexA", "recA", "-"),
("CRP", "lacZ", "+"),
("CRP", "lacY", "+")
]

regulon = {}  

# Primera parte del análisis. 
# Se recorren las tuplas y se construye un diccionario. Cada llave será un TF; sus valores, los genes que regula. 
# De nuevo, se recorren las tuplas y se construye un diccionario. 
# Cada llave será un TF, pero sus valores serán tuplas con esta estructura: (gen, efecto del TF).
for TF, gene, effect in interactions:
    if TF not in regulon:
        regulon[TF] = []
    regulon[TF].append(gene)

for TF in sorted(regulon):
    genes = sorted(regulon[TF])
    total = len(genes)
    lista_genes = ", ".join(genes)    
    print(TF, total, lista_genes)

# Se decidió añadir una línea en blanco para separar ambas tablas.
print("\n")

# De nuevo, se recorren las tuplas y se construye un diccionario. Para no emplear demasiadas variables, se reusó el nombre del diccionario.
# Cada llave será un TF, pero sus valores serán tuplas con esta estructura: (gen, efecto del TF).
regulon = {}  

for TF, gene, effect in interactions:
    if TF not in regulon:
        regulon[TF] = []
    regulon[TF].append((gene, effect))

# Se ordenan los TFs y por cada uno de ellos se inicializan tres variables: el total de genes regulados, los genes activados y los genes reprimidos.
# Asimismo, se examina la información de las tuplas (gen, efecto) preservadas en los valores de cada llave (TF). 

for TF in sorted(regulon):
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