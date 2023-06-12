# Tup-Programacion.2_Trabajo-Integrador-Final

Descripción:
El presente proyecto consiste en el desarrollo de un sistema de gestión para la primera casa física de Buscalibre en Rosario.
El objetivo principal de este sistema es integrar una base de datos utilizando SQLite para gestionar de manera eficiente la información relacionada con el inventario de libros, ventas, clientes y proveedores. La base de datos será el núcleo central del sistema, permitiendo un almacenamiento confiable y un acceso rápido a los datos necesarios para las operaciones diarias de la casa física.

Funcionalidades:
1. Cargar Libros: Permite agregar nuevos libros al inventario de la tienda, ingresando los datos como ID, ISBN, Título, Autor, Género, Precio, Fecha de Último Precio y Cantidad Disponible. El ISBN será único e irrepetible, y el ID se generará automáticamente como clave primaria y autoincremental.
2. Modificar precio de un libro: Permite modificar el precio de un libro existente en el inventario, ingresando su ID. Antes de ejecutar la acción, se solicitará una confirmación al usuario para asegurar la corrección de la actualización.
3. Borrar un libro: Permite eliminar un libro del inventario, ingresando su ID. Antes de ejecutar la acción, se solicitará una confirmación al usuario para evitar eliminaciones accidentales.
4. Cargar disponibilidad: Permite incrementar la cantidad disponible de un libro, ingresando su ID. Esto resulta útil para reflejar nuevas existencias del libro en la tienda física.
5. Listado de Libros: Muestra un listado ordenado de todos los libros en el inventario, ya sea por ID, autor o título. Esto permite tener una visión completa y ordenada de los libros disponibles.
6. Salir del menú: Permite salir del sistema de gestión y finalizar la ejecución del programa.

Tecnologías utilizadas:
Lenguaje de programación: Python
Base de datos: SQLite