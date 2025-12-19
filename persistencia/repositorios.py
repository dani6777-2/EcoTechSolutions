from .db import Database


class DepartamentoRepo:
    def crear(self, departamento):
        sql = "INSERT INTO departamentos (id, nombre, descripcion, created_at, activo) VALUES (%s, %s, %s, NOW(), TRUE)"
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (departamento.id, departamento.nombre, departamento.descripcion))
            conn.commit()
        finally:
            conn.close()

    def listar_todos(self):
        sql = "SELECT id, nombre, descripcion FROM departamentos"
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
        finally:
            conn.close()

    def obtener_por_id(self, id_):
        sql = "SELECT id, nombre, descripcion FROM departamentos WHERE id=%s"
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (id_,))
                return cur.fetchone()
        finally:
            conn.close()

    def buscar_por_nombre(self, nombre):
        sql = "SELECT id, nombre, descripcion FROM departamentos WHERE nombre LIKE %s"
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (f"%{nombre}%",))
                return cur.fetchall()
        finally:
            conn.close()

    def actualizar(self, id_, cambios: dict):
        campos = []
        valores = []
        for k, v in cambios.items():
            campos.append(f"{k}=%s")
            valores.append(v)
        valores.append(id_)
        sql = f"UPDATE departamentos SET {', '.join(campos)} WHERE id=%s"
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, tuple(valores))
            conn.commit()
        finally:
            conn.close()

    def eliminar(self, id_):
        sql = "DELETE FROM departamentos WHERE id=%s"
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (id_,))
            conn.commit()
        finally:
            conn.close()


class ProyectoRepo:
    def crear(self, proyecto):
        sql = "INSERT INTO proyectos (id, nombre, descripcion, fecha_inicio, fecha_fin, created_at, activo) VALUES (%s,%s,%s,%s,%s,NOW(),TRUE)"
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (proyecto.id, proyecto.nombre, proyecto.descripcion, proyecto.fecha_inicio, proyecto.fecha_fin))
            conn.commit()
        finally:
            conn.close()

    def listar_todos(self):
        sql = "SELECT id, nombre, descripcion, fecha_inicio, fecha_fin FROM proyectos"
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
        finally:
            conn.close()

    def obtener_por_id(self, id_):
        sql = "SELECT id, nombre, descripcion, fecha_inicio, fecha_fin FROM proyectos WHERE id=%s"
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (id_,))
                return cur.fetchone()
        finally:
            conn.close()

    def buscar_por_nombre(self, nombre):
        sql = "SELECT id, nombre, descripcion FROM proyectos WHERE nombre LIKE %s"
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (f"%{nombre}%",))
                return cur.fetchall()
        finally:
            conn.close()

    def actualizar(self, id_, cambios: dict):
        campos = []
        valores = []
        for k, v in cambios.items():
            campos.append(f"{k}=%s")
            valores.append(v)
        valores.append(id_)
        sql = f"UPDATE proyectos SET {', '.join(campos)} WHERE id=%s"
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, tuple(valores))
            conn.commit()
        finally:
            conn.close()

    def eliminar(self, id_):
        sql = "DELETE FROM proyectos WHERE id=%s"
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (id_,))
            conn.commit()
        finally:
            conn.close()


class EmpleadoRepo:
    def crear(self, empleado):
        sql = "INSERT INTO empleados (id, usuario_id, nombre, direccion, telefono, email, fecha_inicio_contrato, salario, departamento_id, created_at) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW())"
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (empleado.id, empleado.usuario_id, empleado.nombre, None, None, empleado.email, empleado.fecha_inicio_contrato, empleado.salario, empleado.departamento_id))
            conn.commit()
        finally:
            conn.close()

    def listar_todos(self):
        sql = "SELECT id, usuario_id, nombre, email, fecha_inicio_contrato, salario, departamento_id FROM empleados"
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
        finally:
            conn.close()

    def obtener_por_id(self, id_):
        sql = "SELECT id, usuario_id, nombre, email, fecha_inicio_contrato, salario, departamento_id FROM empleados WHERE id=%s"
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (id_,))
                return cur.fetchone()
        finally:
            conn.close()

    def buscar_por_nombre(self, nombre):
        sql = "SELECT id, usuario_id, nombre, email FROM empleados WHERE nombre LIKE %s"
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (f"%{nombre}%",))
                return cur.fetchall()
        finally:
            conn.close()

    def actualizar(self, id_, cambios: dict):
        campos = []
        valores = []
        for k, v in cambios.items():
            campos.append(f"{k}=%s")
            valores.append(v)
        valores.append(id_)
        sql = f"UPDATE empleados SET {', '.join(campos)} WHERE id=%s"
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, tuple(valores))
            conn.commit()
        finally:
            conn.close()

    def eliminar(self, id_):
        sql = "DELETE FROM empleados WHERE id=%s"
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (id_,))
            conn.commit()
        finally:
            conn.close()


class LogClimaRepo:
    """Repositorio para gestionar logs de consultas de calidad del aire"""
    
    def crear(self, log_clima):
        """Guarda un nuevo registro de consulta de clima en la base de datos"""
        sql = """
        INSERT INTO logs_clima (
            id, ciudad, pais, aqi, co, no2, o3, so2, pm2_5, pm10, nh3,
            latitud, longitud, usuario_id, proyecto_id, fecha_consulta, created_at
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW(), NOW()
        )
        """
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (
                    log_clima.id,
                    log_clima.ciudad,
                    log_clima.pais,
                    log_clima.aqi,
                    log_clima.co,
                    log_clima.no2,
                    log_clima.o3,
                    log_clima.so2,
                    log_clima.pm2_5,
                    log_clima.pm10,
                    log_clima.nh3,
                    log_clima.latitud,
                    log_clima.longitud,
                    log_clima.usuario_id,
                    log_clima.proyecto_id
                ))
            conn.commit()
        finally:
            conn.close()
    
    def listar_todos(self, limit=50):
        """Obtiene todos los registros de clima (limitado por defecto)"""
        sql = """
        SELECT 
            id, ciudad, pais, aqi, co, no2, o3, so2, pm2_5, pm10, nh3,
            latitud, longitud, usuario_id, proyecto_id, fecha_consulta
        FROM logs_clima 
        ORDER BY fecha_consulta DESC 
        LIMIT %s
        """
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (limit,))
                return cur.fetchall()
        finally:
            conn.close()
    
    def listar_por_ciudad(self, ciudad, limit=50):
        """Obtiene registros filtrados por ciudad"""
        sql = """
        SELECT 
            id, ciudad, pais, aqi, co, no2, o3, so2, pm2_5, pm10, nh3,
            latitud, longitud, usuario_id, proyecto_id, fecha_consulta
        FROM logs_clima 
        WHERE ciudad LIKE %s
        ORDER BY fecha_consulta DESC 
        LIMIT %s
        """
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (f"%{ciudad}%", limit))
                return cur.fetchall()
        finally:
            conn.close()
    
    def obtener_por_id(self, id_):
        """Obtiene un registro específico por su ID"""
        sql = """
        SELECT 
            id, ciudad, pais, aqi, co, no2, o3, so2, pm2_5, pm10, nh3,
            latitud, longitud, usuario_id, proyecto_id, fecha_consulta
        FROM logs_clima 
        WHERE id=%s
        """
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (id_,))
                return cur.fetchone()
        finally:
            conn.close()
    
    def listar_por_usuario(self, usuario_id, limit=50):
        """Obtiene registros de un usuario específico"""
        sql = """
        SELECT 
            id, ciudad, pais, aqi, co, no2, o3, so2, pm2_5, pm10, nh3,
            latitud, longitud, usuario_id, proyecto_id, fecha_consulta
        FROM logs_clima 
        WHERE usuario_id=%s
        ORDER BY fecha_consulta DESC 
        LIMIT %s
        """
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (usuario_id, limit))
                return cur.fetchall()
        finally:
            conn.close()
    
    def obtener_estadisticas_por_ciudad(self, ciudad):
        """Obtiene estadísticas agregadas de una ciudad"""
        sql = """
        SELECT 
            ciudad,
            pais,
            COUNT(*) as total_consultas,
            AVG(aqi) as aqi_promedio,
            MAX(aqi) as aqi_maximo,
            MIN(aqi) as aqi_minimo,
            AVG(pm2_5) as pm2_5_promedio,
            AVG(pm10) as pm10_promedio,
            MAX(fecha_consulta) as ultima_consulta
        FROM logs_clima 
        WHERE ciudad LIKE %s
        GROUP BY ciudad, pais
        """
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (f"%{ciudad}%",))
                return cur.fetchone()
        finally:
            conn.close()
    
    def listar_ciudades_consultadas(self):
        """Obtiene lista de ciudades únicas consultadas"""
        sql = """
        SELECT DISTINCT ciudad, pais, COUNT(*) as consultas
        FROM logs_clima 
        GROUP BY ciudad, pais
        ORDER BY consultas DESC, ciudad ASC
        """
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
        finally:
            conn.close()

