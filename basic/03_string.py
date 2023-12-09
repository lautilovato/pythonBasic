my_string = "Mi String"
print(len(my_string))

my_new_line_string = "Este es un string\nCon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con Tab"
print(my_tab_string)

# Formateo

name, surname, age = "Lautaro", "Lovato", 20
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age ))
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age ))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres 
lenguage = "Python"
a, b, c, d, e, f = lenguage
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División

lenguage_slice = lenguage[1:3] # son las letras de la uno a la tres sin contar la 3 
print(lenguage_slice)  

# el primer caracter es el numero cero (0)

lenguage_slice = lenguage[1:] 
print(lenguage_slice)  

lenguage_slice = lenguage[0:4]
print(lenguage_slice)      

lenguage_slice = lenguage[3] # hace un print a la letra que se encuentra en la posición 3
print(lenguage_slice)      

lenguage_slice = lenguage[-2] 
print(lenguage_slice)      

# Reverse 

reversed_lenguage = lenguage[::-1] # lo escribe al revés
print(reversed_lenguage)

print(lenguage.capitalize())
print(lenguage.upper())
print(lenguage.lower())
print(lenguage.count("o"))
print(lenguage.isnumeric())
print("3".isnumeric())
print(lenguage.upper().isupper()) #".issuper()" es para comprobart si todo esta escrito er mayusculas.
print(lenguage.capitalize().isupper())
print(lenguage.startswith("Py"))
print(lenguage.startswith("py"))



