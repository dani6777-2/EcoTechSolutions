"""
Utilidades para mejorar la interfaz de usuario en terminal
"""
import os
import sys


class Colors:
    """Códigos ANSI para colores en terminal"""
    # Colores básicos
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    
    # Colores de texto
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Colores de texto brillantes
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Colores de fondo
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'


class UI:
    """Clase para mejorar la interfaz de usuario"""
    
    @staticmethod
    def clear_screen():
        """Limpia la pantalla"""
        os.system('clear' if os.name != 'nt' else 'cls')
    
    @staticmethod
    def print_header(title, subtitle=None, icon="🌱"):
        """Imprime un encabezado atractivo"""
        width = 70
        print("\n" + Colors.BRIGHT_GREEN + "═" * width + Colors.RESET)
        print(f"{Colors.BRIGHT_GREEN}{Colors.BOLD}   {icon} {title.upper()}{Colors.RESET}")
        if subtitle:
            print(f"{Colors.CYAN}   {subtitle}{Colors.RESET}")
        print(Colors.BRIGHT_GREEN + "═" * width + Colors.RESET)
    
    @staticmethod
    def print_section(title, icon="📋"):
        """Imprime un título de sección"""
        print(f"\n{Colors.BRIGHT_CYAN}{Colors.BOLD}{icon} {title}{Colors.RESET}")
        print(Colors.CYAN + "─" * 60 + Colors.RESET)
    
    @staticmethod
    def print_menu_option(number, text, icon="", enabled=True):
        """Imprime una opción de menú con formato"""
        if enabled:
            color = Colors.BRIGHT_WHITE
            status = ""
        else:
            color = Colors.DIM
            status = " (no disponible)"
        
        print(f"{color}{number}. {icon} {text}{status}{Colors.RESET}")
    
    @staticmethod
    def print_success(message):
        """Imprime mensaje de éxito"""
        print(f"\n{Colors.BRIGHT_GREEN}✅ {message}{Colors.RESET}")
    
    @staticmethod
    def print_error(message):
        """Imprime mensaje de error"""
        print(f"\n{Colors.BRIGHT_RED}❌ {message}{Colors.RESET}")
    
    @staticmethod
    def print_warning(message):
        """Imprime mensaje de advertencia"""
        print(f"\n{Colors.BRIGHT_YELLOW}⚠️  {message}{Colors.RESET}")
    
    @staticmethod
    def print_info(message, icon="💡"):
        """Imprime mensaje informativo"""
        print(f"\n{Colors.BRIGHT_BLUE}{icon} {message}{Colors.RESET}")
    
    @staticmethod
    def print_item(label, value, color=None):
        """Imprime un item con etiqueta y valor"""
        label_color = Colors.BRIGHT_BLACK if not color else color
        print(f"{label_color}  • {label}:{Colors.RESET} {value}")
    
    @staticmethod
    def print_box(lines, title=None, color=Colors.CYAN):
        """Imprime contenido en una caja"""
        width = max(len(line) for line in lines) + 4
        
        print(f"\n{color}┌{'─' * (width - 2)}┐{Colors.RESET}")
        
        if title:
            padding = (width - len(title) - 4) // 2
            print(f"{color}│{' ' * padding}{Colors.BOLD}{title}{Colors.RESET}{color}{' ' * (width - len(title) - padding - 2)}│{Colors.RESET}")
            print(f"{color}├{'─' * (width - 2)}┤{Colors.RESET}")
        
        for line in lines:
            padding = width - len(line) - 2
            print(f"{color}│{Colors.RESET} {line}{' ' * padding}{color}│{Colors.RESET}")
        
        print(f"{color}└{'─' * (width - 2)}┘{Colors.RESET}")
    
    @staticmethod
    def print_table(headers, rows, colors=None):
        """Imprime una tabla formateada"""
        if not rows:
            UI.print_warning("No hay datos para mostrar")
            return
        
        # Calcular anchos de columnas
        col_widths = [len(h) for h in headers]
        for row in rows:
            for i, cell in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(cell)))
        
        # Imprimir encabezado
        header_line = "  ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers))
        print(f"\n{Colors.BOLD}{Colors.BRIGHT_CYAN}{header_line}{Colors.RESET}")
        print(Colors.CYAN + "─" * len(header_line) + Colors.RESET)
        
        # Imprimir filas
        for row in rows:
            row_line = "  ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row))
            print(row_line)
    
    @staticmethod
    def input_prompt(prompt, icon="▶"):
        """Solicita input con formato mejorado"""
        return input(f"\n{Colors.BRIGHT_YELLOW}{icon} {prompt}{Colors.RESET} ").strip()
    
    @staticmethod
    def confirm(message):
        """Solicita confirmación s/n"""
        response = UI.input_prompt(f"{message} (s/n)", icon="❓").lower()
        return response == 's'
    
    @staticmethod
    def pause(message="Presione Enter para continuar"):
        """Pausa la ejecución"""
        input(f"\n{Colors.DIM}[{message}]{Colors.RESET}")
    
    @staticmethod
    def print_divider(char="─", length=70, color=Colors.BRIGHT_BLACK):
        """Imprime una línea divisoria"""
        print(f"{color}{char * length}{Colors.RESET}")
    
    @staticmethod
    def print_welcome(username, role):
        """Imprime mensaje de bienvenida personalizado"""
        UI.clear_screen()
        UI.print_header("ECOTECH SOLUTIONS", "Gestión Empresarial Sustentable", "🌱")
        print(f"\n{Colors.BRIGHT_GREEN}  Bienvenido/a, {Colors.BOLD}{username}{Colors.RESET}")
        print(f"{Colors.CYAN}  Rol: {role}{Colors.RESET}")
        UI.print_divider()
    
    @staticmethod
    def print_goodbye():
        """Imprime mensaje de despedida"""
        print(f"\n{Colors.BRIGHT_GREEN}🌱 Gracias por usar EcoTech Solutions{Colors.RESET}")
        print(f"{Colors.CYAN}✓ Sesión cerrada. ¡Hasta luego!{Colors.RESET}\n")


class ProgressBar:
    """Barra de progreso simple"""
    
    @staticmethod
    def show(current, total, prefix='', suffix='', length=40):
        """Muestra una barra de progreso"""
        filled = int(length * current // total)
        bar = '█' * filled + '░' * (length - filled)
        percent = 100 * (current / float(total))
        
        sys.stdout.write(f'\r{prefix} |{Colors.BRIGHT_GREEN}{bar}{Colors.RESET}| {percent:.1f}% {suffix}')
        sys.stdout.flush()
        
        if current == total:
            print()


class Icons:
    """Iconos útiles para la interfaz"""
    # Acciones
    ADD = "➕"
    EDIT = "✏️"
    DELETE = "🗑️"
    SEARCH = "🔍"
    VIEW = "👁️"
    BACK = "◀️"
    EXIT = "🚪"
    
    # Estados
    SUCCESS = "✅"
    ERROR = "❌"
    WARNING = "⚠️"
    INFO = "💡"
    QUESTION = "❓"
    
    # Módulos
    DEPARTMENT = "🏢"
    PROJECT = "📊"
    EMPLOYEE = "👤"
    USER = "👥"
    ROLE = "🔐"
    
    # EcoTech
    EARTH = "🌍"
    LEAF = "🌱"
    TREE = "🌳"
    AIR = "💨"
    RECYCLE = "♻️"
    
    # Otros
    CALENDAR = "📅"
    MONEY = "💰"
    EMAIL = "📧"
    LOCK = "🔒"
    UNLOCK = "🔓"
    SETTINGS = "⚙️"
    LIST = "📋"
    SHIELD = "🛡️"
    MODULE = "📦"
    CLOUD = "☁️"
    MOLECULE = "🔬"
    CHART = "📈"
    DOT = "•"
    ARROW = "→"
