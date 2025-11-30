from persistencia.repositorios import DepartamentoRepo, ProyectoRepo, EmpleadoRepo


class DepartamentoService:
    def __init__(self):
        self.repo = DepartamentoRepo()

    def crear(self, departamento):
        try:
            self.repo.crear(departamento)
            print("Departamento creado")
        except Exception as e:
            print("Error creando departamento:", e)

    def listar_todos(self):
        return self.repo.listar_todos()

    def obtener_por_id(self, id_):
        return self.repo.obtener_por_id(id_)

    def buscar_por_nombre(self, nombre):
        return self.repo.buscar_por_nombre(nombre)

    def modificar(self, id_, cambios: dict):
        try:
            self.repo.actualizar(id_, cambios)
            print("Departamento actualizado")
        except Exception as e:
            print("Error actualizando departamento:", e)

    def eliminar(self, id_):
        try:
            self.repo.eliminar(id_)
            print("Departamento eliminado")
        except Exception as e:
            print("Error eliminando departamento:", e)


class ProyectoService:
    def __init__(self):
        self.repo = ProyectoRepo()

    def crear(self, proyecto):
        try:
            self.repo.crear(proyecto)
            print("Proyecto creado")
        except Exception as e:
            print("Error creando proyecto:", e)

    def listar_todos(self):
        return self.repo.listar_todos()

    def obtener_por_id(self, id_):
        return self.repo.obtener_por_id(id_)

    def buscar_por_nombre(self, nombre):
        return self.repo.buscar_por_nombre(nombre)

    def modificar(self, id_, cambios: dict):
        try:
            self.repo.actualizar(id_, cambios)
            print("Proyecto actualizado")
        except Exception as e:
            print("Error actualizando proyecto:", e)

    def eliminar(self, id_):
        try:
            self.repo.eliminar(id_)
            print("Proyecto eliminado")
        except Exception as e:
            print("Error eliminando proyecto:", e)


class EmpleadoService:
    def __init__(self):
        self.repo = EmpleadoRepo()

    def crear(self, empleado):
        try:
            self.repo.crear(empleado)
            print("Empleado creado")
        except Exception as e:
            print("Error creando empleado:", e)

    def listar_todos(self):
        return self.repo.listar_todos()

    def obtener_por_id(self, id_):
        return self.repo.obtener_por_id(id_)

    def buscar_por_nombre(self, nombre):
        return self.repo.buscar_por_nombre(nombre)

    def modificar(self, id_, cambios: dict):
        try:
            self.repo.actualizar(id_, cambios)
            print("Empleado actualizado")
        except Exception as e:
            print("Error actualizando empleado:", e)

    def eliminar(self, id_):
        try:
            self.repo.eliminar(id_)
            print("Empleado eliminado")
        except Exception as e:
            print("Error eliminando empleado:", e)
