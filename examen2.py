import hashlib
import sqlite3

# Función para calcular el hash de una contraseña
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Crear o conectar a la base de datos SQLite
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        nombre TEXT PRIMARY KEY,
        hash_password TEXT
    )
''')
conn.commit()

# Solicitar al usuario ingresar nombre de usuario y contraseña
nombre_usuario = input("Ingrese nombre de usuario: ")
password = input("Ingrese contraseña: ")

# Calcular hash de la contraseña
hash_pass = hash_password(password)

# Insertar usuario y contraseña hash en la base de datos
try:
    cursor.execute('INSERT INTO usuarios VALUES (?, ?)', (nombre_usuario, hash_pass))
    conn.commit()
    print(f'Usuario "{nombre_usuario}" registrado correctamente.')
except sqlite3.IntegrityError:
    print(f'Error: El usuario "{nombre_usuario}" ya existe en la base de datos.')

# Mostrar usuarios y hashes de contraseñas en DB Browser para SQLite
print("\nConsulta de usuarios registrados:")
cursor.execute('SELECT * FROM usuarios')
for row in cursor.fetchall():
    print(row)

# Cerrar la conexión a la base de datos al finalizar
conn.close()
