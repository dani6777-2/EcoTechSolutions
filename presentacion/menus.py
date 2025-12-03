from .menu_base import MenuBase
from .ui_helpers import UI, Colors, Icons
from dominio.models import Departamento, Proyecto, Empleado
import uuid


class DepartamentosMenu(MenuBase):
    def mostrar(self):
        UI.print_section("Gestión de Departamentos", Icons.DEPARTMENT)
        UI.print_menu_option("1", "Agregar departamento", Icons.ADD)
        UI.print_menu_option("2", "Mostrar todos", Icons.VIEW)
        UI.print_menu_option("3", "Buscar por código", Icons.SEARCH)
        UI.print_menu_option("4", "Buscar por nombre", Icons.SEARCH)
        UI.print_menu_option("5", "Modificar", Icons.EDIT)
        UI.print_menu_option("6", "Eliminar", Icons.DELETE)
        UI.print_menu_option("7", "Volver", Icons.BACK)

    def ejecutar(self):
        while True:
            self.mostrar()
            opcion = UI.input_prompt("Seleccione una opción")
            
            if opcion == '1':
                nombre = UI.input_prompt("Nombre del departamento", Icons.DEPARTMENT)
                descripcion = UI.input_prompt("Descripción", Icons.EDIT)
                dept = Departamento(id=str(uuid.uuid4()), nombre=nombre, descripcion=descripcion)
                self.servicio.crear(dept)
            elif opcion == '2':
                departamentos = self.servicio.listar_todos()
                if not departamentos:
                    UI.print_warning("No hay departamentos registrados")
                else:
                    UI.print_section("Lista de Departamentos", Icons.DEPARTMENT)
                    for d in departamentos:
                        UI.print_item("Nombre", d.get('nombre', 'N/A'))
                        UI.print_item("Descripción", d.get('descripcion', 'Sin descripción'))
                        UI.print_item("ID", d.get('id', 'N/A'), Colors.DIM)
                        print()
            elif opcion == '3':
                codigo = UI.input_prompt("Código del departamento", Icons.SEARCH)
                dept = self.servicio.obtener_por_id(codigo)
                if dept:
                    UI.print_section("Departamento Encontrado", Icons.SUCCESS)
                    UI.print_item("Nombre", dept.get('nombre', 'N/A'))
                    UI.print_item("Descripción", dept.get('descripcion', 'N/A'))
                    UI.print_item("ID", dept.get('id', 'N/A'), Colors.DIM)
                else:
                    UI.print_error("Departamento no encontrado")
            elif opcion == '4':
                nombre = UI.input_prompt("Nombre a buscar", Icons.SEARCH)
                departamentos = self.servicio.buscar_por_nombre(nombre)
                if not departamentos:
                    UI.print_warning("No se encontraron departamentos")
                else:
                    UI.print_section(f"Resultados para: {nombre}", Icons.SEARCH)
                    for d in departamentos:
                        UI.print_item("Nombre", d.get('nombre', 'N/A'))
                        UI.print_item("Descripción", d.get('descripcion', 'N/A'))
                        print()
            elif opcion == '5':
                codigo = UI.input_prompt("Código del departamento a modificar", Icons.EDIT)
                nombre = UI.input_prompt("Nuevo nombre", Icons.DEPARTMENT)
                descripcion = UI.input_prompt("Nueva descripción", Icons.EDIT)
                self.servicio.modificar(codigo, {'nombre': nombre, 'descripcion': descripcion})
            elif opcion == '6':
                codigo = UI.input_prompt("Código del departamento a eliminar", Icons.DELETE)
                if UI.confirm(f"¿Está seguro de eliminar el departamento?"):
                    self.servicio.eliminar(codigo)
                else:
                    UI.print_warning("Operación cancelada")
            elif opcion == '7':
                break
            else:
                UI.print_error("Opción inválida")
            
            if opcion != '7':
                UI.pause()


class ProyectosMenu(MenuBase):
    def mostrar(self):
        UI.print_section("Gestión de Proyectos", f"{Icons.PROJECT} {Icons.EARTH}")
        UI.print_menu_option("1", "Agregar proyecto", Icons.ADD)
        UI.print_menu_option("2", "Mostrar todos", Icons.VIEW)
        UI.print_menu_option("3", "Buscar por código", Icons.SEARCH)
        UI.print_menu_option("4", "Buscar por nombre", Icons.SEARCH)
        UI.print_menu_option("5", "Modificar", Icons.EDIT)
        UI.print_menu_option("6", "Eliminar", Icons.DELETE)
        UI.print_menu_option("7", "Evaluar calidad del aire", f"{Icons.EARTH} {Icons.AIR}")
        UI.print_menu_option("8", "Volver", Icons.BACK)

    def ejecutar(self):
        while True:
            self.mostrar()
            opcion = UI.input_prompt("Seleccione una opción")
            
            if opcion == '1':
                self._agregar_proyecto()
            elif opcion == '2':
                proyectos = self.servicio.listar_todos()
                if not proyectos:
                    UI.print_warning("No hay proyectos registrados")
                else:
                    UI.print_section("Lista de Proyectos", Icons.PROJECT)
                    for p in proyectos:
                        UI.print_item("Nombre", p.get('nombre', 'N/A'), Colors.BRIGHT_CYAN)
                        UI.print_item("Descripción", p.get('descripcion', 'Sin descripción'))
                        UI.print_item("Fecha inicio", p.get('fecha_inicio', 'N/A'), Colors.BRIGHT_GREEN)
                        UI.print_item("Fecha fin", p.get('fecha_fin', 'En curso'), Colors.BRIGHT_YELLOW)
                        UI.print_item("ID", p.get('id', 'N/A'), Colors.DIM)
                        print()
            elif opcion == '3':
                codigo = UI.input_prompt("Código del proyecto", Icons.SEARCH)
                proyecto = self.servicio.obtener_por_id(codigo)
                if proyecto:
                    UI.print_section("Proyecto Encontrado", Icons.SUCCESS)
                    UI.print_item("Nombre", proyecto.get('nombre', 'N/A'))
                    UI.print_item("Descripción", proyecto.get('descripcion', 'N/A'))
                    UI.print_item("Fecha inicio", proyecto.get('fecha_inicio', 'N/A'))
                    UI.print_item("Fecha fin", proyecto.get('fecha_fin', 'En curso'))
                else:
                    UI.print_error("Proyecto no encontrado")
            elif opcion == '4':
                nombre = UI.input_prompt("Nombre a buscar", Icons.SEARCH)
                proyectos = self.servicio.buscar_por_nombre(nombre)
                if not proyectos:
                    UI.print_warning("No se encontraron proyectos")
                else:
                    UI.print_section(f"Resultados para: {nombre}", Icons.SEARCH)
                    for p in proyectos:
                        UI.print_item("Nombre", p.get('nombre', 'N/A'))
                        UI.print_item("Descripción", p.get('descripcion', 'N/A'))
                        print()
            elif opcion == '5':
                codigo = UI.input_prompt("Código del proyecto a modificar", Icons.EDIT)
                nombre = UI.input_prompt("Nuevo nombre", Icons.PROJECT)
                descripcion = UI.input_prompt("Nueva descripción", Icons.EDIT)
                self.servicio.modificar(codigo, {'nombre': nombre, 'descripcion': descripcion})
            elif opcion == '6':
                codigo = UI.input_prompt("Código del proyecto a eliminar", Icons.DELETE)
                if UI.confirm("¿Está seguro de eliminar el proyecto?"):
                    self.servicio.eliminar(codigo)
                else:
                    UI.print_warning("Operación cancelada")
            elif opcion == '7':
                self._evaluar_calidad_aire()
            elif opcion == '8':
                break
            else:
                UI.print_error("Opción inválida")
            
            if opcion != '8':
                UI.pause()
    
    def _agregar_proyecto(self):
        """Agregar proyecto con opción de evaluar calidad del aire"""
        UI.print_section("Nuevo Proyecto", Icons.ADD)
        
        nombre = UI.input_prompt("Nombre del proyecto", Icons.PROJECT)
        descripcion = UI.input_prompt("Descripción", Icons.EDIT)
        fecha_inicio = UI.input_prompt("Fecha inicio (YYYY-MM-DD)", Icons.CALENDAR)
        fecha_fin = UI.input_prompt("Fecha fin (YYYY-MM-DD) o Enter para proyecto continuo", Icons.CALENDAR)
        
        # Preguntar si desea evaluar calidad del aire antes de crear
        UI.print_info("EcoTech Solutions - Evaluación Ambiental", Icons.LEAF)
        evaluar = UI.confirm("¿Desea evaluar calidad del aire en la ubicación del proyecto?")
        
        if evaluar:
            ciudad = UI.input_prompt("Ciudad del proyecto", Icons.EARTH)
            pais = UI.input_prompt("Código de país (ej: CL, AR, PE) [CL]", Icons.EARTH).upper() or "CL"
            
            print(f"\n{Colors.BRIGHT_CYAN}🔍 Consultando calidad del aire en {ciudad}, {pais}...{Colors.RESET}")
            datos = self.servicio.obtener_calidad_aire_por_ciudad(ciudad, pais)
            
            if datos:
                self._mostrar_reporte_calidad_aire(datos, ciudad)
                
                # Sugerencia basada en AQI
                aqi = datos.get('aqi', 0)
                if aqi >= 4:
                    UI.print_warning("ADVERTENCIA: Calidad del aire POBRE en esta ubicación")
                    if not UI.confirm("¿Desea continuar con el proyecto en esta ubicación?"):
                        UI.print_error("Creación de proyecto cancelada")
                        UI.pause()
                        return
                elif aqi == 3:
                    UI.print_warning("NOTA: Calidad del aire MODERADA - Considere medidas de mitigación")
                else:
                    UI.print_success("Buena calidad del aire - Ubicación apropiada")
            else:
                UI.print_warning("No se pudo obtener información ambiental, continuando...")
        
        # Crear proyecto
        p = Proyecto(
            id=str(uuid.uuid4()), 
            nombre=nombre, 
            descripcion=descripcion, 
            fecha_inicio=fecha_inicio, 
            fecha_fin=fecha_fin or None
        )
        self.servicio.crear(p)
        UI.pause()
    
    def _evaluar_calidad_aire(self):
        """Evaluar calidad del aire en una ubicación específica"""
        UI.print_header("EVALUACIÓN DE CALIDAD DEL AIRE", "EcoTech Solutions", Icons.EARTH)
        
        print(f"\n{Colors.BRIGHT_CYAN}Evalúe condiciones ambientales antes de iniciar proyectos")
        print(f"o expandir operaciones a nuevas ubicaciones.{Colors.RESET}\n")
        
        ciudad = UI.input_prompt("Ciudad a evaluar", Icons.EARTH)
        if not ciudad:
            UI.print_error("Debe ingresar una ciudad")
            UI.pause()
            return
        
        pais = UI.input_prompt("Código de país (ej: CL, AR, PE) [CL]", Icons.EARTH).upper() or "CL"
        
        print(f"\n{Colors.BRIGHT_CYAN}🔍 Consultando calidad del aire en {ciudad}, {pais}...{Colors.RESET}")
        datos = self.servicio.obtener_calidad_aire_por_ciudad(ciudad, pais)
        
        if datos:
            self._mostrar_reporte_calidad_aire(datos, ciudad)
            self._mostrar_recomendacion_proyecto(datos.get('aqi', 0))
        else:
            UI.print_error("No se pudo obtener información de calidad del aire")
            print(f"\n{Colors.BRIGHT_YELLOW}Posibles causas:{Colors.RESET}")
            print("  • Ciudad no encontrada (verifica ortografía)")
            print("  • API_KEY no configurada (ver README.md)")
            print("  • Sin conexión a internet")
        
        UI.pause()
    
    def _mostrar_reporte_calidad_aire(self, datos, ciudad):
        """Muestra reporte formateado de calidad del aire"""
        from aplicacion.api_client import EcoAPIClient
        
        aqi = datos.get('aqi', 0)
        interpretacion = EcoAPIClient.interpretar_aqi(aqi)
        
        UI.print_section(f"REPORTE DE CALIDAD DEL AIRE - {ciudad.upper()}", Icons.AIR)
        
        # Índice de calidad con color según nivel
        aqi_color = Colors.BRIGHT_GREEN if aqi <= 2 else (Colors.BRIGHT_YELLOW if aqi == 3 else Colors.BRIGHT_RED)
        print(f"\n{aqi_color}📊 Índice de Calidad (AQI): {aqi}/5 - {interpretacion}{Colors.RESET}")
        
        print(f"\n{Colors.BRIGHT_CYAN}🔬 Contaminantes principales (μg/m³):{Colors.RESET}")
        UI.print_item("PM2.5 (Partículas finas)", datos.get('pm2_5', 'N/A'))
        UI.print_item("PM10 (Partículas)", datos.get('pm10', 'N/A'))
        UI.print_item("NO₂ (Dióxido nitrógeno)", datos.get('no2', 'N/A'))
        UI.print_item("O₃ (Ozono)", datos.get('o3', 'N/A'))
        UI.print_item("SO₂ (Dióxido azufre)", datos.get('so2', 'N/A'))
    
    def _mostrar_recomendacion_proyecto(self, aqi):
        """Muestra recomendación para proyectos basada en AQI"""
        print(f"\n{Colors.BRIGHT_WHITE}{'─'*60}{Colors.RESET}")
        print(f"{Colors.BRIGHT_WHITE}{Icons.INFO} RECOMENDACIÓN PARA PROYECTOS ECOTECH{Colors.RESET}")
        print(f"{Colors.BRIGHT_WHITE}{'─'*60}{Colors.RESET}")
        
        if aqi <= 2:
            print(f"\n{Colors.GREEN}{Icons.SUCCESS} UBICACIÓN APROBADA{Colors.RESET}")
            print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} Excelente calidad del aire")
            print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} Ambiente saludable para equipo de trabajo")
            print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} Alineado con valores de sustentabilidad EcoTech")
            print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} No requiere medidas especiales")
        elif aqi == 3:
            print(f"\n{Colors.YELLOW}{Icons.WARNING} UBICACIÓN CONDICIONAL{Colors.RESET}")
            print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} Calidad del aire moderada")
            print(f"  {Colors.CYAN}{Icons.INFO} Recomendaciones:{Colors.RESET}")
            print(f"    {Icons.ARROW} Implementar purificadores de aire en oficinas")
            print(f"    {Icons.ARROW} Monitoreo periódico de condiciones")
            print(f"    {Icons.ARROW} Plan de contingencia para días críticos")
            print(f"    {Icons.ARROW} Evaluación de impacto en bienestar del equipo")
        else:
            print(f"\n{Colors.RED}{Icons.ERROR} UBICACIÓN NO RECOMENDADA{Colors.RESET}")
            print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} Alta contaminación ambiental")
            print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} Riesgo para salud del equipo")
            print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} No alineado con valores de sustentabilidad")
            print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} Sugerencia: Buscar ubicación alternativa")
            print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} Considerar trabajo remoto si proyecto es crítico")


class EmpleadosMenu(MenuBase):
    def __init__(self, servicio_empleados, servicio_usuarios, servicio_roles):
        super().__init__(servicio_empleados)
        self.servicio_usuarios = servicio_usuarios
        self.servicio_roles = servicio_roles
    
    def mostrar(self):
        UI.print_section("Gestión de Empleados", Icons.EMPLOYEE)
        UI.print_menu_option("1", "Agregar empleado", Icons.ADD)
        UI.print_menu_option("2", "Mostrar todos", Icons.VIEW)
        UI.print_menu_option("3", "Buscar por código", Icons.SEARCH)
        UI.print_menu_option("4", "Buscar por nombre", Icons.SEARCH)
        UI.print_menu_option("5", "Modificar", Icons.EDIT)
        UI.print_menu_option("6", "Eliminar", Icons.DELETE)
        UI.print_menu_option("7", "Volver", Icons.BACK)

    def ejecutar(self):
        while True:
            self.mostrar()
            opcion = UI.input_prompt("Seleccione una opción")
            
            if opcion == '1':
                self._agregar_empleado()
            elif opcion == '2':
                empleados = self.servicio.listar_todos()
                if not empleados:
                    UI.print_warning("No hay empleados registrados")
                else:
                    UI.print_section("Lista de Empleados", Icons.EMPLOYEE)
                    for e in empleados:
                        UI.print_item("Nombre", e.get('nombre', 'N/A'), Colors.BRIGHT_CYAN)
                        UI.print_item("Email", e.get('email', 'N/A'), Colors.CYAN)
                        UI.print_item("Salario", f"${e.get('salario', 0):,.2f}" if e.get('salario') else 'N/A', Colors.BRIGHT_GREEN)
                        UI.print_item("Fecha inicio", e.get('fecha_inicio_contrato', 'N/A'))
                        UI.print_item("ID", e.get('id', 'N/A'), Colors.DIM)
                        print()
            elif opcion == '3':
                codigo = UI.input_prompt("Código del empleado", Icons.SEARCH)
                empleado = self.servicio.obtener_por_id(codigo)
                if empleado:
                    UI.print_section("Empleado Encontrado", Icons.SUCCESS)
                    UI.print_item("Nombre", empleado.get('nombre', 'N/A'))
                    UI.print_item("Email", empleado.get('email', 'N/A'))
                    UI.print_item("Salario", f"${empleado.get('salario', 0):,.2f}" if empleado.get('salario') else 'N/A')
                    UI.print_item("Fecha inicio", empleado.get('fecha_inicio_contrato', 'N/A'))
                else:
                    UI.print_error("Empleado no encontrado")
            elif opcion == '4':
                nombre = UI.input_prompt("Nombre a buscar", Icons.SEARCH)
                empleados = self.servicio.buscar_por_nombre(nombre)
                if not empleados:
                    UI.print_warning("No se encontraron empleados")
                else:
                    UI.print_section(f"Resultados para: {nombre}", Icons.SEARCH)
                    for e in empleados:
                        UI.print_item("Nombre", e.get('nombre', 'N/A'))
                        UI.print_item("Email", e.get('email', 'N/A'))
                        print()
            elif opcion == '5':
                codigo = UI.input_prompt("Código del empleado a modificar", Icons.EDIT)
                nombre = UI.input_prompt("Nuevo nombre", Icons.EMPLOYEE)
                email = UI.input_prompt("Nuevo email", Icons.EMAIL)
                self.servicio.modificar(codigo, {'nombre': nombre, 'email': email})
            elif opcion == '6':
                codigo = UI.input_prompt("Código del empleado a eliminar", Icons.DELETE)
                if UI.confirm("¿Está seguro de eliminar el empleado?"):
                    self.servicio.eliminar(codigo)
                else:
                    UI.print_warning("Operación cancelada")
            elif opcion == '7':
                break
            else:
                UI.print_error("Opción inválida")
            
            if opcion != '7':
                UI.pause()
    
    def _agregar_empleado(self):
        """Crea un empleado con su usuario asociado automáticamente"""
        import getpass
        from dominio.auth_models import Usuario
        
        UI.print_section("Agregar Nuevo Empleado", Icons.ADD)
        UI.print_info("Se creará automáticamente un usuario para el empleado")
        print()
        
        # Datos del empleado
        nombre_completo = UI.input_prompt("Nombre completo")
        if not nombre_completo:
            UI.print_error("El nombre es obligatorio")
            return
        
        email = UI.input_prompt("Email")
        if not email or '@' not in email:
            UI.print_error("Email inválido")
            return
        
        # Generar nombre de usuario basado en email
        nombre_usuario_sugerido = email.split('@')[0]
        nombre_usuario = UI.input_prompt(f"Nombre de usuario [{nombre_usuario_sugerido}]") or nombre_usuario_sugerido
        
        # Contraseña inicial
        contrasena = getpass.getpass(f"{Colors.CYAN}{Icons.LOCK} Contraseña inicial (min 6 caracteres): {Colors.RESET}")
        if len(contrasena) < 6:
            UI.print_error("Contraseña muy corta (mínimo 6 caracteres)")
            return
        
        confirmar = getpass.getpass(f"{Colors.CYAN}{Icons.LOCK} Confirmar contraseña: {Colors.RESET}")
        if contrasena != confirmar:
            UI.print_error("Las contraseñas no coinciden")
            return
        
        fecha_inicio = UI.input_prompt("Fecha inicio contrato (YYYY-MM-DD)")
        salario = UI.input_prompt("Salario (ej: 1000.00)")
        
        # Mostrar departamentos disponibles
        print(f"\n{Colors.YELLOW}{Icons.INFO} Departamentos disponibles:{Colors.RESET}")
        from aplicacion.services import DepartamentoService
        dept_service = DepartamentoService()
        departamentos = dept_service.listar_todos()
        
        if departamentos:
            for i, dept in enumerate(departamentos, 1):
                print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} {i}. {dept['nombre']} (ID: {dept['id']})")
            dept_opcion = UI.input_prompt("Seleccione departamento (número) o Enter para ninguno")
            
            if dept_opcion:
                try:
                    idx = int(dept_opcion) - 1
                    if 0 <= idx < len(departamentos):
                        dept_id = departamentos[idx]['id']
                    else:
                        dept_id = None
                except ValueError:
                    dept_id = None
            else:
                dept_id = None
        else:
            UI.print_warning("No hay departamentos disponibles")
            dept_id = None
        
        # Obtener rol de Empleado (nivel 3)
        roles = self.servicio_roles.listar_roles()
        rol_empleado = next((r for r in roles if r['nivel_permisos'] == 3), None)
        
        if not rol_empleado:
            UI.print_error("Error: No existe el rol de Empleado en el sistema")
            print(f"{Colors.YELLOW}{Icons.INFO} Ejecute: python scripts/init_data.py{Colors.RESET}")
            return
        
        try:
            # 1. Crear usuario primero
            usuario_id = str(uuid.uuid4())
            usuario = Usuario(
                id=usuario_id,
                nombre_usuario=nombre_usuario,
                contrasena_cifrada="",  # Se genera en el servicio
                salt="",  # Se genera en el servicio
                rol_id=rol_empleado['id'],
                activo=True
            )
            
            self.servicio_usuarios.crear_usuario(usuario, contrasena)
            
            # 2. Crear empleado vinculado al usuario
            empleado = Empleado(
                id=str(uuid.uuid4()),
                usuario_id=usuario_id,
                nombre=nombre_completo,
                email=email,
                fecha_inicio_contrato=fecha_inicio,
                salario=float(salario) if salario else None,
                departamento_id=dept_id
            )
            
            self.servicio.crear(empleado)
            
            UI.print_success(f"Empleado '{nombre_completo}' creado exitosamente")
            print(f"{Colors.CYAN}{Icons.USER} Usuario: {nombre_usuario}{Colors.RESET}")
            print(f"   Rol: Empleado (Nivel 3)")
            print(f"   Email: {email}")
            if dept_id:
                dept_nombre = next((d['nombre'] for d in departamentos if d['id'] == dept_id), 'N/A')
                print(f"   Departamento: {dept_nombre}")
            
        except Exception as e:
            UI.print_error(f"Error creando empleado: {e}")
            # Si falla la creación del empleado, podría quedar el usuario huérfano
            # En producción, esto debería manejarse con una transacción


class MainMenu:
    def __init__(self, servicio_departamentos, servicio_proyectos, servicio_empleados, 
                 servicio_usuarios, servicio_roles, usuario_actual):
        self.servicio_departamentos = servicio_departamentos
        self.servicio_proyectos = servicio_proyectos
        self.servicio_empleados = servicio_empleados
        self.servicio_usuarios = servicio_usuarios
        self.servicio_roles = servicio_roles
        self.usuario_actual = usuario_actual
        self.nivel_permisos = usuario_actual.get('nivel_permisos', 0)
        self.nombre_rol = usuario_actual.get('nombre_rol', 'Usuario')

    def mostrar(self):
        UI.clear_screen()
        UI.print_header(
            "ECOTECH SOLUTIONS",
            f"Usuario: {self.usuario_actual['nombre_usuario']} | Rol: {self.nombre_rol}",
            "🌱"
        )
        
        print(f"\n{Colors.BRIGHT_WHITE}{Colors.BOLD}MENÚ PRINCIPAL{Colors.RESET}")
        UI.print_divider()
        
        # Opciones disponibles según nivel de permisos
        opciones = []
        
        # EMPLEADO (nivel 3+): Solo consulta de proyectos
        if self.nivel_permisos >= 3:
            UI.print_menu_option("1", "Ver Proyectos", f"{Icons.PROJECT} {Icons.EARTH}")
            opciones.append('1')
        
        # GERENTE (nivel 7+): Gestión de Departamentos y Proyectos
        if self.nivel_permisos >= 7:
            UI.print_menu_option("2", "Gestión de Departamentos", Icons.DEPARTMENT)
            UI.print_menu_option("3", "Gestión de Proyectos", f"{Icons.PROJECT} {Icons.EARTH}")
            UI.print_menu_option("4", "Gestión de Empleados", Icons.EMPLOYEE)
            opciones.extend(['2', '3', '4'])
        
        # ADMINISTRADOR (nivel 10): Acceso completo
        if self.nivel_permisos >= 7:
            print()  # Espaciado
        
        if self.nivel_permisos >= 10:
            UI.print_menu_option("5", "Gestión de Usuarios", Icons.USER)
            UI.print_menu_option("6", "Gestión de Roles", Icons.ROLE)
            opciones.extend(['5', '6'])
        
        # Opciones comunes
        print()  # Espaciado
        if self.nivel_permisos >= 3:
            UI.print_menu_option("7", "Cambiar mi contraseña", Icons.LOCK)
        UI.print_menu_option("0", "Cerrar Sesión", Icons.EXIT)
        opciones.extend(['7', '0'])
        
        return opciones

    def ejecutar(self):
        from .auth_menus import UsuariosMenu, RolesMenu
        
        while True:
            opciones_validas = self.mostrar()
            opcion = UI.input_prompt("Seleccione una opción")
            
            # Verificar si la opción es válida para el rol
            if opcion not in opciones_validas and opcion != '0':
                UI.print_error("Opción inválida o no tiene permisos para acceder")
                UI.pause()
                continue
            
            # EMPLEADO (nivel 3+): Solo ver proyectos
            if opcion == '1' and self.nivel_permisos >= 3:
                if self.nivel_permisos < 7:
                    # Empleados solo pueden ver, no modificar
                    ProyectosMenuSoloLectura(self.servicio_proyectos).ejecutar()
                else:
                    # Gerentes y admins tienen acceso completo
                    ProyectosMenu(self.servicio_proyectos).ejecutar()
            
            # GERENTE (nivel 7+): Gestión completa
            elif opcion == '2' and self.nivel_permisos >= 7:
                DepartamentosMenu(self.servicio_departamentos).ejecutar()
            elif opcion == '3' and self.nivel_permisos >= 7:
                ProyectosMenu(self.servicio_proyectos).ejecutar()
            elif opcion == '4' and self.nivel_permisos >= 7:
                EmpleadosMenu(self.servicio_empleados, self.servicio_usuarios, self.servicio_roles).ejecutar()
            
            # ADMINISTRADOR (nivel 10): Gestión de usuarios y roles
            elif opcion == '5' and self.nivel_permisos >= 10:
                UsuariosMenu(self.servicio_usuarios, self.servicio_roles, self.usuario_actual).ejecutar()
            elif opcion == '6' and self.nivel_permisos >= 10:
                RolesMenu(self.servicio_roles).ejecutar()
            
            # Cambiar contraseña (todos los usuarios)
            elif opcion == '7' and self.nivel_permisos >= 3:
                self._cambiar_mi_contrasena()
            
            # Cerrar sesión
            elif opcion == '0':
                UI.print_goodbye()
                break
            else:
                UI.print_error("No tiene permisos para acceder a esta opción")
                UI.pause()
    
    def _cambiar_mi_contrasena(self):
        """Permite al usuario cambiar su propia contraseña"""
        import getpass
        
        UI.print_section("Cambiar Mi Contraseña", Icons.LOCK)
        
        contrasena_actual = getpass.getpass(f"\n{Colors.BRIGHT_YELLOW}🔒 Contraseña actual:{Colors.RESET} ")
        
        # Verificar contraseña actual
        from aplicacion.auth_services import AuthService
        auth_service = AuthService()
        if not auth_service.autenticar(self.usuario_actual['nombre_usuario'], contrasena_actual):
            UI.print_error("Contraseña actual incorrecta")
            UI.pause()
            return
        
        nueva_contrasena = getpass.getpass(f"{Colors.BRIGHT_YELLOW}🔑 Nueva contraseña (min 6 caracteres):{Colors.RESET} ")
        if len(nueva_contrasena) < 6:
            UI.print_error("La contraseña debe tener al menos 6 caracteres")
            UI.pause()
            return
        
        confirmar = getpass.getpass(f"{Colors.BRIGHT_YELLOW}🔑 Confirmar nueva contraseña:{Colors.RESET} ")
        if nueva_contrasena != confirmar:
            UI.print_error("Las contraseñas no coinciden")
            UI.pause()
            return
        
        # Cambiar contraseña
        self.servicio_usuarios.cambiar_contrasena(
            self.usuario_actual['id'], 
            nueva_contrasena
        )
        UI.print_success("Contraseña cambiada exitosamente")
        UI.pause()


class ProyectosMenuSoloLectura(MenuBase):
    """Menú de solo lectura para empleados"""
    
    def mostrar(self):
        UI.print_section(f"{Icons.PROJECT} {Icons.EARTH} Proyectos (Solo Consulta)", Icons.VIEW)
        UI.print_menu_option("1", "Mostrar Todos", Icons.VIEW)
        UI.print_menu_option("2", "Buscar por código", Icons.SEARCH)
        UI.print_menu_option("3", "Buscar por nombre", Icons.SEARCH)
        UI.print_menu_option("4", "Evaluar calidad del aire en ubicación", f"{Icons.EARTH} {Icons.CLOUD}")
        UI.print_menu_option("5", "Volver", Icons.BACK)
    
    def ejecutar(self):
        while True:
            self.mostrar()
            opcion = UI.input_prompt("Seleccione una opción")
            if opcion == '1':
                proyectos = self.servicio.listar_todos()
                if not proyectos:
                    UI.print_warning("No hay proyectos registrados")
                else:
                    for idx, p in enumerate(proyectos, 1):
                        print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} {idx}. {p}")
            elif opcion == '2':
                codigo = UI.input_prompt("Código")
                proyecto = self.servicio.obtener_por_id(codigo)
                if proyecto:
                    UI.print_success(f"Proyecto encontrado: {proyecto}")
                else:
                    UI.print_error("Proyecto no encontrado")
            elif opcion == '3':
                nombre = UI.input_prompt("Nombre")
                proyectos = self.servicio.buscar_por_nombre(nombre)
                if not proyectos:
                    UI.print_warning("No se encontraron proyectos")
                else:
                    for idx, p in enumerate(proyectos, 1):
                        print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} {idx}. {p}")
            elif opcion == '4':
                self._evaluar_calidad_aire()
            elif opcion == '5':
                break
            else:
                UI.print_error("Opción inválida")
            
            if opcion != '5':
                UI.pause()
    
    def _evaluar_calidad_aire(self):
        """Evaluar calidad del aire en una ubicación específica"""
        UI.print_section(f"{Icons.EARTH} EVALUACIÓN DE CALIDAD DEL AIRE", Icons.CLOUD)
        UI.print_info("Evalúe condiciones ambientales antes de iniciar proyectos o expandir operaciones")
        print()
        
        ciudad = UI.input_prompt("Ciudad a evaluar")
        if not ciudad:
            UI.print_error("Debe ingresar una ciudad")
            return
        
        pais = UI.input_prompt("Código de país (ej: CL, AR, PE) [CL]").upper() or "CL"
        
        print(f"\n{Colors.CYAN}{Icons.SEARCH} Consultando calidad del aire en {ciudad}, {pais}...{Colors.RESET}")
        datos = self.servicio.obtener_calidad_aire_por_ciudad(ciudad, pais)
        
        if datos:
            self._mostrar_reporte_calidad_aire(datos, ciudad)
            self._mostrar_recomendacion_proyecto(datos.get('aqi', 0))
        else:
            UI.print_error("No se pudo obtener información de calidad del aire")
            print(f"\n{Colors.YELLOW}{Icons.WARNING} Posibles causas:{Colors.RESET}")
            print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} Ciudad no encontrada (verifica ortografía)")
            print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} API_KEY no configurada (ver README.md)")
            print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} Sin conexión a internet")
        
        UI.pause()
    
    def _mostrar_reporte_calidad_aire(self, datos, ciudad):
        """Muestra reporte formateado de calidad del aire"""
        from aplicacion.api_client import EcoAPIClient
        
        aqi = datos.get('aqi', 0)
        interpretacion = EcoAPIClient.interpretar_aqi(aqi)
        
        # Determinar color según AQI
        if aqi <= 2:
            color_aqi = Colors.GREEN
        elif aqi == 3:
            color_aqi = Colors.YELLOW
        else:
            color_aqi = Colors.RED
        
        print(f"\n{Colors.BRIGHT_WHITE}{'─'*60}{Colors.RESET}")
        print(f"{Colors.BRIGHT_WHITE}{Icons.CHART} REPORTE DE CALIDAD DEL AIRE - {ciudad.upper()}{Colors.RESET}")
        print(f"{Colors.BRIGHT_WHITE}{'─'*60}{Colors.RESET}")
        print(f"\n{color_aqi}{Icons.CHART} Índice de Calidad (AQI): {aqi}/5 - {interpretacion}{Colors.RESET}")
        print(f"\n{Colors.CYAN}{Icons.MOLECULE} Contaminantes principales (μg/m³):{Colors.RESET}")
        print(f"  {Icons.DOT} PM2.5 (Partículas finas): {datos.get('pm2_5', 'N/A')}")
        print(f"  {Icons.DOT} PM10 (Partículas):        {datos.get('pm10', 'N/A')}")
        print(f"  {Icons.DOT} NO₂ (Dióxido nitrógeno):  {datos.get('no2', 'N/A')}")
        print(f"  {Icons.DOT} O₃ (Ozono):               {datos.get('o3', 'N/A')}")
        print(f"  {Icons.DOT} SO₂ (Dióxido azufre):     {datos.get('so2', 'N/A')}")
    
    def _mostrar_recomendacion_proyecto(self, aqi):
        """Muestra recomendación para proyectos basada en AQI"""
        print(f"\n{Colors.BRIGHT_WHITE}{'─'*60}{Colors.RESET}")
        print(f"{Colors.BRIGHT_WHITE}{Icons.INFO} RECOMENDACIÓN PARA PROYECTOS ECOTECH{Colors.RESET}")
        print(f"{Colors.BRIGHT_WHITE}{'─'*60}{Colors.RESET}")
        
        if aqi <= 2:
            print(f"\n{Colors.GREEN}{Icons.SUCCESS} UBICACIÓN APROBADA{Colors.RESET}")
            print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} Excelente calidad del aire")
            print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} Ambiente saludable para equipo de trabajo")
            print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} Alineado con valores de sustentabilidad EcoTech")
            print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} No requiere medidas especiales")
        elif aqi == 3:
            print(f"\n{Colors.YELLOW}{Icons.WARNING} UBICACIÓN CONDICIONAL{Colors.RESET}")
            print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} Calidad del aire moderada")
            print(f"  {Colors.CYAN}{Icons.INFO} Recomendaciones:{Colors.RESET}")
            print(f"    {Icons.ARROW} Implementar purificadores de aire en oficinas")
            print(f"    {Icons.ARROW} Monitoreo periódico de condiciones")
            print(f"    {Icons.ARROW} Plan de contingencia para días críticos")
            print(f"    {Icons.ARROW} Evaluación de impacto en bienestar del equipo")
        else:
            print(f"\n{Colors.RED}{Icons.ERROR} UBICACIÓN NO RECOMENDADA{Colors.RESET}")
            print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} Alta contaminación ambiental")
            print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} Riesgo para salud del equipo")
            print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} No alineado con valores de sustentabilidad")
            print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} Sugerencia: Buscar ubicación alternativa")
            print(f"  {Colors.BRIGHT_BLACK}•{Colors.RESET} Considerar trabajo remoto si proyecto es crítico")

