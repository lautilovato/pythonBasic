### Exceptions Handling ###

number_one = 5
number_two = "4"

def sumNumbers(n1, n2):
    # try except
    try:
        print(n1 + n2) # el bloque de codigo que puede fallar
    except:
        print("Esta operación no se puede realizar") # si falla el bloque try, se ejecuta este bloque de codigo

#sumNumbers(number_one, number_two)


# try except else finally
try:
    print(number_one + number_two) 
except:
    print("Esta operación no se puede realizar") 
else:
    print("La ejecución continua correctamente") # Se ejecuta si no se prduce una excepción 


# try except else finally
try:
    print(number_one + number_two) 
except:
    print("Esta operación no se puede realizar") 
else:
    print("La ejecución continua correctamente")  
finally:
    print("La ejecución continua") # Este bloque se ejecuta siempre

# el else y el finally son opcionales
#-----------------------------------#

# Excepciones especificas por tipo
try:
    print(number_one + number_two) 
except TypeError:
    print("Esta operación no se puede realizar") # Este bloque se ejecuta si y solo si se produce un TypeError


# se pueden capturar varios errores a la vez

try:
    print(number_one + number_two) 
except TypeError:
    print("Se ha producicido un TypeError") # Este bloque se ejecuta si y solo si se produce un TypeError
except ValueError:
    print("Se ha producicido un ValueError")

# Se puede capturar la información de los errores

try:
    print(number_one + number_two) 
except TypeError as error:
    print(error)

try:
    print(number_one + number_two) 
except ValueError as error:
    print(error)
except Exception as error: # except exception captura cualquier tipo de error
    print(error)    