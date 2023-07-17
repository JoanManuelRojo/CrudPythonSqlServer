# Importa el driver para la conexión de Python a SQL Server

import cursor as cursor
import pyodbc
import self as self

import InterfazGrafica


# Se ejecuta el constructor para que se haga la conexión a la base de datos

class sqlServerCon:

    def __init__(self):
        # Conexión a SQL Server
        server = 'localhost'
        bd = 'CrucerosRA'
        usuario = 'sa'
        pw = 'Rammstein27n'
        try:
            self.conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                           'SERVER=' + server + ';'
                                                                'DATABASE=' + bd + ';'
                                                                                   'UID=' + usuario + ';'
                                                                                                      'PWD=' + pw + ';')
            print('Conexión exitosa a la base de datos')
        except pyodbc.Error as e:
            print('Error en la conexión')

    # Consulta a la base de datos

    # Señala acción a la base de datos y controla la query que se envía

    def crearUsuario(self, id, nombre, clave, apellido, direccion, comentarios):
        # cursorCrearUsuario = self.conexion.cursor(id, nombre, clave, apellido, direccion, comentarios)

        cursorCrearUsuario = self.conexion.cursor()
        queryCrearUsuario = f"INSERT INTO Seguridad(ID, Nombre, Contraseña, Apellido, Direccion, Comentarios)" \
                            f"VALUES ({id}, '{nombre}', '{clave}','{apellido}','{direccion}','{comentarios}')"

        # Se ejecuta la query y se envía a la base de datos
        cursorCrearUsuario.execute(queryCrearUsuario)
        self.conexion.commit()

        # Se cierra la conexión del cursor y la conexión a la base de datos
        cursorCrearUsuario.close()
        self.conexion.close()


   # def mostrarUsuario(self, id):
       # cursorMostrarUsuario = self.conexion.cursor()
      #  queryConsulta = f"SELECT * FROM Seguridad WHERE ID = {id};"
     #   cursorMostrarUsuario.execute(queryConsulta)
    #    Seguridad = cursorMostrarUsuario.fetchone()
    #        while Seguridad:
   #             print(Seguridad)
  #              Seguridad = cursorMostrarUsuario.fetchone()
    # Se cierra el cursor y la conexión a la base de datos
 #           cursorMostrarUsuario.close()
#            self.conexion.close()

    def mostrarUsuario(self, id):
        cursorMostrarUsuario = self.conexion.cursor()
        queryConsulta = f"SELECT * FROM Seguridad WHERE ID = {id};"
        cursorMostrarUsuario.execute(queryConsulta)
        Seguridad = cursorMostrarUsuario.fetchone()
        while Seguridad:
            print(Seguridad)
            Seguridad = cursorMostrarUsuario.fetchone()

        # Se cierra el cursor y la conexión a la base de datos
        cursorMostrarUsuario.close()
        self.conexion.close()

        return queryConsulta



    def modificarUsuario(self):
        cursorModificarUsuario = self.conexion.cursor()
        queryModificarUsuario = ""
        cursorModificarUsuario.execute(queryModificarUsuario)

        cursorModificarUsuario.close()
        self.conexion.close()


    def eliminarUsuario(self):
        cursorEliminarUsuario = self.conexion.cursor()
        queryEliminarUsuario = ""
        cursorEliminarUsuario.execute(queryEliminarUsuario)

        cursorEliminarUsuario.close()
        self.conexion.close()
