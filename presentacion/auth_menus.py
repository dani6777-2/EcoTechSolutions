"""Menús de autenticación y gestión de usuarios"""
from .menu_base import MenuBase
from dominio.auth_models import Usuario, Rol
import uuid
import getpass


class LoginMenu:
    """Menú de inicio de sesión"""
    
    def __init__(self, auth_service):
        self.auth_service = auth_service
    
    def mostrar(self):
        print("\n" + "="*50)
        print("   ECOTECH SOLUTIONS - SISTEMA DE GESTIÓN")
        print("="*50)
        print("\n Por favor, inicie sesión para continuar\n")
    
    def ejecutar(self):
        """Ejecuta el proceso de login y retorna el usuario autenticado"""
        intentos = 0
        max_intentos = 3
        
        while intentos < max_intentos:
            self.mostrar()
            
            nombre_usuario = input("Usuario: ").strip()
            if not nombre_usuario:
                print("❌ El nombre de usuario no puede estar vacío")
                continue
            
            # Usar getpass para ocultar contraseña
            contrasena = getpass.getpass("Contraseña: ")
            
            usuario_data = self.auth_service.autenticar(nombre_usuario, contrasena)
            
            if usuario_data:
                return usuario_data
            
            intentos += 1
            restantes = max_intentos - intentos
            if restantes > 0:
                print(f"\n⚠️  Intentos restantes: {restantes}\n")
        
        print("\n❌ Demasiados intentos fallidos. Cerrando aplicación...")
        return None


class UsuariosMenu(MenuBase):
    """Menú de gestión de usuarios"""
    
    def __init__(self, usuario_service, rol_service):
        self.usuario_service = usuario_service
        self.rol_service = rol_service
    
    def mostrar(self):
        print("\n-- Menú Gestión de Usuarios --")
        print("1. Crear nuevo usuario")
        print("2. Listar usuarios")
        print("3. Cambiar mi contraseña")
        print("4. Activar/Desactivar usuario")
        print("5. Volver")
    
    def ejecutar(self):
        while True:
            self.mostrar()
            opcion = self.limpiar_input("Opción: ")
            
            if opcion == '1':
                self._crear_usuario()
            elif opcion == '2':
                self._listar_usuarios()
            elif opcion == '3':
                self._cambiar_contrasena()
            elif opcion == '4':
                self._activar_desactivar()
            elif opcion == '5':
                break
            else:
                print("❌ Opción inválida")
    
    def _crear_usuario(self):
        """Crea un nuevo usuario"""
        print("\n--- Crear Nuevo Usuario ---")
        
        nombre_usuario = self.limpiar_input("Nombre de usuario (min 3 caracteres): ")
        if len(nombre_usuario) < 3:
            print("❌ Nombre de usuario muy corto")
            return
        
        # Mostrar roles disponibles
        roles = self.rol_service.listar_roles()
        if not roles:
            print("❌ No hay roles disponibles. Crear roles primero.")
            return
        
        print("\nRoles disponibles:")
        for i, rol in enumerate(roles, 1):
            print(f"  {i}. {rol['nombre']} - {rol['descripcion'] or 'Sin descripción'}")
        
        try:
            opcion_rol = int(self.limpiar_input("\nSeleccione rol (número): "))
            if opcion_rol < 1 or opcion_rol > len(roles):
                print("❌ Opción inválida")
                return
            rol_seleccionado = roles[opcion_rol - 1]
        except ValueError:
            print("❌ Debe ingresar un número")
            return
        
        # Solicitar contraseña (oculta)
        contrasena = getpass.getpass("Contraseña (min 6 caracteres): ")
        if len(contrasena) < 6:
            print("❌ Contraseña muy corta (mínimo 6 caracteres)")
            return
        
        contrasena_confirm = getpass.getpass("Confirmar contraseña: ")
        if contrasena != contrasena_confirm:
            print("❌ Las contraseñas no coinciden")
            return
        
        # Crear usuario
        usuario = Usuario(
            id=str(uuid.uuid4()),
            nombre_usuario=nombre_usuario,
            contrasena_cifrada="",  # Se generará en el servicio
            salt="",  # Se generará en el servicio
            rol_id=rol_seleccionado['id'],
            activo=True
        )
        
        self.usuario_service.crear_usuario(usuario, contrasena)
    
    def _listar_usuarios(self):
        """Lista todos los usuarios"""
        print("\n--- Usuarios del Sistema ---")
        usuarios = self.usuario_service.listar_usuarios()
        
        if not usuarios:
            print("No hay usuarios registrados")
            return
        
        for u in usuarios:
            estado = "✓ Activo" if u['activo'] else "✗ Inactivo"
            print(f"\n• {u['nombre_usuario']}")
            print(f"  Rol: {u['rol_id']}")
            print(f"  Estado: {estado}")
            print(f"  Creado: {u['fecha_creacion']}")
    
    def _cambiar_contrasena(self):
        """Cambia la contraseña del usuario actual"""
        print("\n--- Cambiar Contraseña ---")
        
        usuario_id = self.limpiar_input("ID de usuario: ")
        contrasena_actual = getpass.getpass("Contraseña actual: ")
        contrasena_nueva = getpass.getpass("Nueva contraseña (min 6 caracteres): ")
        
        if len(contrasena_nueva) < 6:
            print("❌ Contraseña muy corta")
            return
        
        contrasena_confirm = getpass.getpass("Confirmar nueva contraseña: ")
        if contrasena_nueva != contrasena_confirm:
            print("❌ Las contraseñas no coinciden")
            return
        
        self.usuario_service.cambiar_contrasena(usuario_id, contrasena_actual, contrasena_nueva)
    
    def _activar_desactivar(self):
        """Activa o desactiva un usuario"""
        print("\n--- Activar/Desactivar Usuario ---")
        
        usuario_id = self.limpiar_input("ID de usuario: ")
        accion = self.limpiar_input("¿Activar? (s/n): ").lower()
        
        activo = accion == 's'
        self.usuario_service.activar_desactivar_usuario(usuario_id, activo)


class RolesMenu(MenuBase):
    """Menú de gestión de roles"""
    
    def __init__(self, rol_service):
        self.rol_service = rol_service
    
    def mostrar(self):
        print("\n-- Menú Gestión de Roles --")
        print("1. Crear nuevo rol")
        print("2. Listar roles")
        print("3. Volver")
    
    def ejecutar(self):
        while True:
            self.mostrar()
            opcion = self.limpiar_input("Opción: ")
            
            if opcion == '1':
                self._crear_rol()
            elif opcion == '2':
                self._listar_roles()
            elif opcion == '3':
                break
            else:
                print("❌ Opción inválida")
    
    def _crear_rol(self):
        """Crea un nuevo rol"""
        print("\n--- Crear Nuevo Rol ---")
        
        nombre = self.limpiar_input("Nombre del rol: ")
        descripcion = self.limpiar_input("Descripción: ")
        
        try:
            nivel_permisos = int(self.limpiar_input("Nivel de permisos (1-10): "))
            if nivel_permisos < 1 or nivel_permisos > 10:
                print("❌ Nivel de permisos debe estar entre 1 y 10")
                return
        except ValueError:
            print("❌ Debe ingresar un número")
            return
        
        rol = Rol(
            id=str(uuid.uuid4()),
            nombre=nombre,
            descripcion=descripcion,
            nivel_permisos=nivel_permisos,
            activo=True
        )
        
        self.rol_service.crear_rol(rol)
    
    def _listar_roles(self):
        """Lista todos los roles"""
        print("\n--- Roles del Sistema ---")
        roles = self.rol_service.listar_roles()
        
        if not roles:
            print("No hay roles registrados")
            return
        
        for rol in roles:
            print(f"\n• {rol['nombre']}")
            print(f"  Descripción: {rol['descripcion'] or 'N/A'}")
            print(f"  Nivel de permisos: {rol['nivel_permisos']}")
