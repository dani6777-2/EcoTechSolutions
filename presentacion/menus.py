from .menu_base import MenuBase
from dominio.models import Departamento, Proyecto, Empleado
import uuid


class DepartamentosMenu(MenuBase):
    def mostrar(self):
        print("\n-- Menú Departamentos --")
        print("1. Agregar")
        print("2. Mostrar Todos")
        print("3. Buscar por código")
        print("4. Buscar por nombre")
        print("5. Modificar")
        print("6. Eliminar")
        print("7. Volver")

    def ejecutar(self):
        while True:
            self.mostrar()
            opcion = self.limpiar_input("Opción: ")
            if opcion == '1':
                nombre = self.limpiar_input("Nombre: ")
                descripcion = self.limpiar_input("Descripción: ")
                dept = Departamento(id=str(uuid.uuid4()), nombre=nombre, descripcion=descripcion)
                self.servicio.crear(dept)
            elif opcion == '2':
                for d in self.servicio.listar_todos():
                    print(d)
            elif opcion == '3':
                codigo = self.limpiar_input("Código: ")
                print(self.servicio.obtener_por_id(codigo))
            elif opcion == '4':
                nombre = self.limpiar_input("Nombre: ")
                for d in self.servicio.buscar_por_nombre(nombre):
                    print(d)
            elif opcion == '5':
                codigo = self.limpiar_input("Código a modificar: ")
                nombre = self.limpiar_input("Nuevo nombre: ")
                descripcion = self.limpiar_input("Nueva descripción: ")
                self.servicio.modificar(codigo, {'nombre': nombre, 'descripcion': descripcion})
            elif opcion == '6':
                codigo = self.limpiar_input("Código a eliminar: ")
                self.servicio.eliminar(codigo)
            elif opcion == '7':
                break
            else:
                print("Opción inválida")


class ProyectosMenu(MenuBase):
    def mostrar(self):
        print("\n-- Menú Proyectos --")
        print("1. Agregar")
        print("2. Mostrar Todos")
        print("3. Buscar por código")
        print("4. Buscar por nombre")
        print("5. Modificar")
        print("6. Eliminar")
        print("7. Volver")

    def ejecutar(self):
        while True:
            self.mostrar()
            opcion = self.limpiar_input("Opción: ")
            if opcion == '1':
                nombre = self.limpiar_input("Nombre: ")
                descripcion = self.limpiar_input("Descripción: ")
                fecha_inicio = self.limpiar_input("Fecha inicio (YYYY-MM-DD): ")
                fecha_fin = self.limpiar_input("Fecha fin (YYYY-MM-DD) o vacío: ")
                p = Proyecto(id=str(uuid.uuid4()), nombre=nombre, descripcion=descripcion, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin or None)
                self.servicio.crear(p)
            elif opcion == '2':
                for p in self.servicio.listar_todos():
                    print(p)
            elif opcion == '3':
                codigo = self.limpiar_input("Código: ")
                print(self.servicio.obtener_por_id(codigo))
            elif opcion == '4':
                nombre = self.limpiar_input("Nombre: ")
                for p in self.servicio.buscar_por_nombre(nombre):
                    print(p)
            elif opcion == '5':
                codigo = self.limpiar_input("Código a modificar: ")
                nombre = self.limpiar_input("Nuevo nombre: ")
                descripcion = self.limpiar_input("Nueva descripción: ")
                self.servicio.modificar(codigo, {'nombre': nombre, 'descripcion': descripcion})
            elif opcion == '6':
                codigo = self.limpiar_input("Código a eliminar: ")
                self.servicio.eliminar(codigo)
            elif opcion == '7':
                break
            else:
                print("Opción inválida")


class EmpleadosMenu(MenuBase):
    def mostrar(self):
        print("\n-- Menú Empleados --")
        print("1. Agregar")
        print("2. Mostrar Todos")
        print("3. Buscar por código")
        print("4. Buscar por nombre")
        print("5. Modificar")
        print("6. Eliminar")
        print("7. Volver")

    def ejecutar(self):
        while True:
            self.mostrar()
            opcion = self.limpiar_input("Opción: ")
            if opcion == '1':
                usuario_id = self.limpiar_input("Usuario ID: ")
                nombre = self.limpiar_input("Nombre completo: ")
                email = self.limpiar_input("Email: ")
                fecha_inicio = self.limpiar_input("Fecha inicio (YYYY-MM-DD): ")
                salario = self.limpiar_input("Salario (ej: 1000.00): ")
                dept = self.limpiar_input("Departamento ID o vacío: ") or None
                e = Empleado(id=str(uuid.uuid4()), usuario_id=usuario_id, nombre=nombre, email=email, fecha_inicio_contrato=fecha_inicio, salario=salario, departamento_id=dept)
                self.servicio.crear(e)
            elif opcion == '2':
                for e in self.servicio.listar_todos():
                    print(e)
            elif opcion == '3':
                codigo = self.limpiar_input("Código: ")
                print(self.servicio.obtener_por_id(codigo))
            elif opcion == '4':
                nombre = self.limpiar_input("Nombre: ")
                for e in self.servicio.buscar_por_nombre(nombre):
                    print(e)
            elif opcion == '5':
                codigo = self.limpiar_input("Código a modificar: ")
                nombre = self.limpiar_input("Nuevo nombre: ")
                email = self.limpiar_input("Nuevo email: ")
                self.servicio.modificar(codigo, {'nombre': nombre, 'email': email})
            elif opcion == '6':
                codigo = self.limpiar_input("Código a eliminar: ")
                self.servicio.eliminar(codigo)
            elif opcion == '7':
                break
            else:
                print("Opción inválida")


class MainMenu:
    def __init__(self, servicio_departamentos, servicio_proyectos, servicio_empleados, 
                 servicio_usuarios, servicio_roles, usuario_actual):
        self.servicio_departamentos = servicio_departamentos
        self.servicio_proyectos = servicio_proyectos
        self.servicio_empleados = servicio_empleados
        self.servicio_usuarios = servicio_usuarios
        self.servicio_roles = servicio_roles
        self.usuario_actual = usuario_actual

    def mostrar(self):
        print("\n" + "="*50)
        print(f"   ECOTECH MANAGEMENT - Usuario: {self.usuario_actual['nombre_usuario']}")
        print("="*50)
        print("1. Menú de Departamentos")
        print("2. Menú de Proyectos")
        print("3. Menú de Empleados")
        print("4. Gestión de Usuarios")
        print("5. Gestión de Roles")
        print("6. Cerrar Sesión")

    def ejecutar(self):
        from .auth_menus import UsuariosMenu, RolesMenu
        
        while True:
            self.mostrar()
            opcion = input("Opción: ").strip()
            if opcion == '1':
                DepartamentosMenu(self.servicio_departamentos).ejecutar()
            elif opcion == '2':
                ProyectosMenu(self.servicio_proyectos).ejecutar()
            elif opcion == '3':
                EmpleadosMenu(self.servicio_empleados).ejecutar()
            elif opcion == '4':
                UsuariosMenu(self.servicio_usuarios, self.servicio_roles).ejecutar()
            elif opcion == '5':
                RolesMenu(self.servicio_roles).ejecutar()
            elif opcion == '6':
                print("\n✓ Sesión cerrada. Hasta luego!")
                break
            else:
                print("❌ Opción inválida")
