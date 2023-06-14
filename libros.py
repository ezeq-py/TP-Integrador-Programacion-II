
import sqlite3


class Conexiones:

    def abrirConexion(self):
        self.conexion = sqlite3.connect("Biblioteca.db")
        self.cursor = self.conexion.cursor()


    def cerrarConexion(self):
        self.conexion.close()

<<<<<<< HEAD
class ProgramaPrincipal:
    # MENU
=======
#class Conexiones2:
    #def abrirConexionVentas(self):
        # Conexión a la base de datos de las ventas
      #  self.conexion2 = sqlite3.connect("Ventas.db")
     #   self.cursorVentas = self.conexion2.cursorVentas()
    #def cerrarConexionVentas(self):
        #self.conexion2.close()


class ProgramaPrincipal:
    #MENU
>>>>>>> 72698e8af8616f5ab8ebbdb8f09af41facd71a35
    def menu(self):
        while True:
            print("----------MENÚ--------------")
            print("1-Cargar Libros")
            print("2-Modificar precio de un libro")
            print("3-Borrar un libro")
            print("4-Cargar disponibilidad")
            print("5-Listado de Libros")
            print("6-Ventas")
            print("0-Salir del menú")

            opcion = int(input("Elija una opción:"))

            if opcion > 6 or opcion < 0:
                print("ERROR : Por favor, ingrese un número entre 0 y 5")
            else:
                if opcion == 1:
                    self.cargarLibros()
                elif opcion == 2:
                    self.modificarLibros()
                elif opcion == 3:
                    self.borrarLibro()
                elif opcion == 4:
                    self.cargarDisponibilidad()
                elif opcion == 5:
                    self.mostrarListado()
                elif opcion == 6:
                    self.ventas()

    # 1.CARGA DE LIBROS
    def cargarLibros(self):
        print("hola desde cargar libros")
        isbm = input("Ingrese ISBM")
        titulo = input("Ingrese titulo")
        autor = input("Ingrese autor")
        genero = input("Ingrese género")
        precio = float(input("Ingrese precio"))
        fechaUltimoPrecio = input(
            "Ingrese la fecha del ultimo precio (dd/mm/aaaa)")
        cantidadDisponible = int(
            input("Ingrese la cantidad disponible del libro"))

        miConexion = Conexiones()
        miConexion.abrirConexion()

        try:
            miConexion.cursor.execute("INSERT INTO LIBROS (ISBM, Titulo, Autor, Genero, Precio, FechaUltimoPrecio, CantDisponible) VALUES (?, ?, ?, ?, ?, ?, ?)", (
                isbm, titulo, autor, genero, precio, fechaUltimoPrecio, cantidadDisponible))
            miConexion.conexion.commit()
            print("Se cargo el libro correctamente")
        except:
            print("ERROR : No se pudo cargar el libro")
        finally:
            miConexion.cerrarConexion()

    # 2.MODIFICAR PRECIO DEL LIBRO
    def modificarLibros(self):
        conexiooon = Conexiones()
        conexiooon.abrirConexion()

        try:
            buscar = int(
                input("Escriba el ID del libro que desea modificar: "))
            nuevo_precio = float(input("Ingrese el nuevo precio del libro: "))

            libro = conexiooon.cursor.execute(
                "SELECT * FROM LIBROS WHERE ID = ?", (buscar,)).fetchone()

            if libro:
                print("Se encontro el libro")
                confirmacion = int(
                    input("¿Está seguro de realizar la modificación? 1 = SII RE/0 = No :("))

                if confirmacion == 1:
                    conexiooon.cursor.execute(
                        "UPDATE LIBROS SET Precio = ? WHERE ID = ?", (nuevo_precio, buscar))
                    conexiooon.conexion.commit()

                    print("La MODIFICACIÓN, ha sido REALIZADA")
                else:
                    print("MODIFICACIÓN, CANCELADA")

            else:
                print("No se encontró ningún libro con el ID proporcionado.")

        except ValueError:
            print("El ID debe ser un número entero.")
        except:
            print("Ocurrió un error al intentar MODIFICAR el libro.")
        finally:
            conexiooon.cerrarConexion()

    # 3.BORRAR LIBRO
    def borrarLibro(self):
        conexiooon = Conexiones()
        conexiooon.abrirConexion()
        try:
            buscar = int(input("Escriba el ID del libro que desea eliminar: "))
            libro = conexiooon.cursor.execute(
                "SELECT * FROM LIBROS WHERE ID = ?", (buscar,)).fetchone()

            if libro:
                print("Se encontro el libro")
                confirmarEliminarLibro = int(
                    input("¿Está seguro que desea eliminar este libro de la tabla? 1= SI / 0= NO"))

                if confirmarEliminarLibro == 1:
                    conexiooon.cursor.execute(
                        "DELETE FROM LIBROS WHERE ID = ?", (buscar,)).fetchone()
                    conexiooon.conexion.commit()
                    print("Se ha ELIMINADO el libro")
                else:
                    print("ELIMINACIÓN, CANCELADA")
            else:
                print("No se encontró ningún libro con el ID proporcionado.")

        except ValueError:
            print("El ID debe ser un número entero.")
        except:
            print("Ocurrió un error al intentar ELIMINAR el libro.")
        finally:
            conexiooon.cerrarConexion()

<<<<<<< HEAD
    # 4.CARGAR DISPONIBILIDAD

    def cargarDisponibilidad(self):
        conexiooon = Conexiones()
        conexiooon.abrirConexion()

        try:
            buscar = int(
                input("Escriba el ID del libro que desea modificar el stock: "))
            libro = conexiooon.cursor.execute(
                "SELECT * FROM LIBROS WHERE ID = ?", (buscar,)).fetchone()

            if libro:
                print("Se encontró el libro")
                confirmacionModificarStock = int(
                    input("¿Está seguro de incrementar la cantidad disponible? 1 = Sí / 0 = No: "))

                if confirmacionModificarStock == 1:
                    incrementoLibro = int(
                        input("Ingrese la cantidad a incrementar: "))
                    nueva_cantidad = libro[7] + incrementoLibro
                    conexiooon.cursor.execute(
                        "UPDATE Libros SET CantDisponible = ? WHERE ID = ?", (nueva_cantidad, buscar))
                    conexiooon.conexion.commit()
                    print("La cantidad disponible ha sido actualizada.")
                else:
                    print("Incremento cancelado.")
            else:
                print("No se encontró ningún libro con el ID proporcionado.")

        except ValueError:
            print("El ID y el incremento deben ser números enteros.")
        except Exception as e:
            print(
                "Ocurrió un error al intentar incrementar la cantidad disponible:", str(e))
        finally:
            conexiooon.cerrarConexion()

    # 5.MOSTRAR LA LISTA DE LIBROS
=======
    #5.MOSTRAR LA LISTA DE LIBROS
>>>>>>> 72698e8af8616f5ab8ebbdb8f09af41facd71a35
    def mostrarListado(self):
        conexiooon = Conexiones()
        conexiooon.abrirConexion()

        try:
            libros = conexiooon.cursor.execute(
                "SELECT * FROM LIBROS ORDER BY ID, Autor, Titulo").fetchall()

            print("----- LISTADO DE LIBROS -----")
            for libro in libros:
                print(
                    f"ID: {libro[0]}, Autor: {libro[3]}, Título: {libro[2]}, cantidad: {libro[7]}")

        except:
            print("epaa")
        finally:
            conexiooon.cerrarConexion()

<<<<<<< HEAD
    # 6.VENTAS
    def ventas(self):
        print("Hola desde ventas")
        try:
            libro_vendido = int(input("Escriba el ID del libro vendido: "))
            cant_vendida = int(input("Ingrese cantidad vendida: "))
            fecha = input("Ingrese la fecha de la venta (dd/mm/aaaa): ")

            conexiooon = Conexiones()
            conexiooon.abrirConexion()

            libro = conexiooon.cursor.execute(
                "SELECT * FROM LIBROS WHERE ID = ?", (libro_vendido,)).fetchone()
            if libro:
                if cant_vendida <= libro[7]:
                    confirmacion = int(
                        input("Desea registrar la venta? 1-SI / 0-NO : "))
                    if confirmacion == 1:
                        print("Entro al if perro")
                        cantidad_actual = libro[7]
                        cantidad_restante = cantidad_actual - cant_vendida
                        conexiooon.cursor.execute(
                            "INSERT INTO VENTAS (libro_id, cantidadVendida, fecha) VALUES (?, ?, ?)", (libro_vendido, cant_vendida, fecha))

                        conexiooon.cursor.execute(
                            "UPDATE LIBROS SET CantDisponible = ? WHERE ID = ? ", (cantidad_restante, libro_vendido))

                        conexiooon.conexion.commit()
                        print("Registro EXITOSO")
                    else:
                        print("Registro de venta CANCELADO")
                else:
                    print("La cantidad es mayor al stock actual")
            else:
                print("No se encontro el libro con el id ingresado")
=======
    #6.VENTAS
    def ventas(self):
        print("Hola desde ventas")
        try:
          libro_vendido = int(input("Escriba el ID del libro vendido: "))
          cant_vendida= int(input("Ingrese cantidad vendida: "))
          fecha = input("Ingrese la fecha de la venta (dd/mm/aaaa): ")
          
          conexiooon = Conexiones()
          conexiooon.abrirConexion()
          
          libro = conexiooon.cursor.execute("SELECT * FROM LIBROS WHERE ID = ?", (libro_vendido,)).fetchone()
          if libro:
              if cant_vendida <= libro[7]:
                  confirmacion= int(input("Desea registrar la venta? 1-SI / 0-NO : "))
                  if confirmacion==1:
                    print("Entro al if perro")
                    cantidad_actual = libro[7]
                    cantidad_restante= cantidad_actual - cant_vendida
                    conexiooon.cursor.execute("INSERT INTO VENTAS (libro_id, cantidadVendida, fecha) VALUES (?, ?, ?)", (libro_vendido, cant_vendida, fecha))
                    
                    conexiooon.cursor.execute("UPDATE LIBROS SET CantDisponible = ? WHERE ID = ? ", (cantidad_restante, libro_vendido))
                    
                    conexiooon.conexion.commit()
                    print("Registro EXITOSO")
                  else:
                      print("Registro de venta CANCELADO")
              else:
                  print("La cantidad es mayor al stock actual")
          else:  
              print("No se encontro el libro con el id ingresado")      
>>>>>>> 72698e8af8616f5ab8ebbdb8f09af41facd71a35
        except Exception as err:
            print("Algo salió mal:", err)
        except:
            print("Algo salio mal")
<<<<<<< HEAD
        finally:
            conexiooon.cerrarConexion()

    # 7.ACTUALIZAR PRECIOS
=======
        finally:  
           conexiooon.cerrarConexion()  

    #7.ACTUALIZAR PRECIOS   
>>>>>>> 72698e8af8616f5ab8ebbdb8f09af41facd71a35

    def crearTabla(self):
        miConexion = Conexiones()
        miConexion.abrirConexion()
        miConexion.cursor.execute("DROP TABLE IF EXISTS LIBROS")
<<<<<<< HEAD
        miConexion.cursor.execute(
            "CREATE TABLE LIBROS (ID INTEGER PRIMARY KEY AUTOINCREMENT, ISBM VARCHAR(50) UNIQUE, Titulo VARCHAR(50), Autor VARCHAR(50), Genero VARCHAR(50), Precio FLOAT NOT NULL, FechaUltimoPrecio VARCHAR(50), CantDisponible INTEGER)")
        # TABLA VENTAS
        miConexion.cursor.execute("DROP TABLE IF EXISTS VENTAS")
        miConexion.cursor.execute(
            "CREATE TABLE VENTAS (ID INTEGER PRIMARY KEY AUTOINCREMENT,libro_id INTEGER,cantidadVendida INTEGER,fecha VARCHAR(50))")
=======
        miConexion.cursor.execute("CREATE TABLE LIBROS (ID INTEGER PRIMARY KEY AUTOINCREMENT, ISBM VARCHAR(50) UNIQUE, Titulo VARCHAR(50), Autor VARCHAR(50), Genero VARCHAR(50), Precio FLOAT NOT NULL, FechaUltimoPrecio VARCHAR(50), CantDisponible INTEGER)")
       #TABLA VENTAS
        miConexion.cursor.execute("DROP TABLE IF EXISTS VENTAS")
        miConexion.cursor.execute("CREATE TABLE VENTAS (ID INTEGER PRIMARY KEY AUTOINCREMENT,libro_id INTEGER,cantidadVendida INTEGER,fecha VARCHAR(50))")
>>>>>>> 72698e8af8616f5ab8ebbdb8f09af41facd71a35
        miConexion.conexion.commit()
        miConexion.cerrarConexion()
    

programa = ProgramaPrincipal()
programa.crearTabla()
programa.menu()
