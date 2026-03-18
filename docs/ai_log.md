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


