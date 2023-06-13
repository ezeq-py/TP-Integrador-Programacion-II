
import sqlite3

class Conexiones:
    
    def abrirConexion(self):
        self.conexion = sqlite3.connect("Biblioteca.db")
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
                elif opcion == 2:
                    self.modificarLibros()
                elif opcion == 3:
                    self.borrarLibro()
                elif opcion == 5:
                    self.mostrarListado()

    #CARGA DE LIBROS

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

    #MODIFICAR PRECIO DEL LIBRO

    def modificarLibros(self):

        conexiooon = Conexiones()
        conexiooon.abrirConexion()

        try:
            buscar = int(input("Escriba el ID del libro que desea modificar: "))
            nuevo_precio = float(input("Ingrese el nuevo precio del libro: "))

            libro = conexiooon.cursor.execute("SELECT * FROM LIBROS WHERE ID = ?", (buscar,)).fetchone()

            if libro:
                print("Se encontro el libro")
                confirmacion = int(input("¿Está seguro de realizar la modificación? 1 = SII RE/0 = No :("))

                if confirmacion == 1:
                    conexiooon.cursor.execute("UPDATE LIBROS SET Precio = ? WHERE ID = ?", (nuevo_precio, buscar))
                    conexiooon.conexion.commit()

                    print("La MODIFICACIÓN, ha sido REALIZADA")
                else:
                    print("MODIFICACIÓN, CANCELADA")

            else:
                print("No se encontró ningún libro con el ID proporcionado.")

        except ValueError:
            print("El ID debe ser un número entero.")
        except:
            print("Ocurrió un error al intentar modificar el libro.")
        finally:
            conexiooon.cerrarConexion()

    #BORRAR LIBRO

    # def borrarLibro(self):
    #     conexiooon = Conexiones()
    #     conexiooon.abrirConexion()

        #jeeeeeeeeeejejejejej aca hara cosas melo





    #MOSTRAR LA LISTA DE LIBROS

    def mostrarListado(self):
        conexiooon = Conexiones()
        conexiooon.abrirConexion()

        try:
            libros = conexiooon.cursor.execute("SELECT * FROM LIBROS ORDER BY ID, Autor, Titulo").fetchall()

            print("----- LISTADO DE LIBROS -----")
            for libro in libros:
                print(f"ID: {libro[0]}, Autor: {libro[3]}, Título: {libro[2]}, cantidad: {libro[7]}")

        except:
            print("epaa")
        finally:
            conexiooon.cerrarConexion()

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
