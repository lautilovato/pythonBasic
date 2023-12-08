### Listas ###  

my_list = list()

my_other_list = []

print(len(my_list))

my_list = [20, 11, 34, 67]

print(len(my_list))

my_other_list = [20, 1.72, "Lautaro", "Lovato"]

print(type(my_other_list))

print(my_other_list[0]) # imprime el primer elemento de la lista 
print(my_other_list[-2]) # lee de atras para adelante, siempre comenzando del -1 

print(my_other_list.count("Lautaro"))
print(my_other_list.count("Pedro"))

age, height, name, surname = my_other_list
print(name)

print(my_list + my_other_list)

my_other_list.append("LaudrupCORP") # con el append se agrega un elemnto a la lista, en este caso al final de la misma 
print(my_other_list)

my_other_list.insert(1,"Azul") # con el insert se agrega un elemnto a la lista  pero en este caso le decimos la posición en la que queremos que se ubique 
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_list.pop() # el pop sin parametro elimina el ultimo elemento de la lista 
print(my_list)

my_list.pop(2) # el pop con parametro elimina el elemento que se encuentre en la posición que nosotos pedimos con el parametro
print(my_list)

my_list = [20, 11, 34, 67]
print(my_list.pop()) # utilizando el pop directamente en el print da como resultado el elemento que se retira de la lista  

del my_list[0] # esta es otra manera de retirar un elementoi de la lista 
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)

print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort() # el sort en este caso ordena la lista con los numeros de menor a mayor 
print(my_new_list)

my_other_list[1] = "Rojo" # De esta manera reeemplazamos un elemento de la lista por el que nosotros queramos 
print(my_other_list)


