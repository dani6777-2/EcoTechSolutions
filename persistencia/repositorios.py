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
