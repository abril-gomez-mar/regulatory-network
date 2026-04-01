# Importación de los módulos necesarios.
from collections import defaultdict
import os
import sys

# =================================================================================================================================================================================================================================
#  Creación de las rutas de entrada y salida.
# =================================================================================================================================================================================================================================

# =================================================================================================================================================================================================================================
# Responsabilidad: Esclarecer las rutas de los archivos de entrada y salida. También, si es necesario, se crea la carpeta 'results' en el mismo nivel que 'data'.
# Entrada: Ningún argumento. Las rutas de los archivos de entrada y salida se definen dentro de la función.
# Salida: Rutas de los archivos de entrada y salida. Estos datos serán aprovechados por las funciones subsecuentes. 
# =================================================================================================================================================================================================================================

# TODO: Extraer una función que genere las rutas de los archivos de entrada y salida, de forma que pueda ser aprovechada por la función 'load interactions'.

def defining_routes():
   """ Establece las rutas de los archivos de entrada y salida. Si no existe la carpeta 'results', la genera. 
   
   Args:
        Ninguno. Las citadas rutas se definen dentro de la función.

   Returns:
        filename (str): Ruta del archivo TSV de entrada.
        output_file (str): Ruta donde se albergará el archivo de salida. 
   
   """


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

   return filename, output_file


# =================================================================================================================================================================================================================================
# Creación de una estructura que contenga los datos que se planea plasmar en el archivo de salida.
# =================================================================================================================================================================================================================================

# =================================================================================================================================================================================================================================
# Responsabilidad: Leer el archivo de interacciones regulatorias y construir una estructura de datos. También se valida que el archivo exista y el usuario tenga permiso de leerlo.
# Entrada: Archivo TSV con interacciones regulatorias entre reguladores y genes.
# Salida: Lista de tuplas que señalan los TFs, genes regulados y el tipo de efecto regulatorio.
# =================================================================================================================================================================================================================================

# TODO: Proponer una función que englobe el proceso de limpieza de datos y la construcción de la estructura 'interactions'.

def load_interactions(filename):

    """ Lee el archivo de interacciones regulatorias y devuelve una lista de tuplas con la información relevante.
    
    Args:
    Filename (str): Ruta del archivo TSV de interacciones regulatorias.

    Returns:
    Interactions (str): Esta variable es una lista de tuplas, y cada una de ellas alberga tres strings: nombre de un TF, sus respectivos genes regulados, y el tipo de efecto regulatorio.

    """

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
 
    # Se devuelve la lista de tuplas con la información de los TFs, genes regulados y el tipo de efecto regulatorio.
    return interactions


# =================================================================================================================================================================================================================================
#  Transformación de los datos de 'interactions' en otra estructura de datos que sintetice la información y más adelante pueda utilizarse para redactar el archivo de salida.
# =================================================================================================================================================================================================================================

# =================================================================================================================================================================================================================================
# Responsabilidad: Procesar la lista de tuplas (interactions) para construir un diccionario que represente la red regulatoria.
# Entrada: Lista de tuplas con información sobre los TFs, genes regulados y el tipo de efecto regulatorio.
# Salida: Diccionario; cada clave es un TF y tiene asociado un diccionario con tres etiquetas: 'genes' (lista de genes regulados), 'activados' (número de genes activados) y 'reprimidos' (cantidad de genes reprimidos).  
# =================================================================================================================================================================================================================================

# TODO: Extraer la construcción del regulon a una función, con tal de mejorar la modularidad del programa y facilitar las pruebas unitarias.


def build_regulon(interactions):

    """ Construye un diccionario a partir de los datos procesados con anterioridad. 
   
   Args:
        interactions (str): Lista de tuplas que detallan los nombres de los TFs, sus correspondientes genes regulados, y el efecto regulatorio (activador, represor o dual) del TF sobre los referidos genes.

   Returns:
        regulon (str): Diccionario que sintetiza las interacciones de la red regulatoria. Cada clave será un RF y le corresponderán tres campos (resguardados en un diccionario): lista de genes regulados, número de genes activados y cantidad de genes reprimidos.
   
   """

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

    return regulon


# ================================================================================================================================================================================================================================
#  Creación del archivo TSV de salida.
# ================================================================================================================================================================================================================================

# ================================================================================================================================================================================================================================
# Responsabilidad: Generar el archivo de salida empleando la información del diccionario. También se determina el tipo de regulación (activador, represor o dual) para cada TF, dado el número de genes activados y reprimidos.
# Entrada: Diccionario con datos sobre los TFs, sus respectivos genes regulados, y los totales de genes activados y reprimidos.
# Salida: Archivo TSV; cada línea contiene el nombre del TF, el total de genes regulados, el número de genes activados, la cantidad de genes reprimidos, el tipo de regulación y los nombres de los antedichos genes. 
# ================================================================================================================================================================================================================================

# TODO: Extraer una función que, iterando sobre las keys del diccionario, genere el contenido del archivo de salida, donde cada renglón debe contener seis datos: el nombre del TF, el total de genes regulados, el número de genes activados, la cantidad de genes reprimidos, el tipo de regulación (activador, represor o dual) y los nombres de los antedichos genes.
 
def write_output(regulon, output_file):

    """ Elabora un manuscrito con la información del diccionario recién creado. 
   
   Args:
        regulon (str): Diccionario que contiene la información resumida de la red regulatoria. Cada clave es un TF y se vincula con tres etiquetas: 'genes' (lista de genes regulados), 'activados' (número de genes activados) y 'reprimidos' (cantidad de genes reprimidos).
        output_file (str): Ruta del archivo de salida, la cual se definió en la función 'defining_routes'. Este documento se localizará en la carpeta 'results' y se llamará 'regulon_summary.tsv'.
        
   Returns:
        Ninguno. La función solo transcribe la información en el archivo de salida, así que no debe regresar ningún valor particular.
   
   """

    # La información recopilada se plasma en el archivo de salida. Un tabulador separa cada dato. Se escribe la primera línea del documento.
    with open(output_file, 'w') as outfile:
        outfile.write('TF\tTotal genes\tActivados\tReprimidos\tTipo de efecto regulatorio\tLista de genes\n')

        # Los TFs se ordenan de manera alfabética y se itera sobre cada uno de ellos. 
        for TF in sorted(regulon):
            data = regulon[TF]

            # Se acomoda de manera alfabética la lista de target genes de cada TF. Luego, se obtiene la cardinalidad de dicha lista y sus strings se concatenan con una coma y un espacio como separador.
            genes = sorted(data["genes"])
            total = len(genes)
            lista_genes = ', '.join(genes)

            # Considerando los resultados de los contadores de genes activados y reprimidos, se pondera cuál es el efecto regulatorio de cada TF: activador, represor o dual. 
            activados = data["activados"]
            reprimidos = data["reprimidos"]

            # En este escenario, los totales de cada contador son mayores que cero.
            if activados and reprimidos:
                efecto = 'Dual'

            # En esta instancia, solo el total de genes activados es mayor que cero, mientras que hay cero genes reprimidos.
            elif activados and not reprimidos:
                efecto = 'Activador'

            # En este caso, la cantidad de genes reprimidos es superior a cero, pero no hay genes activados.    
            else:
                efecto = 'Represor'

            # En cada línea del archivo de salida se colocan los seis datos correspondientes a cada TF, separados por un tabulador.
            outfile.write(f'{TF}\t{total}\t{activados}\t{reprimidos}\t{efecto}\t{lista_genes}\n')


    # Dado que no se regresará ningún valor, al menos puede imprimirse un mensaje para indicarle al usuario que el archivo ya está disponible en la carpeta 'results'. 
    print(f'El archivo regulon_summary.tsv puede consultarse en la carpeta "results".')

    # A raíz de que 'return 0' no estará asociado a ningún valor, estará vacío y por ello puede omitirse. 


# =================================================================================================================================================================================================================================
#  Función principal que posibilitará la ejecución del programa.
# ================================================================================================================================================================================================================================= 

def main():
    """ Función que ejecuta en el orden correcto las funciones mostradas más arriba. No recibe ningún argumento y tampoco regresa ningún valor. """

    # Se definen las rutas de los archivos de entrada y salida.
    filename, output_file = defining_routes()

    # Se carga el archivo de interacciones regulatorias y se obtiene una lista de tuplas con la información relevante.
    interactions = load_interactions(filename)

    # Se construye un diccionario a partir de la lista de tuplas.
    regulon = build_regulon(interactions)

    # Se genera el archivo de salida con la información del diccionario.
    write_output(regulon, output_file)

#==================================================================================================================================================================================================================================
# Se llama a la función principal para ejecutar el programa.
# =================================================================================================================================================================================================================================

if __name__ == "__main__":
    main()
