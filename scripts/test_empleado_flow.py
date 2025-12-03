#!/usr/bin/env python3
"""
Script de prueba para validar el flujo de creación de empleados
"""
import os
import sys

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aplicacion.services import EmpleadoService, DepartamentoService
from aplicacion.auth_services import UsuarioService, RolService


def verificar_empleados():
    """Verifica empleados existentes en el sistema"""
    empleado_service = EmpleadoService()
    
    print("\n📋 EMPLEADOS REGISTRADOS EN EL SISTEMA")
    print("="*60)
    
    empleados = empleado_service.listar_todos()
    
    if not empleados:
        print("  No hay empleados registrados")
    else:
        for emp in empleados:
            print(f"\n• {emp['nombre']}")
            print(f"  Email: {emp['email']}")
            print(f"  Usuario ID: {emp['usuario_id']}")
            print(f"  Fecha inicio: {emp['fecha_inicio_contrato']}")
            print(f"  Salario: ${emp['salario'] if emp['salario'] else 'N/A'}")
            print(f"  Departamento: {emp.get('departamento_id', 'Sin asignar')}")
    
    print("\n" + "="*60)


def verificar_usuarios_empleados():
    """Verifica usuarios con rol de empleado"""
    usuario_service = UsuarioService()
    rol_service = RolService()
    
    print("\n👥 USUARIOS CON ROL DE EMPLEADO")
    print("="*60)
    
    # Obtener rol de empleado
    roles = rol_service.listar_roles()
    rol_empleado = next((r for r in roles if r['nivel_permisos'] == 3), None)
    
    if not rol_empleado:
        print("❌ No existe el rol de Empleado en el sistema")
        return
    
    usuarios = usuario_service.listar_usuarios()
    usuarios_empleado = [u for u in usuarios if u['rol_id'] == rol_empleado['id']]
    
    if not usuarios_empleado:
        print("  No hay usuarios con rol de Empleado")
    else:
        for usr in usuarios_empleado:
            estado = "✓ Activo" if usr['activo'] else "✗ Inactivo"
            print(f"\n• Usuario: {usr['nombre_usuario']}")
            print(f"  ID: {usr['id']}")
            print(f"  Estado: {estado}")
            print(f"  Creado: {usr['fecha_creacion']}")
    
    print("\n" + "="*60)


def verificar_departamentos():
    """Verifica departamentos disponibles"""
    dept_service = DepartamentoService()
    
    print("\n🏢 DEPARTAMENTOS DISPONIBLES")
    print("="*60)
    
    departamentos = dept_service.listar_todos()
    
    if not departamentos:
        print("  No hay departamentos registrados")
        print("\n💡 Sugerencia: Cree departamentos primero desde el menú principal")
    else:
        for dept in departamentos:
            print(f"\n• {dept['nombre']}")
            print(f"  ID: {dept['id']}")
            print(f"  Descripción: {dept.get('descripcion', 'N/A')}")
    
    print("\n" + "="*60)


def main():
    print("\n🧪 VERIFICACIÓN DEL SISTEMA DE EMPLEADOS")
    print("="*60)
    
    # Verificar departamentos
    verificar_departamentos()
    
    # Verificar empleados
    verificar_empleados()
    
    # Verificar usuarios empleados
    verificar_usuarios_empleados()
    
    print("\n📝 FLUJO CORRECTO PARA CREAR EMPLEADO:")
    print("="*60)
    print("""
1. Ejecutar aplicación principal:
   python main.py

2. Login como admin:
   Usuario: admin
   Contraseña: admin123

3. Ir a: Menú de Empleados (opción 3 o 4 según su rol)

4. Seleccionar: Agregar (opción 1)

5. El sistema le pedirá:
   • Nombre completo del empleado
   • Email del empleado
   • Nombre de usuario (sugerido automáticamente del email)
   • Contraseña inicial para el empleado
   • Confirmar contraseña
   • Fecha inicio de contrato (YYYY-MM-DD)
   • Salario
   • Departamento (selección por número)

6. El sistema creará AUTOMÁTICAMENTE:
   ✓ Usuario con rol "Empleado" (nivel 3)
   ✓ Registro de empleado vinculado al usuario
   
7. El empleado podrá iniciar sesión con:
   Usuario: [el nombre de usuario creado]
   Contraseña: [la contraseña inicial]
   
8. El empleado tendrá acceso limitado:
   ✓ Ver Proyectos (solo lectura)
   ✓ Evaluar calidad del aire
   ✓ Cambiar su propia contraseña
   ✗ NO puede gestionar departamentos, proyectos, empleados, usuarios o roles

""")
    
    print("="*60)
    print("✅ VERIFICACIÓN COMPLETADA")
    print("="*60)


if __name__ == "__main__":
    main()
