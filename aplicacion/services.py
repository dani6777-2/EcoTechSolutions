from persistencia.repositorios import DepartamentoRepo, ProyectoRepo, EmpleadoRepo, LogClimaRepo
from aplicacion.api_client import EcoAPIClient
from presentacion.ui_helpers import UI
from dominio.models import LogClima
import uuid


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
        self.log_clima_repo = LogClimaRepo()

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

    def obtener_calidad_aire_por_ciudad(self, ciudad: str, pais: str = "CL", 
                                        usuario_id: str = None, proyecto_id: str = None,
                                        guardar_log: bool = True):
        """
        Obtiene datos de calidad del aire para una ciudad y opcionalmente guarda el log.
        Usa `aplicacion.api_client.EcoAPIClient`.
        
        Args:
            ciudad: Nombre de la ciudad
            pais: Código de país ISO 3166
            usuario_id: ID del usuario que realiza la consulta (opcional)
            proyecto_id: ID del proyecto relacionado (opcional)
            guardar_log: Si es True, guarda el registro en la base de datos
        
        Returns:
            Diccionario con datos de calidad del aire o None si hay error
        """
        try:
            client = EcoAPIClient()
            
            # Obtener coordenadas primero
            coords = client.obtener_coordenadas_ciudad(ciudad, pais)
            if not coords:
                return None
            
            # Obtener datos de calidad del aire
            datos = client.obtener_calidad_aire(coords['lat'], coords['lon'])
            
            if datos and guardar_log:
                # Guardar log en la base de datos
                try:
                    log = LogClima(
                        id=str(uuid.uuid4()),
                        ciudad=ciudad,
                        pais=pais,
                        aqi=datos.get('aqi'),
                        co=datos.get('co'),
                        no2=datos.get('no2'),
                        o3=datos.get('o3'),
                        so2=datos.get('so2'),
                        pm2_5=datos.get('pm2_5'),
                        pm10=datos.get('pm10'),
                        nh3=datos.get('nh3'),
                        latitud=coords['lat'],
                        longitud=coords['lon'],
                        usuario_id=usuario_id,
                        proyecto_id=proyecto_id
                    )
                    self.log_clima_repo.crear(log)
                except Exception as e:
                    # Si falla guardar el log, no afecta la consulta
                    UI.print_warning(f"Advertencia: No se pudo guardar el log ({e})")
            
            return datos
            
        except ValueError as e:
            # API_KEY no configurada
            UI.print_error(f"Configuración faltante para API: {e}")
            return None
        except Exception as e:
            UI.print_error(f"Error obteniendo calidad del aire: {e}")
            return None
    
    def listar_logs_clima(self, limit=50):
        """Obtiene todos los logs de clima guardados"""
        try:
            return self.log_clima_repo.listar_todos(limit)
        except Exception as e:
            UI.print_error(f"Error obteniendo logs: {e}")
            return []
    
    def listar_logs_por_ciudad(self, ciudad: str, limit=50):
        """Obtiene logs filtrados por ciudad"""
        try:
            return self.log_clima_repo.listar_por_ciudad(ciudad, limit)
        except Exception as e:
            UI.print_error(f"Error obteniendo logs: {e}")
            return []
    
    def obtener_estadisticas_ciudad(self, ciudad: str):
        """Obtiene estadísticas agregadas de una ciudad"""
        try:
            return self.log_clima_repo.obtener_estadisticas_por_ciudad(ciudad)
        except Exception as e:
            UI.print_error(f"Error obteniendo estadísticas: {e}")
            return None
    
    def listar_ciudades_consultadas(self):
        """Obtiene lista de ciudades únicas consultadas"""
        try:
            return self.log_clima_repo.listar_ciudades_consultadas()
        except Exception as e:
            UI.print_error(f"Error obteniendo ciudades: {e}")
            return []


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
