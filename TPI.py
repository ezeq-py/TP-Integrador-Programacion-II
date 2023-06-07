import datetime
import sqlite3

class ProgramaPrincipal:

    def menu(self):
        while True:
            print("Bienvenidos a la biblioteca!")
            print("1- Cargar libros")
            print("2- Modificar Precio")
            print("3- Borrar un libro")
            print("4- Cargar")
            print("5- Listado de libros")
            #APROBACION DIRECTA
            print("6- Ventas")
            print("7- Actualizar precio")
            print("8- Algo largo que dice ahi jajaja")
            nro = int(input("Por favor ingrese un número"))

#Definimos libro y le damos sus atributos
class Libro:
    id_autoincremental = 0

    def __init__(self, isbn, titulo, autor, genero, precio, fecha_ultimo_precio, cant_disponible):
        self.id = Libro.generar_id()
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.precio = precio
        self.fecha_ultimo_precio = fecha_ultimo_precio
        self.cant_disponible = cant_disponible

    @classmethod
    def generar_id(cls):
        cls.id_autoincremental += 1
        return cls.id_autoincremental
##############################

#Intento de carga 
def cargaLibros():
 isbn = input("Ingrese el ISBN del libro: ")
 titulo = input("Ingrese el título del libro: ")
 autor = input("Ingrese el autor del libro: ")
 genero = input("Ingrese el género del libro: ")
 precio = float(input("Ingrese el precio del libro: "))
 fecha_ultimo_precio = input("Ingrese la fecha del último precio (YYYY-MM-DD): ")
 cant_disponible = int(input("Ingrese la cantidad disponible del libro: "))

 libro = Libro(isbn, titulo, autor, genero, precio, fecha_ultimo_precio, cant_disponible)

#Intento de modificacion de id
def modificar_precio(self, nuevo_precio):
        nuevo_precio = float(input("Ingrese el nuevo precio del libro: "))
        confirmacion = input(f"¿Estás seguro que deseas modificar el precio del libro '{self.titulo}'? (S/N): ")
        if confirmacion.upper() == "S":
            self.precio = nuevo_precio
            self.fecha_ultimo_precio = datetime.now().strftime("%Y-%m-%d")
            print("El precio del libro ha sido modificado exitosamente.")
        else:
            print("La modificación del precio del libro ha sido cancelada.")      

########################################            

# Modificar el precio del libro
libro.modificar_precio(nuevo_precio)

############################################



