#!/usr/bin/env python3
"""
Demostración de la nueva interfaz mejorada de EcoTech Solutions
"""
import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from presentacion.ui_helpers import UI, Colors, Icons, ProgressBar
import time


def demo_colores():
    """Demostración de colores"""
    UI.print_section("Paleta de Colores", Icons.SETTINGS)
    
    print(f"{Colors.RED}Texto en rojo{Colors.RESET}")
    print(f"{Colors.GREEN}Texto en verde{Colors.RESET}")
    print(f"{Colors.YELLOW}Texto en amarillo{Colors.RESET}")
    print(f"{Colors.BLUE}Texto en azul{Colors.RESET}")
    print(f"{Colors.MAGENTA}Texto en magenta{Colors.RESET}")
    print(f"{Colors.CYAN}Texto en cian{Colors.RESET}")
    print(f"{Colors.BRIGHT_GREEN}Texto en verde brillante{Colors.RESET}")
    print(f"{Colors.BOLD}Texto en negrita{Colors.RESET}")
    print(f"{Colors.DIM}Texto atenuado{Colors.RESET}")
    print(f"{Colors.UNDERLINE}Texto subrayado{Colors.RESET}")
    
    UI.pause()


def demo_mensajes():
    """Demostración de mensajes"""
    UI.print_section("Tipos de Mensajes", Icons.INFO)
    
    UI.print_success("Operación completada exitosamente")
    UI.print_error("Ha ocurrido un error en el proceso")
    UI.print_warning("Advertencia: Verifique los datos ingresados")
    UI.print_info("Información importante para el usuario")
    UI.print_info("Operación de actualización", Icons.SETTINGS)
    
    UI.pause()


def demo_menus():
    """Demostración de menús"""
    UI.print_section("Opciones de Menú", Icons.ROLE)
    
    UI.print_menu_option("1", "Crear nuevo registro", Icons.ADD)
    UI.print_menu_option("2", "Ver todos los registros", Icons.VIEW)
    UI.print_menu_option("3", "Buscar registro", Icons.SEARCH)
    UI.print_menu_option("4", "Editar registro", Icons.EDIT)
    UI.print_menu_option("5", "Eliminar registro", Icons.DELETE)
    UI.print_menu_option("0", "Volver al menú principal", Icons.BACK)
    
    UI.pause()


def demo_tablas():
    """Demostración de tablas"""
    UI.print_section("Tabla de Datos", Icons.PROJECT)
    
    headers = ["ID", "Nombre", "Departamento", "Estado"]
    rows = [
        ["001", "Juan Pérez", "Tecnología", "Activo"],
        ["002", "María González", "Ventas", "Activo"],
        ["003", "Carlos Rodríguez", "Recursos Humanos", "Inactivo"]
    ]
    
    UI.print_table(headers, rows)
    
    UI.pause()


def demo_items():
    """Demostración de items"""
    UI.print_section("Detalles del Empleado", Icons.EMPLOYEE)
    
    UI.print_item("Nombre", "Daniel Morales")
    UI.print_item("Email", "daniel@ecotech.com")
    UI.print_item("Departamento", "Tecnología")
    UI.print_item("Salario", "$45,000", Colors.BRIGHT_GREEN)
    UI.print_item("Fecha de inicio", "2025-01-15")
    UI.print_item("Estado", "✓ Activo", Colors.GREEN)
    
    UI.pause()


def demo_cajas():
    """Demostración de cajas"""
    UI.print_section("Mensajes en Caja", Icons.INFO)
    
    UI.print_box([
        "Este es un mensaje importante",
        "que está contenido en una caja",
        "para llamar la atención del usuario"
    ], title="IMPORTANTE", color=Colors.BRIGHT_YELLOW)
    
    print()
    
    UI.print_box([
        "Usuario: admin",
        "Rol: Administrador",
        "Nivel de permisos: 10",
        "Último acceso: 2025-12-03 10:30:15"
    ], title="INFORMACIÓN DE SESIÓN", color=Colors.BRIGHT_CYAN)
    
    UI.pause()


def demo_barra_progreso():
    """Demostración de barra de progreso"""
    UI.print_section("Barra de Progreso", Icons.SETTINGS)
    
    print(f"\n{Colors.BRIGHT_CYAN}Procesando registros...{Colors.RESET}\n")
    
    total = 50
    for i in range(total + 1):
        ProgressBar.show(i, total, prefix='Progreso:', suffix='Completo', length=40)
        time.sleep(0.05)
    
    UI.print_success("¡Proceso completado!")
    
    UI.pause()


def demo_header():
    """Demostración de encabezados"""
    UI.clear_screen()
    UI.print_header("ECOTECH SOLUTIONS", "Sistema de Gestión Empresarial Sustentable", "🌱")
    
    print(f"\n{Colors.BRIGHT_CYAN}Esta es la nueva interfaz mejorada de EcoTech Solutions{Colors.RESET}")
    print(f"{Colors.CYAN}Con colores vibrantes, iconos expresivos y mejor legibilidad{Colors.RESET}")
    
    UI.pause()


def demo_iconos():
    """Demostración de iconos disponibles"""
    UI.print_section("Iconos Disponibles", Icons.LEAF)
    
    print(f"\n{Colors.BOLD}Acciones:{Colors.RESET}")
    print(f"  {Icons.ADD} Agregar  {Icons.EDIT} Editar  {Icons.DELETE} Eliminar")
    print(f"  {Icons.SEARCH} Buscar  {Icons.VIEW} Ver  {Icons.BACK} Volver  {Icons.EXIT} Salir")
    
    print(f"\n{Colors.BOLD}Estados:{Colors.RESET}")
    print(f"  {Icons.SUCCESS} Éxito  {Icons.ERROR} Error  {Icons.WARNING} Advertencia")
    print(f"  {Icons.INFO} Info  {Icons.QUESTION} Pregunta")
    
    print(f"\n{Colors.BOLD}Módulos:{Colors.RESET}")
    print(f"  {Icons.DEPARTMENT} Departamentos  {Icons.PROJECT} Proyectos")
    print(f"  {Icons.EMPLOYEE} Empleados  {Icons.USER} Usuarios  {Icons.ROLE} Roles")
    
    print(f"\n{Colors.BOLD}EcoTech:{Colors.RESET}")
    print(f"  {Icons.EARTH} Tierra  {Icons.LEAF} Hoja  {Icons.TREE} Árbol")
    print(f"  {Icons.AIR} Aire  {Icons.RECYCLE} Reciclaje")
    
    print(f"\n{Colors.BOLD}Otros:{Colors.RESET}")
    print(f"  {Icons.CALENDAR} Calendario  {Icons.MONEY} Dinero  {Icons.EMAIL} Email")
    print(f"  {Icons.LOCK} Bloqueado  {Icons.UNLOCK} Desbloqueado  {Icons.SETTINGS} Configuración")
    
    UI.pause()


def demo_inputs():
    """Demostración de inputs"""
    UI.print_section("Entrada de Datos", Icons.EDIT)
    
    nombre = UI.input_prompt("Ingrese su nombre", Icons.USER)
    if nombre:
        UI.print_success(f"Hola, {nombre}!")
    
    confirmar = UI.confirm("¿Desea continuar con la demostración?")
    if confirmar:
        UI.print_success("Continuando...")
    else:
        UI.print_warning("Demostración cancelada")
    
    UI.pause()


def menu_principal():
    """Menú principal de la demostración"""
    while True:
        UI.clear_screen()
        UI.print_header("DEMO - INTERFAZ MEJORADA", "EcoTech Solutions", "🎨")
        
        print(f"\n{Colors.BRIGHT_WHITE}{Colors.BOLD}DEMOSTRACIÓN DE CARACTERÍSTICAS{Colors.RESET}")
        UI.print_divider()
        
        UI.print_menu_option("1", "Encabezados", "📋")
        UI.print_menu_option("2", "Colores", "🎨")
        UI.print_menu_option("3", "Mensajes (éxito, error, advertencia)", Icons.INFO)
        UI.print_menu_option("4", "Opciones de menú", Icons.ROLE)
        UI.print_menu_option("5", "Tablas de datos", Icons.PROJECT)
        UI.print_menu_option("6", "Items y detalles", Icons.EMPLOYEE)
        UI.print_menu_option("7", "Cajas de mensaje", Icons.INFO)
        UI.print_menu_option("8", "Barra de progreso", Icons.SETTINGS)
        UI.print_menu_option("9", "Iconos disponibles", Icons.LEAF)
        UI.print_menu_option("10", "Inputs interactivos", Icons.EDIT)
        UI.print_menu_option("0", "Salir de la demostración", Icons.EXIT)
        
        opcion = UI.input_prompt("Seleccione una opción")
        
        if opcion == '1':
            demo_header()
        elif opcion == '2':
            demo_colores()
        elif opcion == '3':
            demo_mensajes()
        elif opcion == '4':
            demo_menus()
        elif opcion == '5':
            demo_tablas()
        elif opcion == '6':
            demo_items()
        elif opcion == '7':
            demo_cajas()
        elif opcion == '8':
            demo_barra_progreso()
        elif opcion == '9':
            demo_iconos()
        elif opcion == '10':
            demo_inputs()
        elif opcion == '0':
            UI.print_goodbye()
            break
        else:
            UI.print_error("Opción inválida")
            UI.pause()


def main():
    """Función principal"""
    print(f"""
{Colors.BRIGHT_GREEN}╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║  🌱 ECOTECH SOLUTIONS - DEMOSTRACIÓN DE INTERFAZ MEJORADA  🌱    ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.BRIGHT_CYAN}Esta demostración muestra las mejoras visuales implementadas:{Colors.RESET}

  ✅ Colores vibrantes con códigos ANSI
  ✅ Iconos expresivos para mejor UX
  ✅ Mensajes formateados (éxito, error, advertencia)
  ✅ Tablas y cajas de información
  ✅ Barras de progreso
  ✅ Prompts interactivos mejorados
  ✅ Encabezados y secciones bien definidas
  ✅ Mejor espaciado y legibilidad

{Colors.BRIGHT_YELLOW}¡Presione Enter para comenzar la demostración!{Colors.RESET}
""")
    input()
    
    try:
        menu_principal()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.BRIGHT_YELLOW}Demostración interrumpida por el usuario{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.BRIGHT_RED}Error: {e}{Colors.RESET}")


if __name__ == "__main__":
    main()
