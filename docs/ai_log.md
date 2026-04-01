# Interacciones relacionadas con las primeras versiones del programa.

En este caso, se usó GitHub Copilot Chat.

## Interacción 1
Modo: ASK 

Pregunta: ¿De qué otras formas puedo determinar el total de genes regulados por cada TF, así como las cantidades de genes activados y reprimidos por el mismo factor de transcripción?

Aprendí: Podría hacer comprehension lists que aprovechasen las tuplas (gen, efecto del TF) que almacené como valores de cada llave en el diccionario. En este sentido, por cada TF, se recorrerían todos sus valores: el primer elemento de todas las tuplas correspondería al nombre del gen regulado, así que estas denominaciones se preservarían en una lista cuyo número de elementos se calcularía hasta al final. Por su parte, el segundo elemento de todas las tuplas representaría el tipo de efecto que cierto TF tiene sobre su target gene; esta información podría guardarse en una lista para después examinar la frecuencia de los símbolos '+' y '-'. 

A raíz de lo anterior, de este modo podrían ocuparse las comprehension lists:

```python

# Nótese que regulon [TF] alude a los valores, que en este caso son tuplas (gen, efecto) llamadas "traits", de cada llave. Así, traits[0] es el target gene, mientras que traits[1] describe el tipo de efecto del TF.

for TF in sorted(regulon):
activados = 0
reprimidos = 0    
total_genes = len([traits [0] for traits in regulon[TF]]) 

global_effects = [traits[1] for traits in regulon[TF]] 
for item in global effects:
    if item == '+':
      activados += 1
    else:
      reprimidos += 1    
```

El principal inconveniente del enfoque previo es que genera listas intermediarias para encontrar los valores numéricos que podrían averiguarse tras solo analizar los elementos de cada una de las tuplas presentes en el diccionario recién creado.


# Interacciones relacionadas con la versión actualizada del código (construcción de interactions a partir de un archivo de entrada)

A continuación, se describen las interacciones que se tuvieron con PyLIA — Pythonic Line Interface Assistant.

## Interacción 1

**Pregunta:** ¿Cómo puedo indicar que el documento de salida `regulon_summary.tsv` debe guardarse en la carpeta `results`, que debe crearse si no existe?

**Aprendí:** Puedo importar el módulo os y puntualizar, mediante os.makedirs(), el nombre del directorio que crearé. Entonces, puedo integrar este fragmento de código:

```python
import os

os.makedirs('results', exist_ok=True)

```

Más adelante, al usar "with open() as outfile:" para crear el archivo de salida, en el primer parámetro deberé escribir 'results/', seguido del nombre del documento. Así, la línea será la siguiente: 

```python

with open('results/regulon_summary.tsv', 'w') as outfile:
```

<br>

## Interacción 2

**Pregunta:** ¿De qué forma puedo hacer mi código más eficiente? En este momento, tengo un for que itera sobre cada TF (key) del diccionario creado a partir de interactions y luego hay un for interno que revisa cada tupla (gene, effect). Quisiera deshacerme de este último ciclo para que disminuyera la complejidad del algoritmo, porque me parece que en este momento ella se asemeja a O(n*m), donde n es el número de TFs y m podría ser el número promedio de tuplas asociadas a cada transcription factor.  

**Aprendí:** Respetando la lógica de las versiones previas del código, puedo importar defaultdict del módulo collections. Ese nuevo tipo de diccionario me permitirá usar de manera directa los datos de interactions (agrupados como (TF, gene, effect)) y crear una estructura predeterminada para analizar cada TF, la cual incluirá la lista de genes, el total de genes activados y el número de genes reprimidos. Así, preservaré las variables con las que estaba trabajando y evitaré crear una serie de tuplas en el diccionario, las cuales estaba analizando más adelante para contar los genes reprimidos o activados.

Por lo anterior, puedo añadir este fragmento de código a mi programa e incluir un tercer condicional para evaluar el parámetro effect, ya que ahora el archivo puede contener '+-' en la sexta columna de cada renglón.

```python
regulon = defaultdict(lambda: {"genes": [],"activados": 0,"reprimidos": 0})
for TF, gene, effect in interactions:
    data = regulon[TF]
    data['genes'].append(gene)

    if effect == '+':
        data['activados'] += 1

    elif effect == '-':
        data['reprimidos'] += 1    

```

<br>

## Interacción 3

**Pregunta:** ¿De qué forma puedo modificar mi código para validar que el archivo de entrada existe? Asimismo, ¿cómo puedo cambiar mi código para que reconozca que `results` debe crearse para resguardar el archivo de salida, pero este repositorio deberá estar en el mismo nivel que las demás carpetas del proyecto?

**Aprendí:** Puedo importar el módulo sys y aprovechar otras funciones de os. Gracias a este último módulo, puedo establecer varias rutas: la del directorio actual, la de la raíz (que está un nivel más arriba que `src`), la del archivo de entrada, y la del documento de salida. Este mismo módulo me permitirá precisar, mediante os.path.join() y os.makedirs(), que deseo crear `results` en el mismo nivel que la raíz del proyecto. 

Por su parte, mediante la instrucción "try" del módulo sys puedo indicarle al programa que debe intentar abrir el archivo de entrada, mismo que se resguardaría en `filename` tras definir la ruta con os.path.join(). A su vez, por medio de la cadena "except FileNotFoundError:" y la posterior indentación apropiada de algunas instrucciones, puedo esclarecer qué debería ocurrir si el documento no existiera en la ruta preestablecida.

Entonces, puedo incorporar este código a mi programa:

```python

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)

data_dir = os.path.join(project_root, 'data', 'raw')
filename = os.path.join(data_dir, 'NetworkRegulatorGene.tsv')

results_dir = os.path.join(project_root, 'results')
os.makedirs(results_dir, exist_ok=True)

output_file = os.path.join(results_dir, 'regulon_summary.tsv')

try:
    # Aquí estarían todas las líneas subordinadas a with open(filename) as f:


except FileNotFoundError:
    print(f'Error: archivo {filename} no encontrado')
    sys.exit(1)
```

<br>

## Interacción 4

**Pregunta:** Dada la nueva versión del código, ¿cómo puedo validar que el archivo de entrada existe, pero no puede ser leído?

**Aprendí:** Considerando que ya importé el módulo sys, puedo usar la cadena "except PermissionError:", seguida de un par de instrucciones indentadas, para dilucidar cómo debería comportarse el programa en caso de que el usuario no tenga permiso de leer el archivo de entrada. En consecuencia, puedo emplear este fragmento de código, el cual imprime el error que se presentó y finaliza el programa:

```python

except PermissionError:
    print(f'Error: permiso denegado para leer el archivo {filename}')    
    sys.exit(1)
```

## Interacción 5

**Pregunta:** Dado que en la última función no necesito regresar ningún valor, ¿también debo poner un 'return' al final de ese fragmento de código?

**Aprendí:** Si bien escribirse 'return 0' al final del programa, cualquier función que carezca de dicha línea ejecutará 'return' de manera automática. Por otro lado, en vista de que en este código se piensa devolver de forma explícita un valor nulo después de generar el archivo de salida, podría ser más práctico regresar 0 de manera implícita.


