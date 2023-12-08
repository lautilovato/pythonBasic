# this is the first comment 
print("Hola Python")
"""
Este es 
un comentario 
en varias lineas
"""

"""
print(type("Hola Python"))
# el type imprime el tipo de hola Python, en esta caso un string
print(type(5))
print(type(1.4))
print(type(True))
"""
nombre = input("ingrese su nombre: ")
empresa = input("Que empresa prefiere?, Marvel o CapCom: ").upper
inicial = nombre[0]

if (inicial <= "m" and empresa == "MARVEL"):
  print("Usted esta en el grupo A")