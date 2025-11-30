from aplicacion.services import DepartamentoService, ProyectoService, EmpleadoService
from aplicacion.auth_services import AuthService, UsuarioService, RolService
from presentacion.menus import MainMenu
from presentacion.auth_menus import LoginMenu


def main():
    # Servicios de autenticación
    auth_service = AuthService()
    usuario_service = UsuarioService()
    rol_service = RolService()
    
    # Menú de login
    login_menu = LoginMenu(auth_service)
    usuario_actual = login_menu.ejecutar()
    
    if not usuario_actual:
        # Si el login falla, terminar aplicación
        return
    
    # Servicios de la aplicación
    servicio_dept = DepartamentoService()
    servicio_proj = ProyectoService()
    servicio_emp = EmpleadoService()
    
    # Menú principal con usuario autenticado
    menu = MainMenu(
        servicio_dept, 
        servicio_proj, 
        servicio_emp,
        usuario_service,
        rol_service,
        usuario_actual
    )
    menu.ejecutar()


if __name__ == '__main__':
    main()
