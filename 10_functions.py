### Funciones ###

def my_function(): # Acá defino la función
    print("Esto es una función")

my_function() # Acá llamo a la función


def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(7, 4)
sum_two_values("7", "4")
sum_two_values(7.3, 4.5)

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value 
    return my_sum

my_result = sum_two_values_with_return(21,1)
print(my_result)


def print_name(name, surname):
    print(f"{name} {surname}")

print_name("Lautaro", "Lovato")


def print_name_with_default(name, surname, alias = "Sin alias"): # Cargo un valor al parametro predeterminado, para poder usar la funcion sin alias 
    print(f"{name} {surname} {alias}")
    
print_name_with_default("Lautaro", "Lovato")
print_name_with_default("Lautaro", "Lovato", "chyno11")


def print_upper_texts(*texts): #Con el * puedo utilizar infinitos parametros, se pueden utilizar una cantidad distinta cada vez que se llame la funcion 
    my_list = []
    for text in texts:
        my_list.append(text.upper())
        
    print(my_list)


print_upper_texts("hola", "Python", "Laudrup")