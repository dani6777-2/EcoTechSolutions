"""Script de verificación de conexión a MySQL"""
from persistencia.db import Database

conn = Database.get_connection()
cur = conn.cursor()
cur.execute('SHOW TABLES')
tables = cur.fetchall()
print(f'✓ Conexión exitosa! Base de datos con {len(tables)} tablas')
for t in tables:
    print(f"  - {t['Tables_in_ecotech_management']}")
conn.close()
