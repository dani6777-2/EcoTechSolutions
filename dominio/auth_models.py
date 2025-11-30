"""Modelos de dominio para autenticación"""


class Usuario:
    def __init__(self, id: str, nombre_usuario: str, contrasena_cifrada: str, 
                 salt: str, rol_id: str, activo: bool = True):
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.contrasena_cifrada = contrasena_cifrada
        self.salt = salt
        self.rol_id = rol_id
        self.activo = activo
    
    @property
    def nombre_usuario(self):
        return self._nombre_usuario
    
    @nombre_usuario.setter
    def nombre_usuario(self, value):
        if not value or len(value) < 3:
            raise ValueError("El nombre de usuario debe tener al menos 3 caracteres")
        self._nombre_usuario = value
    
    def __repr__(self):
        return f"Usuario(id={self.id}, nombre_usuario={self.nombre_usuario}, rol={self.rol_id})"


class Rol:
    def __init__(self, id: str, nombre: str, descripcion: str = None, 
                 nivel_permisos: int = 1, activo: bool = True):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.nivel_permisos = nivel_permisos
        self.activo = activo
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, value):
        if not value or len(value) < 2:
            raise ValueError("El nombre del rol debe tener al menos 2 caracteres")
        self._nombre = value
    
    def __repr__(self):
        return f"Rol(id={self.id}, nombre={self.nombre}, nivel_permisos={self.nivel_permisos})"
