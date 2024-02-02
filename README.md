# ATBASH

El link del repositorio es: [GitHub](https://github.com/Germiprogramer/ATBASH.git)

## FORMULA MATEMATICA ATBASH

El cifrado Atbash es una forma simple de cifrado en el cual se invierte el orden del alfabeto. La fórmula matemática para el cifrado Atbash es bastante directa:

Dada una letra en el alfabeto latino, puedes encontrar su equivalente en Atbash utilizando la siguiente fórmula:

**Pi = (N - 1) - Pf**

​
Pi  es la posición de la letra en el alfabeto Atbash.

N es el número total de letras en el alfabeto.

Pf es la posición original de la letra en el alfabeto latino.

## METODO

La lógica detrás de este método es bastante directa:

Identificación de las letras: Primero, se identifican las letras en el texto original.

Asignación de posiciones: Cada letra se asigna a una posición específica en el alfabeto latino estándar.

Inversión de posiciones: La posición de cada letra se invierte utilizando la fórmula Pi = (N - 1) - Pf, donde Pi es la posición en el alfabeto Atbash, N es el número total de letras en el alfabeto, y Pf es la posición original de la letra.

Reemplazo de letras: Finalmente, cada letra se reemplaza con su equivalente en el alfabeto Atbash, según la posición invertida.

La fórmula específica para Atbash es una manera matemática de expresar esta inversión. En esencia, la lógica del método es proporcionar una correspondencia directa entre las letras originales y sus equivalentes invertidos en el alfabeto.

Por ejemplo, utilizando el alfabeto latino:

A (posición original 1) se convierte en Z (posición invertida 26).

B (posición original 2) se convierte en Y (posición invertida 25).

C (posición original 3) se convierte en X (posición invertida 24).

Y así sucesivamente.

Esta lógica simple hace que el cifrado Atbash sea fácil de entender y aplicar.

## SEGURIDAD Y EFECTIVIDAD

El cifrado Atbash no es seguro principalmente porque es un cifrado de sustitución muy simple y fácil de descifrar.

### 1. Fácil de invertir

La estructura del cifrado Atbash es directamente reversible. Al ser un cifrado por sustitución, la relación entre las letras originales y las letras cifradas es fija y conocida.

### 2. Falta de complejidad

Atbash opera simplemente invirtiendo el orden de las letras en el alfabeto, sin introducir ninguna clave secreta ni confusión adicional. La falta de complejidad y la previsibilidad hacen que sea vulnerable a métodos de análisis estadístico y otros enfoques criptoanalíticos.

### 3. Sensibilidad a frecuencias de letras

Al igual que otros cifrados de sustitución simples, el Atbash no oculta las frecuencias de las letras en el mensaje original. Las letras más comunes en el idioma original conservan su frecuencia relativa en el mensaje cifrado, facilitando el análisis de frecuencia para descifrar el mensaje.

### 4. No resiste ataques modernos

Con el avance de las técnicas criptoanalíticas y la potencia computacional moderna, el Atbash se considera obsoleto y fácilmente vencible. Métodos más seguros, como los algoritmos de cifrado simétrico o asimétrico utilizados en la actualidad, están diseñados para resistir ataques más avanzados.

## Mensaje descifrado

**The flag is say we are crazy**
