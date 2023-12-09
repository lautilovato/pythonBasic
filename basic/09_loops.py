### Loops ###

# While

my_condition = 0 

while my_condition < 10:
    print(my_condition)
    my_condition += 1 ## Es igual a:  my_condition = my_condition + 1
else: #Este else pertence al while, y es ocpional
    print("Mi condicion es mayor o igual a 10")

my_condition = 10

while my_condition < 20: 
        print(my_condition)
        my_condition += 1
        if my_condition == 15:
             print("Se detiene la ejecución")
             break 
        

# For

my_list = [20, 11, 34, 67]
    
for element in my_list:
     print(element)

for element in my_list:
     print(element)
     if element == 11:
          print("El bucle finalizará")
          break # se puede salir del bucle con un break
