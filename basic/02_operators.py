# Operadores artimeticos 

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(5 / 2)
print(10 % 2) # el módulo describe el resto de la división}
print(10 // 3) # intenta apoxima el resultado a un número entero
print( 2 ** 3) # 2 elevado a la 3

print("Hola " + "Python")
print("Hola " + str(2))
print("Hola" * 4)

# Operadores comparativos 

print(3 < 4)
print(3 > 4)
print(3 <= 4)
print(3 >= 4)
print(3 == 4)
print(3 !=   4)

# Operadores Lógicos
print(3 > 4 and "hola" > "Python")
print(3 > 4 or "hola" > "Python")
print(not(3 > 4))

#ejercicio 
nota_1 = float(input("nota del primer parcial= "))
nota_2 = float(input("nota del segundo parcial= "))
nota_final = float(((4 * nota_1  + 6 * nota_2 ) / 10))

print(nota_final)