"""Repositorios para autenticación y gestión de usuarios"""
from persistencia.db import Database


class UsuarioRepo:
    def crear(self, usuario):
        """Crea un nuevo usuario en la base de datos"""
        sql = """INSERT INTO usuarios (id, nombre_usuario, contrasena_cifrada, salt, rol_id, 
                 fecha_creacion, activo) VALUES (%s, %s, %s, %s, %s, NOW(), %s)"""
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (usuario.id, usuario.nombre_usuario, 
                                 usuario.contrasena_cifrada, usuario.salt, 
                                 usuario.rol_id, usuario.activo))
            conn.commit()
        finally:
            conn.close()
    
    def obtener_por_nombre_usuario(self, nombre_usuario):
        """Obtiene un usuario por su nombre de usuario con información del rol"""
        sql = """SELECT u.id, u.nombre_usuario, u.contrasena_cifrada, u.salt, 
                        u.rol_id, u.activo, r.nivel_permisos, r.nombre as nombre_rol
                 FROM usuarios u
                 JOIN roles r ON u.rol_id = r.id
                 WHERE u.nombre_usuario = %s"""
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (nombre_usuario,))
                return cur.fetchone()
        finally:
            conn.close()
    
    def obtener_por_id(self, id_):
        """Obtiene un usuario por su ID"""
        sql = """SELECT id, nombre_usuario, contrasena_cifrada, salt, rol_id, activo 
                 FROM usuarios WHERE id = %s"""
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (id_,))
                return cur.fetchone()
        finally:
            conn.close()
    
    def listar_todos(self):
        """Lista todos los usuarios (sin contraseñas)"""
        sql = """SELECT id, nombre_usuario, rol_id, activo, fecha_creacion 
                 FROM usuarios ORDER BY fecha_creacion DESC"""
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
        finally:
            conn.close()
    
    def actualizar_ultimo_login(self, id_):
        """Actualiza la fecha del último login"""
        sql = "UPDATE usuarios SET ultimo_login = NOW() WHERE id = %s"
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (id_,))
            conn.commit()
        finally:
            conn.close()
    
    def cambiar_contrasena(self, id_, nueva_contrasena_cifrada, nuevo_salt):
        """Cambia la contraseña de un usuario"""
        sql = "UPDATE usuarios SET contrasena_cifrada = %s, salt = %s WHERE id = %s"
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (nueva_contrasena_cifrada, nuevo_salt, id_))
            conn.commit()
        finally:
            conn.close()
    
    def actualizar_estado(self, id_, activo):
        """Activa o desactiva un usuario"""
        sql = "UPDATE usuarios SET activo = %s WHERE id = %s"
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (activo, id_))
            conn.commit()
        finally:
            conn.close()


class RolRepo:
    def crear(self, rol):
        """Crea un nuevo rol"""
        sql = """INSERT INTO roles (id, nombre, descripcion, nivel_permisos, created_at, activo) 
                 VALUES (%s, %s, %s, %s, NOW(), %s)"""
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (rol.id, rol.nombre, rol.descripcion, 
                                 rol.nivel_permisos, rol.activo))
            conn.commit()
        finally:
            conn.close()
    
    def listar_todos(self):
        """Lista todos los roles"""
        sql = "SELECT id, nombre, descripcion, nivel_permisos FROM roles WHERE activo = TRUE"
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
        finally:
            conn.close()
    
    def obtener_por_id(self, id_):
        """Obtiene un rol por su ID"""
        sql = "SELECT id, nombre, descripcion, nivel_permisos FROM roles WHERE id = %s"
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (id_,))
                return cur.fetchone()
        finally:
            conn.close()
