# Variables
my_string_variable = "My Stirng Variable"
print(my_string_variable)

my_int_variable = 7
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

my_int_to_str_variable= str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Concatenación de variables
print(my_bool_variable, my_int_variable, my_string_variable)
print("Este es el valor de mi variable int:", my_int_variable)

# Algunas Funciones del sistema
print(len(my_string_variable)) # estafuncion cuenta los caracteres 

# Variables en una sola línea (mala práctica)
name, surname, alias, age = "Lautaro", "Lovato", "Laudrup", 20 
print("Me llamo",name, surname, ",Tengo", age, "años", "y mi alias es", alias)


# Inputs

name = input("Cual es tu nombre? ")
age = input("Cuantos años tienes? ")
print(f"Tu nombre es {name}")
print(f"Tu edad es de {age} años")
