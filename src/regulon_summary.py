# Importación de los módulos necesarios.
from collections import defaultdict
import os
import sys
import argparse

# =================================================================================================================================================================================================================================
#  Creación de las rutas de entrada y salida.
# =================================================================================================================================================================================================================================

# =================================================================================================================================================================================================================================
# Responsabilidad: Esclarecer las rutas de los archivos de entrada y salida. También, si es necesario, se crea la carpeta 'results' en el mismo nivel que 'data'.
# Entrada: Ningún argumento. Las rutas de los archivos de entrada y salida se definen dentro de la función.
# Salida: Rutas de los archivos de entrada y salida. Estos datos serán aprovechados por las funciones subsecuentes. 
# =================================================================================================================================================================================================================================

# TODO: Extraer una función que genere las rutas de los archivos de entrada y salida, de forma que pueda ser aprovechada por la función 'load interactions'.
# TODO: Validar, mediante el uso del módulo os, que el archivo de entrada exista. De ser posible, también verificar que dicho documento pueda ser leído.
# TODO: Extraer, mediante el módulo argparse, una función que cumpla los mismos roles mostrados enseguida: definir las rutas de los archivos de entrada y salida.

def parse_arguments():

   """ Recibe rutas de los archivos de entrada y salida (ellas son relativas a la raíz del proyecto).
       Asimismo, resuelve esas rutas y, si es necesario, crea el directorio del archivo de salida. 
   
   Args:
        Dos rutas relativas. No se brindan desde main, sino que se proporcionan a través de la línea de comandos.

   Returns:
        filename (str): Ruta absoluta del archivo TSV de entrada.
        output_file (str): Ruta absoluta donde se albergará el archivo de salida.
        min_genes (int): Número mínimo de genes que un TF debe tener para ser parte del archivo de salida. 
   
   """

   parser = argparse.ArgumentParser(description='Rutas relativas (respecto a la raíz del proyecto) de los archivos de entrada y salida.')

   # Definir los argumentos posicionales.
   parser.add_argument('input', help='Ruta relativa del archivo TSV de entrada.')
   parser.add_argument('output', help='Ruta relativa del archivo TSV de salida.')
   
   # Definir un nuevo argumento, que será opcional, para filtrar los TFs que se tomarán en cuenta al redactar el archivo de salida.
   parser.add_argument('--min_genes', type=int, default=1, help='Número mínimo de genes asociados a cada uno de los TFs que se desea incluir en el archivo de salida.')
   
   args = parser.parse_args()

   # Validación de que el archivo de entrada tiene la extensión .tsv o .txt (se ha atestiguado que un archivo con extensión .txt puede contener tabuladores, así que se aceptará esa extensión).
   if not args.input.lower().endswith(('.tsv', '.txt')):
        raise argparse.ArgumentTypeError(f'El archivo de entrada {args.input} debe ser .tsv o .txt. Por favor, revise que haya seleccionado el archivo correcto e intente de nuevo.')

   # Se establece la ruta absoluta de la raíz del proyecto, para lo cual se obtiene la ruta del directorio actual y luego se accede a su carpeta parental.
   current_dir = os.path.dirname(os.path.abspath(__file__))
   project_root = os.path.dirname(current_dir)

   # Las rutas relativas introducidas se vinculan con la raíz del proyecto. Luego, se establecen las rutas absolutas de los archivos de entrada y salida. Esta información se aprovechará más adelante.
   filename = os.path.abspath(os.path.join(project_root, args.input))
   output_file = os.path.abspath(os.path.join(project_root, args.output))

   # Se removió la línea que creaba el directorio 'results', si aún no existía. Por ende, el usuario siempre deberá señalar que el output se almacenará en dicha carpeta, y cualquier otra ruta será rechazada más adelante.

   # Para mejorar el manejo de errores, se regresó a load_interactions la sección encargada de cerciorarse de que el archivo de entrada exista y pueda ser leído.
   
   # Se regresan las rutas de los archivos de entrada y salida. También se retorna un dato que se usará más abajo: el número mínimo de genes de los TFs que figurarán en el archivo de salida. 
   return filename, output_file, args.min_genes

# =================================================================================================================================================================================================================================
# Creación de una estructura que contenga los datos que se planea plasmar en el archivo de salida.
# =================================================================================================================================================================================================================================

# =================================================================================================================================================================================================================================
# Responsabilidad: Leer el archivo de interacciones regulatorias y construir una estructura de datos. De antemano, se validó que el archivo existiera y pudiera ser leído por el usuario.
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
    # Validaciones relaciondas con la ruta del archivo de entrada. 
    
    input_dir = os.path.dirname(filename)
    if not os.path.exists(input_dir):
        raise RuntimeError('Error: la ruta especificada es errónea. Por favor, revise lo que tecleó e intente de nuevo.')
    
    if not os.path.exists(filename):
        raise RuntimeError('Error: el archivo de entrada no existe. Por favor, revise la ruta proporcionada e intente de nuevo.')
    
    if os.path.isdir(filename):
        raise RuntimeError('Error: la ruta especificada es un directorio, no un archivo. Por favor, revise la ruta proporcionada e intente de nuevo.')

    # Recepción y limpieza de los datos del archivo TSV.
    interactions = []

    try: 
        with open(filename) as f:
            if not f.read(1): 
                raise ValueError('Error: el archivo de entrada está vacío. Por favor, revise el documento e intente de nuevo.')
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

                if '\t' not in line and ' ' in line:
                    raise ValueError('Error: el archivo usa espacios en lugar de tabuladores, así que no se puede procesar. Por favor, revise el documento de entrada e intente de nuevo.')

                # Se dividen las líneas en campos utilizando el tabulador como separador. En la línea previa se validó que el archivo separa sus datos con tabuladores, así que esta división debería ser exitosa.
                fields = line.split('\t')

                # Validaciones sobre los tipos de datos y el número de columnas del archivo de entrada.  
                if all(f.strip().isdigit() for f in fields if f.strip()):
                    raise TypeError('Error: el archivo contiene únicamente valores numéricos, pero se anticipaban cadenas para TF y genes. Por favor, revise el documento de entrada e intente de nuevo.')
 
                if len(fields) < 6:
                    raise ValueError(f'Error: el archivo contiene al menos una línea con columnas insuficientes. Por favor, revise ese documento e intente de nuevo.')

                # Selección de las columnas que se utilizarán para construir la red regulatoria. Más adelante, se revisará que los nombres de los TFs no sean anómalos. 
                TF = fields[1]
                gene = fields[4]
                effect = fields[5]

                if TF.isdigit() or gene.isdigit():
                    raise TypeError(f'Error: tipo de dato incorrecto. Se esperaba un nombre (string) pero se encontró un valor numérico en un TF, un gen o ambos. Por favor, revise el archivo de entrada e intente de nuevo.')
                
                tf_digits = ''.join('T' if c.isdigit() else 'F' for c in TF)

                if 'TTTTT' in tf_digits:
                    raise ValueError(f'Error: se encontró un TF con una denominación inválida; recuerde que ninguna puede contener cinco o más dígitos consecutivos. Por favor, revise el archivo de entrada e intente de nuevo.')

                # Comprobación de que solo se incluirán los tres tipos válidos de efectos genéticos: activación ('+'), represión ('-') y efecto dual ('-+').
                if effect not in ('+', '-', '-+'):
                    print(f'Advertencia. Efecto desconocido {effect} en la interacción entre {TF} y {gene}. Se omitirá esta interacción.')
                    continue

                # Creación de tuplas que sintetizan las interacciones en la red regulatoria.
                interactions.append((TF, gene, effect))      

    # Se reincorporaron las líneas de manejo de errores.
    except PermissionError:
        raise RuntimeError('Error: no se puede acceder al archivo de entrada, ya que usted no tiene permisos de lectura.')
     
    except OSError as e:
        raise RuntimeError(f'Error al intentar abrir o leer el archivo de entrada. Se presentó un error en el sistema operativo: {e}')
    
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
    regulon = defaultdict(lambda: {"genes": set(),"activados": 0,"reprimidos": 0})

    for TF, gene, effect in interactions:
        data = regulon[TF]
        data['genes'].add(gene)

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
 
def write_output(regulon, output_file, min_genes):

    """ Elabora un manuscrito con la información del diccionario recién creado. 
   
   Args:
        regulon (str): Diccionario que contiene la información resumida de la red regulatoria. Cada clave es un TF y se vincula con tres etiquetas: 'genes' (lista de genes regulados), 'activados' (número de genes activados) y 'reprimidos' (cantidad de genes reprimidos).
        output_file (str): Ruta del archivo de salida, la cual se definió en la función 'defining_routes'. Este documento se localizará en la carpeta 'results' y se llamará 'regulon_summary.tsv'.
        min_genes (int): Número mínimo de genes asociados a un TF para que este se incluya en el archivo de salida.

   Returns:
        Ninguno. La función solo transcribe la información en el archivo de salida, así que no debe regresar ningún valor particular.
   
    """

    # En esta sección se validaría que la ruta del archivo de salida no solo sea un directorio. De lo contrario, habría un OSError porque la ruta sería inválida. 
    if os.path.isdir(output_file):
        raise RuntimeError('La ruta del archivo de salida es inválida, ya que no menciona el nombre del documento. Por favor, revise los datos proporcionados e intente de nuevo.')

    # Se revisaría que el directorio del archivo de salida existiera. De lo contrario, se identificaría un FileNotFoundError. 
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        raise RuntimeError('El directorio del archivo de salida no existe. Recuerde que debe emplear la carpeta results para almacenar aquel archivo.')

    # Aquí se detectaría si hubiera un PermissionError.
    if not os.access(output_dir, os.W_OK):
        raise RuntimeError('Usted no puede escribir en el directorio de salida. Por favor, revise sus permisos y vuelva a intentarlo.')

    try:

        # La información recopilada se plasma en el archivo de salida. Un tabulador separa cada dato. Se escribe la primera línea del documento.
        with open(output_file, 'w') as outfile:

            outfile.write('TF\tTotal genes\tActivados\tReprimidos\tTipo de efecto regulatorio\tLista de genes\n')

            # Los TFs se ordenan de manera alfabética y se itera sobre cada uno de ellos. 
            for TF in sorted(regulon):
                data = regulon[TF]

                # Se acomoda de manera alfabética la lista de target genes de cada TF. Luego, se obtiene la cardinalidad de dicha lista.
                genes = sorted(data["genes"])
                total = len(genes)

                # Se crea un filtro con base en min_genes, que equivale al valor de args.min_genes definido en la función parse_arguments. 
                # Solo si el valor de la variable 'total' es mayor o igual al mínimo de genes, el código subordinado al if no se ejecutará y por ende el TF se tomará en cuenta para escribir el archivo de salida. 
                if total < min_genes:
                    continue   

                # Los target genes se concatenan en un string y solo son separados por comas, seguidas de un espacio.
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

    # Aquí se manejarían los errores relacionados con la escritura del archivo de salida.
    except OSError as e:
        raise RuntimeError(f'Error al intentar escribir el archivo de salida. Ocurrió un error en el sistema operativo: {e}')
        
    # Dado que no se regresará ningún valor, al menos puede imprimirse un mensaje para indicarle al usuario que el archivo ya está disponible en la carpeta 'results'. 
    print(f'El archivo {output_file} puede consultarse en la carpeta "results".')

    # A raíz de que 'return 0' no estará asociado a ningún valor, estará vacío y por ello puede omitirse. 


# =================================================================================================================================================================================================================================
#  Función principal que posibilitará la ejecución del programa.
# ================================================================================================================================================================================================================================= 

def main():
    """ Función que ejecuta en el orden correcto las funciones mostradas más arriba. No recibe ningún argumento y tampoco regresa ningún valor. """

    try:

        # Se definen las rutas de los archivos de entrada y salida. 
        filename, output_file, min_genes = parse_arguments()

        if min_genes < 0 or min_genes > 1000:
            raise ValueError(f'Error: si usted coloca el argumento opcional --min_genes, no puede usar un valor negativo o superior a 1000. Intente de nuevo.')

        # Se carga el archivo de interacciones regulatorias y se obtiene una lista de tuplas con la información relevante.
        interactions = load_interactions(filename)

        # En caso de que el archivo de entrada solo tenga comentarios y por ende interactions quede vacía, el usuario recibe una advertencia y se detiene la ejecución del programa.
        if not interactions:
            raise ValueError('Error: el archivo de entrada solo tiene comentarios. Por favor, revise el documento e intente de nuevo.')

        # Se construye un diccionario a partir de la lista de tuplas.
        regulon = build_regulon(interactions)

        # Se genera el archivo de salida con la información del diccionario.
        write_output(regulon, output_file, min_genes)

    except Exception as e:
        print(e)
        sys.exit(1)
#==================================================================================================================================================================================================================================
# Se llama a la función principal para ejecutar el programa.
# =================================================================================================================================================================================================================================

if __name__ == "__main__":
    main()
