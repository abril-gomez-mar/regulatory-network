# Documentación de interacciones con IA

Registro de preguntas, respuestas y cambios aplicados al código. El borrador de la plantilla se generó mediante la asistencia de la IA, y después se validó que no faltara ninguna sección solicitada. 

---
## Interaccion 1. Reemplazo del módulo sys por os, con tal de validar el archivo de entrada

### Pregunta
¿Cómo puedo implementar el nuevo TODO para que, mediante el módulo os, se revise que el archivo de entrada existe y puede ser leído? Esos eran los roles de dos validaciones que había creado con el módulo sys en la función load_interactions. 

### Respuesta resumida
Es posible usar dos expresiones para hacer dichas validaciones sin sys: os.path.isfile(filename) y os.access(filename, os.R_OK). La primera línea verifica que el archivo exista, mientras que la segunda checa si el usuario tiene permisos de lectura. Ya no se requeriría usar "try" y "except" al crear la lista de interacciones en load_interactions. 

### Mi aprendizaje
Puedo construir dos ifs con esas expresiones y subordinar a cada condicional a un par de instrucciones que, solo si el archivo no existe o no puede leerse, impriman un mensaje de error y terminen la ejecución del código. Estos condicionales podrían ser desplazados a la primera función del programa, lo cual permitiría que load_interactions solo se encargara de elaborar la lista de interacciones.

### Modificaciones en el código
- Adición de dos condicionales en la función defining_routes:

```python
if not os.path.isfile(filename):
      print(f'Error: el archivo de entrada no existe.')
      sys.exit(1)

   # ...

   if not os.access(filename, os.R_OK):
      print(f'Error: no se puede acceder al archivo de entrada, ya que usted no tiene permisos de lectura.')
      sys.exit(1)

```

- Se removieron las palabras "try" y "except" dentro de la función load_interactions. En consecuencia, ahora las líneas que construyen *interactions* solo se subordinaron a este renglón (que abre el archivo):

```python
with open(filename) as f:

```
- Se quitaron las validaciones al final de load_interactions. 

<br>

## Interacción 2. Implementación de argparse para recibir argumentos desde la línea de comando


### Pregunta
¿Cómo puedo implementar el nuevo TODO, para que ahora se utilice argparse para recibir rutas de entrada y salida en la función parse_arguments?

### Respuesta resumida
Puede emplearse `argparse.ArgumentParser()` para aceptar dos argumentos posicionales (input e output) que representan rutas relativas respecto a la raíz del proyecto. A continuación, es menester definir los argumentos que se ocuparán.

### Mi prendizaje
- `argparse` permite que el usuario introduzca las rutas relativas de los archivos de entrada y salida. Ello posibilita que el programa sea más flexible.
- Una vez que defina los argumentos posicionales, debo considerar esos nombres en las líneas que se encargaban de hilar las rutas a la raíz del proyecto y crear, si era necesario, la carpeta del archivo de salida. 


### Modificaciones en el código
- Se importa el módulo argparse al comienzo del programa.
- Se añadieron las siguientes instrucciones para señalar que se pasarán argumentos por línea de comandos. Asimismo, se especifica cuáles argumentos se recibirán:

```python
 parser = argparse.ArgumentParser(description="Rutas relativas (respecto a la raíz del proyecto) de los archivos de entrada y salida.")

# ...

   # Definir los argumentos posicionales.
   parser.add_argument('input', help='Ruta relativa del archivo TSV de entrada.')
   parser.add_argument('output', help='Ruta relativa del archivo TSV de salida.')
   args = parser.parse_args()
```

- Se actualizó el fragmento que vincula la raíz del proyecto con las carpetas de los archivos de entrada y salida (y de ser necesario crea este último repositorio). Ahora, esos procesos se llevan a cabo considerando las rutas brindadas por el usuario, de las cuales se obtendrán sus rutas absolutas para posterior uso del programa. 

```python
filename = os.path.abspath(os.path.join(project_root, args.input))
output_file = os.path.abspath(os.path.join(project_root, args.output))

# ...
   os.makedirs(os.path.dirname(output_file), exist_ok=True)

```

- El nombre de la función ("defining_routes") se convirtió en "parse_arguments".

<br>

## Interacción 3. Adición de un argumento opcional en la función parse_arguments

### Pregunta
¿Debo definir el argumento opcional "min_genes" en parse_arguments o en write_output? ¿Qué opción contribuiría más a la coherencia del código? Considera que ese argumento debe contemplarse al determinar cuáles TFs figurarán en el archivo de salida.

### Respuesta resumida
Es mejor definir todos los argumentos CLI en parse_arguments por coherencia. Esa función podría regresar el valor de args.min_genes, además de los dos returns que ya brinda (las rutas absolutas de los archivos de entrada y salida). Después, ese nuevo return se ocuparía por write_output como un nuevo parámetro al momento de filtrar los TFs que se emplearían para redactar el archivo de salida. 

### Mi aprendizaje
- Es conveniente que todos los argumentos se definan en una misma función al comienzo del programa, aunque se utilizarán en otra parte del código.
- Dado que el valor del nuevo argumento opcional no estará disponible fuera del ámbito local de la primera función, es necesario que sea regresado por parse_arguments. Luego, puede resguardarse en una variable (min_genes) que se definirá en el main() del programa y se pasará como argumento a write_output. 
- Para filtrar los TFs que se incluirán en el archivo de salida, puede recurrise a un condicional que compare si el total de target genes de cada tf, cantidad que se calcula dentro de un for el programa actual, es menor que min_genes; si ese fuera el caso, el programa pasará a la siguiente iteración del bucle. De lo contrario, se ejecutarán los demás renglones, a los cuales les corresponde escribir el archivo de salida.

### Modificaciones en el código
- Adición de un argumento opcional en la función parse_arguments:

```python
parser.add_argument('--min_genes', type=int, default=1, help='Número mínimo de genes asociados a cada uno de los TFs que se desea incluir en el archivo de salida.')

```

- Se estableció que la susodicha función también regresaría el valor de *args.min_genes*:

```python
return filename, output_file, args.min_genes
```

- En el main() del programa, se creó la variable min_genes, que recibirá el valor de args.min_genes y se aprovechará por write_output. 


```python
filename, output_file, min_genes = parse_arguments()

    # ...

    # Se genera el archivo de salida con la información del diccionario.
    write_output(regulon, output_file, min_genes)

```

- Se escribió un condicional dentro del for de write_outputs para que el archivo de salida solo contenga los TFs cuyo total de target genes no sea inferior al valor de *min_genes* introducido por línea de comandos. Entonces, ahora el programa se ve así:

```python
def write_output(regulon, output_file, min_genes):

    # Para que este reporte fuera más conciso, se removieron algunos comentarios presentes en el programa verdadero. 
    # ... 
    with open(output_file, 'w') as outfile:
        outfile.write('TF\tTotal genes\tActivados\tReprimidos\tTipo de efecto regulatorio\tLista de genes\n')
        for TF in sorted(regulon):
            data = regulon[TF]

            # Se acomoda de manera alfabética la lista de target genes de cada TF. Luego, se obtiene la cardinalidad de dicha lista.
            genes = sorted(data["genes"])
            total = len(genes)

            # ...
            if total < min_genes:
                continue   

            # Si se cumplió la condición anterior, las líneas subsecuentes no se ejecutan para la presente iteración del bucle. Ello posibilita que el archivo de salida solo contenga los TFs que regulan cierta cantidad mínima de target genes. 

            # Los target genes se concatenan en un string y solo son separados por comas, seguidas de un espacio.
            lista_genes = ', '.join(genes)

            # Más abajo se continúa recabando la información que se plasmará en el archivo de salida. 

```

<br>


