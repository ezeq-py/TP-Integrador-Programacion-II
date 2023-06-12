
import sqlite3

class Conexiones:
    
    def abrirConexion(self):
        self.conexion = sqlite3.connect("Biblioteca")
        self.cursor = self.conexion.cursor()

    def cerrarConexion(self):
        self.conexion.close()

class ProgramaPrincipal:

    def menu(self):
        while True:
            print("----------MENÚ--------------")
            print("1-Cargar Libros")
            print("2-Modificar precio de un libro")
            print("3-Borrar un libro")
            print("4-Cargar disponibilidad")
            print("5-Listado de Libros")
            print("0-Salir del menú")

            opcion = int(input("Elija una opción:"))

            if opcion > 5 or opcion < 0:
                print("ERROR : Por favor, ingrese un número entre 0 y 5")
            else:
                if opcion == 1:
                    self.cargarLibros()

    def cargarLibros(self):
        print("hola desde cargar libros")
        isbm = input("Ingrese ISBM")
        titulo = input("Ingrese titulo")
        autor = input("Ingrese autor")
        genero = input("Ingrese género")
        precio = float(input("Ingrese precio"))
        fechaUltimoPrecio = input("Ingrese la fecha del ultimo precio (dd/mm/aaaa)")
        cantidadDisponible = int(input("Ingrese la cantidad disponible del libro"))

        miConexion = Conexiones()
        miConexion.abrirConexion()

        try:
            miConexion.cursor.execute("INSERT INTO LIBROS (ISBM, Titulo, Autor, Genero, Precio, FechaUltimoPrecio, CantDisponible) VALUES (?, ?, ?, ?, ?, ?, ?)", (isbm, titulo, autor, genero, precio, fechaUltimoPrecio, cantidadDisponible))
            miConexion.conexion.commit()
            print("Se cargo el libro correctamente")
        except:
            print("ERROR : No se pudo cargar el libro")
        finally:
            miConexion.cerrarConexion()




    def crearTabla(self):
        miConexion = Conexiones()
        miConexion.abrirConexion()
        miConexion.cursor.execute("DROP TABLE IF EXISTS LIBROS")
        miConexion.cursor.execute("CREATE TABLE LIBROS (ID INTEGER PRIMARY KEY AUTOINCREMENT, ISBM VARCHAR(50) UNIQUE, Titulo VARCHAR(50), Autor VARCHAR(50), Genero VARCHAR(50), Precio FLOAT NOT NULL, FechaUltimoPrecio VARCHAR(50), CantDisponible INTEGER)")
        miConexion.conexion.commit()
        miConexion.cerrarConexion()



programa = ProgramaPrincipal()
programa.crearTabla()
programa.menu()
