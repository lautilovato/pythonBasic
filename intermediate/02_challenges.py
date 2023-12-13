### Challenges ###

"""
EL FAMOSO "FIZZ BUZZ
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""



def x_es_multiplo_de_y(x, y):
    return x % y == 0

def es_multiplo_de_3_y_5(number):
    return number % 3 == 0 and number % 5 == 0

def fizzbuzz():
    for i in range(1,101):
        
        if es_multiplo_de_3_y_5(i):
            print("fizzbuzz \n")

        elif x_es_multiplo_de_y(i, 3):
            print("fizz \n")
        
        elif x_es_multiplo_de_y(i, 5):
            print("buzz \n")

        else:
            print(f"{i} \n")
    

fizzbuzz()

'''
* Escribe una funcion que reciba dos palabras(String) y retorne 
* Verdadero o Falos (Bool) según sean o no anagranmas.
* - Un Anagrama consiste en formar una palabra reordenando TODAS 
* las letras de la palabra inicial
* - No hace falta comprobar que ambas palabras existan 
* - Dos palabras exactamente iguales no son anagramas
'''

def is_anagram(word1, word2):
    
    if word1.lower() == word2.lower():
        return False

    elif sorted(word1.lower()) == sorted(word2.lower()):
        return True
    
    else:
        return False
    

print(is_anagram("hola", "ohal"))

"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    condition = 0
    numbers = []
    while condition  != 50:
        if condition == 1 or condition == 0:
            numbers.append(condition)
            print(condition)
            condition += 1
        else:
            last_number = numbers[-1] + numbers[-2]
            numbers.append(last_number)
            print(last_number)
            condition += 1
       

fibonacci()

'''
* Es un numero primo?
-Escribe un programa que se encargue de comprobar si un numero es o no primo
-Hecho esto, imprime los números primos entre 1 y 100
'''

def is_prime(number):
    divs_enteras = 0
    
    for index in range(1,number + 1):
        if number % index == 0:
            divs_enteras += 1  
    
    return divs_enteras == 2
    
for number in range (1, 101):
    if is_prime(number):
        print(number)

"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def reverse(text):
    new_text = ""
    for index in range(1,len(text) + 1):
        new_text += text[-index]
        
    return new_text

print(reverse("hola que tal"))