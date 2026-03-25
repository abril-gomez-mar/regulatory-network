# Importación de las bibliotecas necesarias.
from collections import defaultdict
import os

# Recepción y limpieza de los datos del archivo TSV.
interactions = []

# Lectura de datos desde el archivo TSV
filename = '../data/raw/NetworkRegulatorGene.tsv'

with open(filename) as f:

    for line in f:
        # Remoción de saltos de línea.
        line = line.strip() 

        # Se verifica que las líneas no estén vacías.
        if not line:
            continue

        # Verificación de que las líneas no sean comentarios o pertenezan al encabezado del archivo. Se revisó que el encabezado del archivo comienza con '1)regulatorId'.
        if line.startswith('#') or line.startswith('1)regulatorId'):
            continue

        # Se dividen las líneas en campos utilizando el tabulador como separador.
        fields = line.split('\t') 

        # Validación del número mínimo de columnas requeridas para procesar la información. 
        if len(fields) < 6:
            continue

        # Selección de las columnas que se utilizarán para construir la red regulatoria.
        TF = fields[1]
        gene = fields[4]
        effect = fields[5]

        # Comprobación de que solo se incluirán los tres tipos válidos de efectos genéticos: activación ('+'), represión ('-') y efecto dual ('-+').
        if effect not in ('+', '-', '-+'):
            continue

        # Creación de tuplas que sintetizan las interacciones en la red regulatoria.
        interactions.append((TF, gene, effect))

# Creación del archivo de salida y se escribe su primera línea.
os.makedirs('results', exist_ok=True)
with open('results/regulon_summary.tsv', 'w') as outfile:
  outfile.write('TF\tTotal genes\tActivados\tReprimidos\tTipo de regulación\tLista de genes\n')

# Se preservó la idea central del código original: procesar la lista de tuplas para crear un diccionario de la red regulatoria. Cada key (TF) tendrá esta tupla: (gen, efecto del TF).
# A partir del diccionario, se obtienen los seis datos que se colocarán en cada línea del archivo de salida: el nombre del TF, el total de genes regulados, el número de genes activados, la cantidad de genes reprimidos, el tipo de regulación (activador, represor o dual) y los nombres de los citados genes.
regulon = defaultdict(lambda: {"genes": [],"activados": 0,"reprimidos": 0})
for TF, gene, effect in interactions:
    data = regulon[TF]
    data['genes'].append(gene)

    if effect == '+':
            data['activados'] += 1

    elif effect == '-':
            data['reprimidos'] += 1    

     # Se agregó esta línea para contabilizar los genes cuyo efecto es '-+', ya que el código inicial asumía que solo existían los efectos '+' y '-'.
    else:
            data['activados'] += 1
            data['reprimidos'] += 1 

# La información recopilada se plasma en el archivo de salida. Un tabulador separa cada dato.
output_file = 'results/regulon_summary.tsv'

with open(output_file, 'w') as outfile:
    outfile.write('TF\tTotal genes\tActivados\tReprimidos\tTipo de regulación\tLista de genes\n')

    for TF in sorted(regulon):
        data = regulon[TF]

        genes = ", ".join(sorted(data["genes"]))
        total = len(genes)
        activados = data["activados"]
        reprimidos = data["reprimidos"]

        if activados and reprimidos:
            efecto = 'Dual'

        elif activados and not reprimidos:
            efecto = 'Activador'
        else:
            efecto = 'Represor'

        outfile.write(f'{TF}\t{total}\t{activados}\t{reprimidos}\t{efecto}\t{genes}\n')