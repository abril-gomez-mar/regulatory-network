# Importación de los módulos necesarios.
from collections import defaultdict
import os
import sys

# Se establecen las rutas con las cuales se trabajará. Si no existe la carpeta 'results', se crea para almacenar el archivo de salida.

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)

# Información sobre el archivo de entrada.
data_dir = os.path.join(project_root, 'data', 'raw')
filename = os.path.join(data_dir, 'NetworkRegulatorGene.tsv')

# Datos sobre el archivo de salida.
results_dir = os.path.join(project_root, 'results')
os.makedirs(results_dir, exist_ok=True)

output_file = os.path.join(results_dir, 'regulon_summary.tsv')

# Recepción y limpieza de los datos del archivo TSV.
interactions = []

try:
    with open(filename) as f:

        for line in f:
            # Remoción de saltos de línea.
            line = line.strip() 

            # Se verifica que las líneas no estén vacías.
            if not line:
                continue

            # Verificación de que las líneas no sean comentarios.
            if line.startswith('#'):
                continue 
            
            # Inspección de que las líneas no pertenezan al encabezado, que comienza con '1)regulatorId'.
            if line.startswith('1)regulatorId'):
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
                print(f'Advertencia. Efecto desconocido {effect} en la interacción entre {TF} y {gene}. Se omitirá esta interacción.')
                continue

            # Creación de tuplas que sintetizan las interacciones en la red regulatoria.
            interactions.append((TF, gene, effect))

# Manejo de posibles errores al intentar abrir el archivo. Si alguno de estas fallas se presenta, el usuario recibirá un mensaje y el programa finalizará de manera controlada.
except FileNotFoundError:
    print(f'Error: archivo {filename} no encontrado')
    sys.exit(1)
except PermissionError:
    print(f'Error: permiso denegado para leer el archivo {filename}')    
    sys.exit(1)

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

# La información recopilada se plasma en el archivo de salida. Un tabulador separa cada dato. Se escribe la primera línea del documento.
with open(output_file, 'w') as outfile:
    outfile.write('TF\tTotal genes\tActivados\tReprimidos\tTipo de efecto regulatorio\tLista de genes\n')

    for TF in sorted(regulon):
        data = regulon[TF]

        genes = sorted(data["genes"])
        total = len(genes)
        lista_genes = ', '.join(genes)
        activados = data["activados"]
        reprimidos = data["reprimidos"]

        if activados and reprimidos:
            efecto = 'Dual'

        elif activados and not reprimidos:
            efecto = 'Activador'
        else:
            efecto = 'Represor'

        outfile.write(f'{TF}\t{total}\t{activados}\t{reprimidos}\t{efecto}\t{lista_genes}\n')