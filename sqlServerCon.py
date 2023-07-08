'''# Importa el driver para la conexión de Python a SQL Server
import pyodbc

# Conexión a SQL Server. Datos del servidor y credenciales de usuario

server = 'localhost'
bd = 'CrucerosRA'
usuario = 'sa'
pw = ''

try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                              'SERVER='+server+';'
                              'DATABASE='+bd+';'
                              'UID='+usuario+';'
                              'PWD='+pw+';')
    print('Conexión exitosa a la base de datos')

except:

    print('Error en la conexión')

# Querys

# Consulta Select

def ConsultaSelect():
    cursor = conexion.cursor()
    cursor.execute("Select * FROM Seguridad WHERE ID=1;")

    Seguridad


    cursor.close()
    conexion.close()'''


import pyodbc
import pyodbc as odbc # pip install pypyodbc

#Conexión a SQL Server

server = 'localhost'
bd = 'CrucerosRA'
usuario='sa'
pw='Rammstein27n'

try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                              'SERVER='+server+';'
                              'DATABASE='+bd+';'
                              'UID='+usuario+';'
                              'PWD='+pw+';')
    print('Conexión exitosa a la base de datos')

except:

    print('Error en la conexión')


# Consulta a la base de datos

# Señala acción a la base de datos y controla la query que se envía
cursor = conexion.cursor()
queryConsulta = "Select * FROM Seguridad WHERE ID=1;"
cursor.execute(queryConsulta)


Seguridad = cursor.fetchone()

while Seguridad:
    print(Seguridad)
    Seguridad = cursor.fetchone()


# Se cierra el cursor y la conexión a la base de datos

cursor.close()
conexion.close()
