### Sets ### 

my_set = set()
my_other_set = {} # inicialmente es un diccionario

my_other_set = {"Lautaro", "Lovato", 20}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Laudrup")
print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("Laudrup")
print(my_other_set) # Un set no admite elementos repetidos

print("Lautaro" in my_other_set)
print("pedro" in my_other_set)

my_other_set.remove("Lovato")
print(my_other_set)

my_other_set.update(my_set)  
print(my_other_set)

my_other_set.clear()
print(my_other_set)

my_set = {"Lautaro", "Lovato", 20}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"python", "java", "html"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.difference(my_set))