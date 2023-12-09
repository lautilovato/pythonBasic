### Diccionarios ###

my_dict= dict()
my_other_dict= {}

my_other_dict= {"nombre":"Lautaro", "apellido":"Lovato", "edad":20, 1:"Python"} # nombre-clave, Lautaro-valor
my_dict= {"nombre":"Lautaro", "apellido":"Lovato", "edad":20, "Lenguajes":{"Python","Java","Swift"}}
print(my_dict)
print(my_other_dict)

print(my_dict["nombre"])

my_dict["nombre"] = "Tomás" #se puede modicar el valor de las claves del diccionarios  
print(my_dict["nombre"])

my_dict["calle"] = "Zapiola" #forma de agregar claves al diccionario 
print(my_dict)

del my_dict["calle"] #forma de eliminar claves del diccionario
print(my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = dict.fromkeys(("Nombre", "Altura", 11)) # creo un nuevo diccionario sin valores, pára despues ir agregandoselos
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict) # creo en un diccionario sin valores con las claves de otro diccionario ya existente
print(my_new_dict)

print(my_new_dict.values())