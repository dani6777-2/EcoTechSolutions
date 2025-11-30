"""Servicios de autenticación y gestión de usuarios"""
from persistencia.auth_repositorios import UsuarioRepo, RolRepo
from dominio.auth_models import Usuario, Rol
from dominio.security import PasswordHasher


class AuthService:
    """Servicio de autenticación"""
    
    def __init__(self):
        self.usuario_repo = UsuarioRepo()
    
    def autenticar(self, nombre_usuario: str, contrasena: str):
        """
        Autentica un usuario con nombre de usuario y contraseña.
        
        Args:
            nombre_usuario: Nombre de usuario
            contrasena: Contraseña en texto plano
            
        Returns:
            dict con datos del usuario si es exitoso, None si falla
        """
        try:
            usuario_data = self.usuario_repo.obtener_por_nombre_usuario(nombre_usuario)
            
            if not usuario_data:
                print("❌ Usuario no encontrado")
                return None
            
            if not usuario_data['activo']:
                print("❌ Usuario inactivo")
                return None
            
            # Verificar contraseña
            if PasswordHasher.verify_password(
                contrasena, 
                usuario_data['salt'], 
                usuario_data['contrasena_cifrada']
            ):
                # Actualizar último login
                self.usuario_repo.actualizar_ultimo_login(usuario_data['id'])
                print(f"✓ Bienvenido {nombre_usuario}!")
                return usuario_data
            else:
                print("❌ Contraseña incorrecta")
                return None
        except Exception as e:
            print(f"Error en autenticación: {e}")
            return None


class UsuarioService:
    """Servicio de gestión de usuarios"""
    
    def __init__(self):
        self.usuario_repo = UsuarioRepo()
        self.rol_repo = RolRepo()
    
    def crear_usuario(self, usuario: Usuario, contrasena_plana: str):
        """
        Crea un nuevo usuario con contraseña hasheada.
        
        Args:
            usuario: Instancia de Usuario (sin salt ni hash aún)
            contrasena_plana: Contraseña en texto plano
        """
        try:
            # Generar salt y hashear contraseña
            salt = PasswordHasher.generate_salt()
            contrasena_hash = PasswordHasher.hash_password(contrasena_plana, salt)
            
            # Actualizar usuario con salt y hash
            usuario.salt = salt
            usuario.contrasena_cifrada = contrasena_hash
            
            self.usuario_repo.crear(usuario)
            print(f"✓ Usuario '{usuario.nombre_usuario}' creado exitosamente")
        except Exception as e:
            print(f"Error creando usuario: {e}")
    
    def listar_usuarios(self):
        """Lista todos los usuarios (sin contraseñas)"""
        return self.usuario_repo.listar_todos()
    
    def cambiar_contrasena(self, usuario_id: str, contrasena_actual: str, contrasena_nueva: str):
        """
        Cambia la contraseña de un usuario.
        
        Args:
            usuario_id: ID del usuario
            contrasena_actual: Contraseña actual en texto plano
            contrasena_nueva: Nueva contraseña en texto plano
        """
        try:
            usuario_data = self.usuario_repo.obtener_por_id(usuario_id)
            
            if not usuario_data:
                print("❌ Usuario no encontrado")
                return False
            
            # Verificar contraseña actual
            if not PasswordHasher.verify_password(
                contrasena_actual, 
                usuario_data['salt'], 
                usuario_data['contrasena_cifrada']
            ):
                print("❌ Contraseña actual incorrecta")
                return False
            
            # Generar nuevo salt y hash
            nuevo_salt = PasswordHasher.generate_salt()
            nuevo_hash = PasswordHasher.hash_password(contrasena_nueva, nuevo_salt)
            
            self.usuario_repo.cambiar_contrasena(usuario_id, nuevo_hash, nuevo_salt)
            print("✓ Contraseña cambiada exitosamente")
            return True
        except Exception as e:
            print(f"Error cambiando contraseña: {e}")
            return False
    
    def activar_desactivar_usuario(self, usuario_id: str, activo: bool):
        """Activa o desactiva un usuario"""
        try:
            self.usuario_repo.actualizar_estado(usuario_id, activo)
            estado = "activado" if activo else "desactivado"
            print(f"✓ Usuario {estado}")
        except Exception as e:
            print(f"Error actualizando estado: {e}")


class RolService:
    """Servicio de gestión de roles"""
    
    def __init__(self):
        self.rol_repo = RolRepo()
    
    def crear_rol(self, rol: Rol):
        """Crea un nuevo rol"""
        try:
            self.rol_repo.crear(rol)
            print(f"✓ Rol '{rol.nombre}' creado")
        except Exception as e:
            print(f"Error creando rol: {e}")
    
    def listar_roles(self):
        """Lista todos los roles activos"""
        return self.rol_repo.listar_todos()
    
    def obtener_rol(self, rol_id: str):
        """Obtiene un rol por su ID"""
        return self.rol_repo.obtener_por_id(rol_id)
