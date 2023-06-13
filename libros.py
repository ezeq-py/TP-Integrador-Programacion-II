
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
            elif opcion == 1:
                    self.cargarLibros()
            elif opcion == 2:
                isbm_buscado: input("Ingrese el isbm del libro que desea modificar: ")
                nuevo_precio: input("Ingrese el nuevo precio: ")
                self.modificar_libro(isbm_buscado, nuevo_precio)

                                   
        
    def cargarLibros(self):
        print("hola desde cargar libros")
        isbm = input("Ingrese ISBM: ")
        titulo = input("Ingrese titulo: ")
        autor = input("Ingrese autor: ")
        genero = input("Ingrese género: ")
        precio = float(input("Ingrese precio: "))
        fechaUltimoPrecio = input("Ingrese la fecha del ultimo precio (dd/mm/aaaa): ")
        cantidadDisponible = int(input("Ingrese la cantidad disponible del libro: "))

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

    def modificar_libro(self, isbm_buscado, nuevo_precio):
        miConexion = Conexiones()
        miConexion.abrirConexion()
        try:
            miConexion.cursor.execute(
                 "UPDATE LIBROS SET precio = ? WHERE ISBN = ?",
                (nuevo_precio, isbm_buscado),
            )
            miConexion.miConexion.commit()
            print("Libro modificado correctamente")
        except Exception as err:
            print("Error al modificar un libro")
            print(err)
        finally:
            miConexion.cerrarConexion()

    def borrar_libro(self, isbm_buscado):
        miConexion = Conexiones()
        miConexion.abrirConexion()
        try:
             miConexion.cursor.execute(
                "DELETE FROM LIBROS WHERE ISBN = ?",
                (isbm_buscado),
             )
             miConexion.miConexion.commit()
             print("Libro eliminado correctamente")
        except:
            print("Error al eliminar el libro")
        finally:
            miConexion.cerrarConexion()

    def modificar_cant(self, isbm_buscado, nueva_cantidad):
        miConexion = Conexiones()
        miConexion.abrirConexion()

        try:
            miConexion.cursor.execute(
            "UPDATE LIBROS SET CantDisponible = ? WHERE ISBN = ?",
                (nueva_cantidad, isbm_buscado),
            )
            print("La cantidad disponible ha sido actualizada ")
        except:
            print("Hubo un error al actualizar la cantidad nueva")
        finally:
            miConexion.cerrarConexion()

    #def mostrar_libros(self): Calculo que es un for seleccionando lo de la tabla

programa = ProgramaPrincipal()
programa.crearTabla()
programa.menu()
