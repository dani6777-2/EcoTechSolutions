"""Menús de autenticación y gestión de usuarios"""
from .menu_base import MenuBase
from .ui_helpers import UI, Colors, Icons
from dominio.auth_models import Usuario, Rol
import uuid
import getpass


class LoginMenu:
    """Menú de inicio de sesión"""
    
    def __init__(self, auth_service):
        self.auth_service = auth_service
    
    def mostrar(self):
        UI.clear_screen()
        UI.print_header("ECOTECH SOLUTIONS", "Gestión Empresarial Sustentable", "🌱")
        print(f"\n{Colors.BRIGHT_CYAN}  Por favor, inicie sesión para continuar{Colors.RESET}\n")
    
    def ejecutar(self):
        """Ejecuta el proceso de login y retorna el usuario autenticado"""
        intentos = 0
        max_intentos = 3
        
        while intentos < max_intentos:
            self.mostrar()
            
            nombre_usuario = UI.input_prompt("Usuario", icon="👤")
            if not nombre_usuario:
                UI.print_error("El nombre de usuario no puede estar vacío")
                UI.pause()
                continue
            
            # Usar getpass para ocultar contraseña
            contrasena = getpass.getpass(f"\n{Colors.BRIGHT_YELLOW}🔒 Contraseña:{Colors.RESET} ")
            
            usuario_data = self.auth_service.autenticar(nombre_usuario, contrasena)
            
            if usuario_data:
                UI.print_welcome(usuario_data['nombre_usuario'], usuario_data.get('nombre_rol', 'Usuario'))
                UI.pause()
                return usuario_data
            
            intentos += 1
            restantes = max_intentos - intentos
            if restantes > 0:
                UI.print_error(f"Credenciales incorrectas. Intentos restantes: {restantes}")
                UI.pause()
        
        UI.print_error("Demasiados intentos fallidos. Cerrando aplicación...")
        return None


class UsuariosMenu(MenuBase):
    """Menú de gestión de usuarios"""
    
    def __init__(self, usuario_service, rol_service, usuario_actual=None):
        self.usuario_service = usuario_service
        self.rol_service = rol_service
        self.usuario_actual = usuario_actual
    
    def mostrar(self):
        UI.print_section("Gestión de Usuarios", Icons.USER)
        UI.print_menu_option("1", "Crear nuevo usuario", Icons.ADD)
        UI.print_menu_option("2", "Listar usuarios", Icons.VIEW)
        UI.print_menu_option("3", "Cambiar contraseña de usuario", Icons.LOCK)
        UI.print_menu_option("4", "Activar/Desactivar usuario", Icons.SETTINGS)
        UI.print_menu_option("5", "Volver", Icons.BACK)
    
    def ejecutar(self):
        while True:
            self.mostrar()
            opcion = UI.input_prompt("Seleccione una opción")
            
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
                UI.print_error("Opción inválida")
            
            if opcion != '5':
                UI.pause()
    
    def _crear_usuario(self):
        """Crea un nuevo usuario"""
        UI.print_section("Crear Nuevo Usuario", Icons.ADD)
        
        nombre_usuario = UI.input_prompt("Nombre de usuario (min 3 caracteres)")
        if len(nombre_usuario) < 3:
            UI.print_error("Nombre de usuario muy corto")
            return
        
        # Mostrar roles disponibles
        roles = self.rol_service.listar_roles()
        if not roles:
            UI.print_error("No hay roles disponibles. Crear roles primero")
            return
        
        print(f"\n{Colors.YELLOW}{Icons.INFO} Roles disponibles:{Colors.RESET}")
        for i, rol in enumerate(roles, 1):
            desc = rol['descripcion'] or 'Sin descripción'
            print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} {i}. {rol['nombre']} - {desc}")
        
        try:
            opcion_rol = int(UI.input_prompt("Seleccione rol (número)"))
            if opcion_rol < 1 or opcion_rol > len(roles):
                UI.print_error("Opción inválida")
                return
            rol_seleccionado = roles[opcion_rol - 1]
        except ValueError:
            UI.print_error("Debe ingresar un número")
            return
        
        # Solicitar contraseña (oculta)
        contrasena = getpass.getpass(f"{Colors.CYAN}{Icons.LOCK} Contraseña (min 6 caracteres): {Colors.RESET}")
        if len(contrasena) < 6:
            UI.print_error("Contraseña muy corta (mínimo 6 caracteres)")
            return
        
        contrasena_confirm = getpass.getpass(f"{Colors.CYAN}{Icons.LOCK} Confirmar contraseña: {Colors.RESET}")
        if contrasena != contrasena_confirm:
            UI.print_error("Las contraseñas no coinciden")
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
        UI.print_section("Usuarios del Sistema", Icons.VIEW)
        usuarios = self.usuario_service.listar_usuarios()
        
        if not usuarios:
            UI.print_warning("No hay usuarios registrados")
            return
        
        # Obtener todos los roles para mostrar nombres
        roles = self.rol_service.listar_roles()
        roles_dict = {r['id']: r['nombre'] for r in roles}
        
        headers = ["#", "Usuario", "Rol", "Estado", "Fecha Creación"]
        rows = []
        
        for idx, u in enumerate(usuarios, 1):
            estado_icon = f"{Colors.GREEN}●{Colors.RESET}" if u['activo'] else f"{Colors.RED}●{Colors.RESET}"
            estado_texto = f"{estado_icon} {'Activo' if u['activo'] else 'Inactivo'}"
            rol_nombre = roles_dict.get(u['rol_id'], 'Desconocido')
            
            rows.append([
                str(idx),
                u['nombre_usuario'],
                rol_nombre,
                estado_texto,
                str(u['fecha_creacion'])[:10]
            ])
        
        UI.print_table(headers, rows)
    
    def _cambiar_contrasena(self):
        """Cambia la contraseña de un usuario seleccionado"""
        UI.print_section("Cambiar Contraseña de Usuario", Icons.LOCK)
        
        # Listar usuarios disponibles
        usuarios = self.usuario_service.listar_usuarios()
        if not usuarios:
            UI.print_error("No hay usuarios registrados")
            return
        
        print(f"\n{Colors.YELLOW}{Icons.INFO} Usuarios disponibles:{Colors.RESET}")
        for i, u in enumerate(usuarios, 1):
            estado = f"{Colors.GREEN}✓{Colors.RESET}" if u['activo'] else f"{Colors.RED}✗{Colors.RESET}"
            print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} {i}. {u['nombre_usuario']} {estado}")
        
        try:
            opcion = int(UI.input_prompt("Seleccione usuario (número)"))
            if opcion < 1 or opcion > len(usuarios):
                UI.print_error("Opción inválida")
                return
            usuario_seleccionado = usuarios[opcion - 1]
        except ValueError:
            UI.print_error("Debe ingresar un número")
            return
        
        # Solicitar nueva contraseña
        print(f"\n{Colors.CYAN}{Icons.INFO} Cambiando contraseña para: {Colors.BOLD}{usuario_seleccionado['nombre_usuario']}{Colors.RESET}")
        contrasena_nueva = getpass.getpass(f"{Colors.CYAN}{Icons.LOCK} Nueva contraseña (min 6 caracteres): {Colors.RESET}")
        
        if len(contrasena_nueva) < 6:
            UI.print_error("Contraseña muy corta")
            return
        
        contrasena_confirm = getpass.getpass(f"{Colors.CYAN}{Icons.LOCK} Confirmar nueva contraseña: {Colors.RESET}")
        if contrasena_nueva != contrasena_confirm:
            UI.print_error("Las contraseñas no coinciden")
            return
        
        # Cambiar contraseña (sin verificar la actual - admin puede resetear)
        self.usuario_service.cambiar_contrasena(usuario_seleccionado['id'], contrasena_nueva)
    
    def _activar_desactivar(self):
        """Activa o desactiva un usuario"""
        UI.print_section("Activar/Desactivar Usuario", Icons.SETTINGS)
        
        # Listar usuarios disponibles
        usuarios = self.usuario_service.listar_usuarios()
        if not usuarios:
            UI.print_error("No hay usuarios registrados")
            return
        
        print(f"\n{Colors.YELLOW}{Icons.INFO} Usuarios disponibles:{Colors.RESET}")
        for i, u in enumerate(usuarios, 1):
            estado = f"{Colors.GREEN}✓ Activo{Colors.RESET}" if u['activo'] else f"{Colors.RED}✗ Inactivo{Colors.RESET}"
            print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} {i}. {u['nombre_usuario']} - {estado}")
        
        try:
            opcion = int(UI.input_prompt("Seleccione usuario (número)"))
            if opcion < 1 or opcion > len(usuarios):
                UI.print_error("Opción inválida")
                return
            usuario_seleccionado = usuarios[opcion - 1]
        except ValueError:
            UI.print_error("Debe ingresar un número")
            return
        
        # Prevenir que un usuario se desactive a sí mismo
        if self.usuario_actual and usuario_seleccionado['nombre_usuario'] == self.usuario_actual.get('nombre_usuario'):
            UI.print_error("No puedes desactivar tu propia cuenta")
            UI.print_warning("Usa otra cuenta de administrador para realizar esta acción")
            return
        
        print(f"\n{Colors.CYAN}{Icons.INFO} Usuario seleccionado: {Colors.BOLD}{usuario_seleccionado['nombre_usuario']}{Colors.RESET}")
        estado_actual = f"{Colors.GREEN}Activo{Colors.RESET}" if usuario_seleccionado['activo'] else f"{Colors.RED}Inactivo{Colors.RESET}"
        print(f"{Colors.CYAN}{Icons.INFO} Estado actual: {estado_actual}")
        
        # Determinar la acción según el estado actual
        if usuario_seleccionado['activo']:
            # Usuario está activo, preguntar si desactivar
            if UI.confirm("¿Desactivar usuario?"):
                nuevo_estado = False
            else:
                UI.print_info("Operación cancelada")
                return
        else:
            # Usuario está inactivo, preguntar si activar
            if UI.confirm("¿Activar usuario?"):
                nuevo_estado = True
            else:
                UI.print_info("Operación cancelada")
                return
        
        # Validación especial para el usuario admin
        if not nuevo_estado and usuario_seleccionado['nombre_usuario'] == 'admin':
            UI.print_warning("ADVERTENCIA: No se recomienda desactivar el usuario administrador")
            if not UI.confirm("¿Está seguro?"):
                UI.print_error("Operación cancelada")
                return
        
        self.usuario_service.activar_desactivar_usuario(usuario_seleccionado['id'], nuevo_estado)


class RolesMenu(MenuBase):
    """Menú de gestión de roles"""
    
    def __init__(self, rol_service):
        self.rol_service = rol_service
    
    def mostrar(self):
        UI.print_section("Gestión de Roles", Icons.SHIELD)
        UI.print_menu_option("1", "Crear nuevo rol", Icons.ADD)
        UI.print_menu_option("2", "Listar roles", Icons.VIEW)
        UI.print_menu_option("3", "Volver", Icons.BACK)
    
    def ejecutar(self):
        while True:
            self.mostrar()
            opcion = UI.input_prompt("Seleccione una opción")
            
            if opcion == '1':
                self._crear_rol()
            elif opcion == '2':
                self._listar_roles()
            elif opcion == '3':
                break
            else:
                UI.print_error("Opción inválida")
            
            if opcion != '3':
                UI.pause()
    
    def _crear_rol(self):
        """Crea un nuevo rol"""
        UI.print_section("Crear Nuevo Rol", Icons.ADD)
        
        nombre = UI.input_prompt("Nombre del rol")
        descripcion = UI.input_prompt("Descripción")
        
        try:
            nivel_permisos = int(UI.input_prompt("Nivel de permisos (1-10)"))
            if nivel_permisos < 1 or nivel_permisos > 10:
                UI.print_error("Nivel de permisos debe estar entre 1 y 10")
                return
        except ValueError:
            UI.print_error("Debe ingresar un número")
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
        UI.print_section("Roles del Sistema", Icons.VIEW)
        roles = self.rol_service.listar_roles()
        
        if not roles:
            UI.print_warning("No hay roles registrados")
            return
        
        headers = ["#", "Nombre", "Descripción", "Nivel Permisos"]
        rows = []
        
        for idx, rol in enumerate(roles, 1):
            desc = rol['descripcion'] or 'N/A'
            rows.append([
                str(idx),
                rol['nombre'],
                desc,
                str(rol['nivel_permisos'])
            ])
        
        UI.print_table(headers, rows)
