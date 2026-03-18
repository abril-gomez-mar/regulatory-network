# Lista de interacciones en la red regulatoria. Cada tupla incluye el nombre del TF, su target gene, y el efecto sobre dicho gen.
interactions = [
("AraC", "araA", "+"),
("AraC", "araB", "-"),
("LexA", "recA", "-"),
("CRP", "lacZ", "+"),
("CRP", "lacY", "+")
]

regulon = {}

# Se recorren las tuplas y se construye un diccionario. Cada llave será un TF; sus valores, los genes que regula. 
for TF, gene, effect in interactions:
    if TF not in regulon:
        regulon[TF] = []
    regulon[TF].append(gene)

# Se ordenan los TFs, así como sus target genes. 
# Además, cada lista de genes se somete a dos procesos: se calcula su longitud y se convierte a una cadena de texto; los genes son separados por comas. 
# Al final, se imprime el nombre del TF y su total de target genes, los cuales también se nombran.

for TF in sorted(regulon):
    genes = sorted(regulon[TF])
    total = len(genes)
    lista_genes = ", ".join(genes)    
    print(TF, total, lista_genes)

       