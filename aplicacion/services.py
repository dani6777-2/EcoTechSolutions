from persistencia.repositorios import DepartamentoRepo, ProyectoRepo, EmpleadoRepo
from aplicacion.api_client import EcoAPIClient
from presentacion.ui_helpers import UI


class DepartamentoService:
    def __init__(self):
        self.repo = DepartamentoRepo()

    def crear(self, departamento):
        try:
            self.repo.crear(departamento)
            UI.print_success("Departamento creado")
        except Exception as e:
            UI.print_error(f"Error creando departamento: {e}")

    def listar_todos(self):
        return self.repo.listar_todos()

    def obtener_por_id(self, id_):
        return self.repo.obtener_por_id(id_)

    def buscar_por_nombre(self, nombre):
        return self.repo.buscar_por_nombre(nombre)

    def modificar(self, id_, cambios: dict):
        try:
            self.repo.actualizar(id_, cambios)
            UI.print_success("Departamento actualizado")
        except Exception as e:
            UI.print_error(f"Error actualizando departamento: {e}")

    def eliminar(self, id_):
        try:
            self.repo.eliminar(id_)
            UI.print_success("Departamento eliminado")
        except Exception as e:
            UI.print_error(f"Error eliminando departamento: {e}")


class ProyectoService:
    def __init__(self):
        self.repo = ProyectoRepo()

    def crear(self, proyecto):
        try:
            self.repo.crear(proyecto)
            UI.print_success("Proyecto creado")
        except Exception as e:
            UI.print_error(f"Error creando proyecto: {e}")

    def listar_todos(self):
        return self.repo.listar_todos()

    def obtener_por_id(self, id_):
        return self.repo.obtener_por_id(id_)

    def buscar_por_nombre(self, nombre):
        return self.repo.buscar_por_nombre(nombre)

    def modificar(self, id_, cambios: dict):
        try:
            self.repo.actualizar(id_, cambios)
            UI.print_success("Proyecto actualizado")
        except Exception as e:
            UI.print_error(f"Error actualizando proyecto: {e}")

    def eliminar(self, id_):
        try:
            self.repo.eliminar(id_)
            UI.print_success("Proyecto eliminado")
        except Exception as e:
            UI.print_error(f"Error eliminando proyecto: {e}")

    def obtener_calidad_aire_por_ciudad(self, ciudad: str, pais: str = "CL"):
        """
        Obtiene datos de calidad del aire para una ciudad y los devuelve.
        Usa `aplicacion.api_client.EcoAPIClient`.
        """
        try:
            client = EcoAPIClient()
            return client.obtener_calidad_aire_ciudad(ciudad, pais)
        except ValueError as e:
            # API_KEY no configurada
            UI.print_error(f"Configuración faltante para API: {e}")
            return None
        except Exception as e:
            UI.print_error(f"Error obteniendo calidad del aire: {e}")
            return None


class EmpleadoService:
    def __init__(self):
        self.repo = EmpleadoRepo()

    def crear(self, empleado):
        try:
            self.repo.crear(empleado)
            UI.print_success("Empleado creado")
        except Exception as e:
            UI.print_error(f"Error creando empleado: {e}")

    def listar_todos(self):
        return self.repo.listar_todos()

    def obtener_por_id(self, id_):
        return self.repo.obtener_por_id(id_)

    def buscar_por_nombre(self, nombre):
        return self.repo.buscar_por_nombre(nombre)

    def modificar(self, id_, cambios: dict):
        try:
            self.repo.actualizar(id_, cambios)
            UI.print_success("Empleado actualizado")
        except Exception as e:
            UI.print_error(f"Error actualizando empleado: {e}")

    def eliminar(self, id_):
        try:
            self.repo.eliminar(id_)
            UI.print_success("Empleado eliminado")
        except Exception as e:
            UI.print_error(f"Error eliminando empleado: {e}")
