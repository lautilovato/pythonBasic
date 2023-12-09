### Classes ###

class Person:
    def __init__(self, name, surname, alias = "Sin alias"): # Constructor de clase
        self.name = name # Variable publica, se puede acceder y modificarla
        self.__surname = surname # Con el guion bajo, la variable es priovada y no se puede modificar
        self.full_name = f"{name} {surname} ({alias})"    
        
    def get_surname(self):
        return self.__surname

    def walk(self): #Estos son los mensajes que sabe responder la clase persona
        print(f"{self.name} {self.__surname} está caminando")

    def greet(self):
        print(f"Hola!, mi nombre es {self.name}")


my_person = Person("Lautaro", "Lovato")


print(my_person.full_name)
my_person.walk()


my_other_person = Person("Aliccia", "Herrera", "Dele")

print(my_other_person.full_name)

my_other_person.full_name = "Changuito Zeballos" # Puedo modificar el objeto una vez creado

print(my_other_person.full_name)

print(my_other_person.get_surname())

