### Tuplas ###

my_tuple = tuple()
my_other_tuple = (20, 34, 27, 56, 11)

my_tuple = (20, 1.72, "Lautaro", "Lovato")
print(my_tuple)

print(my_tuple[-1])

print(my_tuple.count(20))
print(my_tuple.index("Lautaro")) # nos dice en que posición de la lista se encuentra el elemento que estamos buscando
# las tuplas son inmutables

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[2:4])
# transformo la tupla e una lista, para asi modificarla 
my_tuple = list(my_tuple)

my_tuple[3] = "Herrera"
my_tuple.insert(0, "Azul") 
print(my_tuple)