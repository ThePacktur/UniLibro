import mysql.connector
from mysql.connector import Error

class BibliotecaDAO:
    def __init__(self, db_config):
        """ Inicializa el DAO con la conexión a la base de datos """
        self.connection = self.create_connection(db_config)
        self.create_tables()  # Crear las tablas al iniciar

    def create_connection(self, db_config):
        """ Crea una conexión a la base de datos MySQL """
        try:
            conn = mysql.connector.connect(**db_config)
            if conn.is_connected():
                print("Conexión establecida a la base de datos.")
            return conn
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def create_tables(self):
        """ Crea las tablas usuarios y deudores si no existen """
        create_usuarios_table = '''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                tipo VARCHAR(50) NOT NULL,
                nombre VARCHAR(100) NOT NULL,
                rut VARCHAR(20) UNIQUE NOT NULL,
                contacto VARCHAR(50) NOT NULL
            )
        '''
        create_deudores_table = '''
            CREATE TABLE IF NOT EXISTS deudores (
                id INT AUTO_INCREMENT PRIMARY KEY,
                rut_usuario VARCHAR(20) UNIQUE NOT NULL,
                FOREIGN KEY (rut_usuario) REFERENCES usuarios(rut)
            )
        '''
        create_libros_table = '''
            CREATE TABLE IF NOT EXISTS libros (
                codigo INT AUTO_INCREMENT PRIMARY KEY,
                titulo VARCHAR(100) NOT NULL,
                autor VARCHAR(100) NOT NULL,
                stock INT NOT NULL
            )
        '''
        create_prestamos_table = '''
            CREATE TABLE IF NOT EXISTS prestamos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                libro_id INT NOT NULL,
                usuario_id INT NOT NULL,
                fecha_prestamo DATE NOT NULL,
                fecha_devolucion DATE NOT NULL,
                renovaciones INT NOT NULL,
                FOREIGN KEY (libro_id) REFERENCES libros(codigo),
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
            )
        '''
        self.create_table(create_usuarios_table)
        self.create_table(create_deudores_table)
        self.create_table(create_libros_table)
        self.create_table(create_prestamos_table)

    def create_table(self, create_table_sql):
        """ Crea una tabla usando la sentencia SQL pasada como argumento """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Tabla creada exitosamente.")
        except Error as e:
            print(f"Error al crear la tabla: {e}")

    def insert_libro(self, libro):
        """ Inserta un libro en la tabla de libros """
        sql = ''' INSERT INTO libros(codigo, titulo, autor, stock)
                  VALUES(%s, %s, %s, %s) '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, libro)
            self.connection.commit()
            print("Libro agregado exitosamente.")
        except Error as e:
            print(f"Error al insertar libro: {e}")

    def select_libro_by_codigo(self, codigo):
        """ Selecciona un libro por su código """
        sql = ''' SELECT * FROM libros WHERE codigo=%s '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (codigo,))
            libro = cursor.fetchone()
            return libro
        except Error as e:
            print(f"Error al seleccionar libro: {e}")
            return None

    def update_libro_stock(self, codigo, stock):
        """ Actualiza el stock de un libro """
        sql = ''' UPDATE libros
                  SET stock = %s
                  WHERE codigo = %s '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (stock, codigo))
            self.connection.commit()
            print("Stock del libro actualizado exitosamente.")
        except Error as e:
            print(f"Error al actualizar el stock del libro: {e}")

    def delete_libro(self, codigo):
        """ Elimina un libro por su código """
        sql = ''' DELETE FROM libros WHERE codigo = %s '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (codigo,))
            self.connection.commit()
            print("Libro eliminado exitosamente.")
        except Error as e:
            print(f"Error al eliminar el libro: {e}")

    def insert_usuario(self, usuario):
        """ Inserta un usuario en la tabla de usuarios """
        sql = ''' INSERT INTO usuarios(tipo, nombre, rut, contacto)
                  VALUES(%s, %s, %s, %s) '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, usuario)
            self.connection.commit()
            print("Usuario registrado exitosamente.")
        except Error as e:
            print(f"Error al insertar usuario: {e}")

    def registrar_deudor(self, rut_usuario):
        """ Registra un usuario como deudor en la tabla de deudores """
        sql = ''' INSERT INTO deudores(rut_usuario)
                  VALUES(%s) '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (rut_usuario,))
            self.connection.commit()
            print("Usuario registrado como deudor exitosamente.")
        except Error as e:
            print(f"Error al registrar deudor: {e}")

    def buscar_usuario_por_rut(self, rut):
        """ Busca un usuario por su rut """
        sql = ''' SELECT * FROM usuarios WHERE rut=%s '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (rut,))
            usuario = cursor.fetchone()
            return usuario
        except Error as e:
            print(f"Error al buscar usuario por rut: {e}")
            return None