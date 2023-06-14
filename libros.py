
import sqlite3
import math
from typing import final
from datetime import datetime


class Conexiones:

    def abrirConexion(self):
        self.conexion = sqlite3.connect("Biblioteca.db")
        self.cursor = self.conexion.cursor()

    def cerrarConexion(self):
        self.conexion.close()


class ProgramaPrincipal:
    # MENU
    def menu(self):
        while True:
            print("\n ----------MENÚ--------------")
            print(" 1-Cargar Libros")
            print(" 2-Modificar precio de un libro")
            print(" 3-Borrar un libro")
            print(" 4-Cargar disponibilidad")
            print(" 5-Listado de Libros")
            print(" 6-Ventas")
            print(" 7-Actualizar precio")
            print(" 8-Registros por fecha")
            print(" 0-Salir del menú")
            print("---------------------------")
            opcion = int(input(" ELIJA UNA OPCIÓN DEL MENÚ ANTERIOR: "))
            

            if opcion > 8 or opcion < 0:
                print("ERROR : Por favor, ingrese un número entre 0 y 8")
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
                elif opcion == 7:
                    self.actualizarPrecio()
                elif opcion == 8:
                    self.registrosAnteriores()
                elif opcion == 0:
                    break
            
    # 1.CARGA DE LIBROS
    def cargarLibros(self):
        isbm = input("Ingrese ISBM: ")
        titulo = input("Ingrese titulo: ")
        autor = input("Ingrese autor: ")
        genero = input("Ingrese género: ")
        precio = float(input("Ingrese precio: "))
        fechaUltimoPrecio = datetime.now()
        cantidadDisponible = int(
            input("Ingrese la cantidad disponible del libro: "))

        miConexion = Conexiones()
        miConexion.abrirConexion()

        try:
            miConexion.cursor.execute("INSERT INTO LIBROS (ISBM, Titulo, Autor, Genero, Precio, FechaUltimoPrecio, CantDisponible) VALUES (?, ?, ?, ?, ?, ?, ?)", (
                isbm, titulo, autor, genero, precio, fechaUltimoPrecio, cantidadDisponible))
            miConexion.conexion.commit()
            print("SUCCESS: Se cargo el libro correctamente")
        except:
            print("ERROR : No se pudo cargar el libro")
        finally:
            miConexion.cerrarConexion()

    # 2.MODIFICAR PRECIO DEL LIBRO
    def modificarLibros(self):
        conexiooon = Conexiones()
        conexiooon.abrirConexion()

        try:
            buscar = int(input("Escriba el ID del libro que desea modificar: "))
            nuevo_precio = float(input("Ingrese el nuevo precio del libro: "))

            libro = conexiooon.cursor.execute(
                "SELECT * FROM LIBROS WHERE ID = ?", (buscar,)).fetchone()
            print("Se encontro el libro")

            if libro:
                confirmacion = int(input("¿Está seguro de realizar la modificación? 1 = Sí / 0 = No: "))

                if confirmacion == 1:
                    conexiooon.cursor.execute(
                        "UPDATE LIBROS SET Precio = ? WHERE ID = ?", (nuevo_precio, buscar))
                    conexiooon.conexion.commit()

                    print("\n[SUCCESS: La modificación ha sido realizada.]")
                else:
                    print("ERROR: Modificación cancelada.")

            else:
                print("ERROR: No se encontró ningún libro con el ID proporcionado.")

        except ValueError:
            print("ERROR: El ID debe ser un número entero.")
        except Exception as e:
            print("ERROR: Ocurrió un error al intentar modificar el libro:", str(e))
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
            print("Se encontro el libro")

            if libro:
                
                confirmarEliminarLibro = int(
                    input("¿Está seguro que desea eliminar este libro de la tabla? 1= SI / 0= NO"))

                if confirmarEliminarLibro == 1:
                    conexiooon.cursor.execute(
                        "DELETE FROM LIBROS WHERE ID = ?", (buscar,)).fetchone()
                    conexiooon.conexion.commit()
                    print("\n[SUCCESS: Se elimino el libro correctamente]")
                else:
                    print("\n[ERROR: Eliminacion cancelada.]")
            else:
                print("No se encontró ningún libro con el ID proporcionado.]")

        except ValueError:
            print("El ID debe ser un número entero.")
        except:
            print("Ocurrió un error al intentar ELIMINAR el libro.")
        finally:
            conexiooon.cerrarConexion()

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
                    print("\n[SUCCESS: La cantidad disponible ha sido actualizada.]")
                else:
                    print("\n[ERROR: Incremento cancelado.]")
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
    def mostrarListado(self):
        conexiooon = Conexiones()
        conexiooon.abrirConexion()

        try:
            libros = conexiooon.cursor.execute(
                "SELECT * FROM LIBROS ORDER BY ID, Autor, Titulo").fetchall()

            print("\n ----- LISTADO DE LIBROS -----")
            for libro in libros:
                print(
                    f"ID: {libro[0]}, Autor: {libro[3]}, Título: {libro[2]}, Cantidad: {libro[7]}, Precio: {libro[4]} ")

        except:
            print("\n[ERROR: Ocurrió un error al mostrar el listado de libros.]")
        finally:
            conexiooon.cerrarConexion()

    # 6.VENTAS
    def ventas(self):
        try:
            libro_vendido = int(input("Escriba el ID del libro vendido: "))
            cant_vendida = int(input("Ingrese cantidad vendida: "))
            fecha = datetime.now()

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
                        print("\n[SUCCES: Registro exitoso]")
                    else:
                        print("\n[ERROR: Registro de venta cancelado]")
                else:
                    print("La cantidad es mayor al stock actual")
            else:
                print("No se encontro el libro con el id ingresado")    
        except Exception as err:
            print("Algo salió mal:", err)
        except:
            print("Algo salio mal")
        finally:
            conexiooon.cerrarConexion()

    # 7.ACTUALIZAR PRECIOS
    def actualizarPrecio(self):
        conexioon = Conexiones()
        conexioon.abrirConexion()

        try:
            porcentaje = float(input("Ingrese el PORCENTAJE"))
            fechaActual = datetime.now()

            libros = conexioon.cursor.execute(
                "SELECT * FROM LIBROS").fetchall()

            for libro in libros:
                conexioon.cursor.execute("INSERT INTO HISTORIAL (ISBM, Titulo, Autor, Genero, Precio, FechaUltimoPrecio, CantDisponible) VALUES (?, ?, ?, ?, ?, ?, ?)", (
                    libro[1], libro[2], libro[3], libro[4], libro[5], libro[6], libro[7]))
                conexioon.conexion.commit()

                nuevoPrecio = libro[5] + (libro[5] * porcentaje / 100)

                conexioon.cursor.execute(
                    "UPDATE LIBROS SET Precio = ? WHERE ID = ?", (nuevoPrecio, libro[0]))
                conexioon.conexion.commit()

                conexioon.cursor.execute(
                    "UPDATE LIBROS SET FechaUltimoPrecio = ?", (fechaActual,))
                conexioon.conexion.commit()

            print("\n[SUCCESS: Precio modificado correctamente]")

        except ValueError as e:
            print("ERROR: ", str(e))
        except Exception as e:
            print("\n[ERROR:Ocurrió un error al actualizar el precio]", str(e))
        finally:
            conexioon.cerrarConexion()

    #8. MOSTRAR REGISTROS ANTERIORES
    def registrosAnteriores(self):
        fecha = input("Por favor, ingrese respetando la siguiente manera (AAAA-MM-DD): ")
        fecha = datetime.strptime(fecha, "%Y-%m-%d")
        conexioon = Conexiones()
        conexioon.abrirConexion()

        try:
            registros = conexioon.cursor.execute("SELECT ID, ISBM, Titulo, FechaUltimoPrecio FROM LIBROS WHERE FechaUltimoPrecio < ?", (fecha,))
            
            if registros:
                print("Registros anteriores a la fecha ingresada:")
                for registro in registros:
                    print("ID:", registro[0])
                    print("ISBN:", registro[1])
                    print("Título:", registro[2])
                    print("Fecha último precio:", registro[3])
                    print("------------------------")
            else:
                print("No existen registros anteriores a la fecha ingresada.")

            conexioon.conexion.commit()
        except Exception as err:
            print("Error al mostrar registros")
            print(err)
        finally:
            conexioon.cerrarConexion()

    # CREAR TABLAS
    def crearTabla(self):
        miConexion = Conexiones()
        miConexion.abrirConexion()
        miConexion.cursor.execute("DROP TABLE IF EXISTS LIBROS")
        miConexion.cursor.execute(
            "CREATE TABLE LIBROS (ID INTEGER PRIMARY KEY AUTOINCREMENT, ISBM VARCHAR(50) UNIQUE, Titulo VARCHAR(50), Autor VARCHAR(50), Genero VARCHAR(50), Precio FLOAT NOT NULL, FechaUltimoPrecio VARCHAR(50), CantDisponible INTEGER)")
        # TABLA VENTAS
        miConexion.cursor.execute("DROP TABLE IF EXISTS VENTAS")
        miConexion.cursor.execute(
            "CREATE TABLE VENTAS (ID INTEGER PRIMARY KEY AUTOINCREMENT,libro_id INTEGER,cantidadVendida INTEGER,fecha VARCHAR(50))")
        miConexion.conexion.commit()
        # TABLA HISTORICA
        miConexion.cursor.execute("DROP TABLE IF EXISTS HISTORIAL")
        miConexion.cursor.execute(
            "CREATE TABLE HISTORIAL (ID INTEGER PRIMARY KEY AUTOINCREMENT, ISBM VARCHAR(50) UNIQUE, Titulo VARCHAR(50), Autor VARCHAR(50), Genero VARCHAR(50), Precio FLOAT NOT NULL, FechaUltimoPrecio VARCHAR(50), CantDisponible INTEGER)"
        )
        miConexion.cerrarConexion()


programa = ProgramaPrincipal()
programa.crearTabla()
programa.menu()
