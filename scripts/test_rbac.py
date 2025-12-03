#!/usr/bin/env python3
"""
Script de prueba para verificar el control de acceso basado en roles (RBAC)
"""
import os
import sys

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aplicacion.auth_services import AuthService, UsuarioService, RolService
from dominio.auth_models import Usuario, Rol
import uuid


def crear_usuarios_prueba():
    """Crea usuarios de prueba con diferentes roles"""
    usuario_service = UsuarioService()
    rol_service = RolService()
    
    # Obtener roles existentes
    roles = rol_service.listar_roles()
    
    if len(roles) < 3:
        print("❌ Se necesitan al menos 3 roles (Admin, Gerente, Empleado)")
        print("Ejecute primero: python scripts/init_data.py")
        return False
    
    # Buscar roles por nivel de permisos
    rol_admin = next((r for r in roles if r['nivel_permisos'] == 10), None)
    rol_gerente = next((r for r in roles if r['nivel_permisos'] == 7), None)
    rol_empleado = next((r for r in roles if r['nivel_permisos'] == 3), None)
    
    if not all([rol_admin, rol_gerente, rol_empleado]):
        print("❌ No se encontraron todos los roles necesarios")
        return False
    
    print("\n🔧 Creando usuarios de prueba...")
    print("="*60)
    
    # Crear empleado de prueba
    try:
        empleado = Usuario(
            id=str(uuid.uuid4()),
            nombre_usuario="empleado_test",
            contrasena_cifrada="",
            salt="",
            rol_id=rol_empleado['id'],
            activo=True
        )
        usuario_service.crear_usuario(empleado, "empleado123")
        print("✓ Usuario 'empleado_test' creado (Empleado - Nivel 3)")
    except Exception as e:
        if "duplicate" in str(e).lower() or "already exists" in str(e).lower():
            print("⚠️  Usuario 'empleado_test' ya existe")
        else:
            print(f"❌ Error creando empleado_test: {e}")
    
    # Crear gerente de prueba
    try:
        gerente = Usuario(
            id=str(uuid.uuid4()),
            nombre_usuario="gerente_test",
            contrasena_cifrada="",
            salt="",
            rol_id=rol_gerente['id'],
            activo=True
        )
        usuario_service.crear_usuario(gerente, "gerente123")
        print("✓ Usuario 'gerente_test' creado (Gerente - Nivel 7)")
    except Exception as e:
        if "duplicate" in str(e).lower() or "already exists" in str(e).lower():
            print("⚠️  Usuario 'gerente_test' ya existe")
        else:
            print(f"❌ Error creando gerente_test: {e}")
    
    print("\n✅ Usuarios de prueba disponibles:")
    print("  • admin (Administrador) - Contraseña: admin123")
    print("  • gerente_test (Gerente) - Contraseña: gerente123")
    print("  • empleado_test (Empleado) - Contraseña: empleado123")
    print("="*60)
    
    return True


def probar_autenticacion_roles():
    """Prueba la autenticación con diferentes roles"""
    auth_service = AuthService()
    
    print("\n🔐 Probando autenticación con diferentes roles...")
    print("="*60)
    
    usuarios_prueba = [
        ("admin", "admin123", 10, "Administrador"),
        ("gerente_test", "gerente123", 7, "Gerente"),
        ("empleado_test", "empleado123", 3, "Empleado")
    ]
    
    for nombre_usuario, contrasena, nivel_esperado, rol_esperado in usuarios_prueba:
        print(f"\n🔍 Autenticando como '{nombre_usuario}'...")
        
        usuario_data = auth_service.autenticar(nombre_usuario, contrasena)
        
        if usuario_data:
            nivel_real = usuario_data.get('nivel_permisos', 0)
            rol_real = usuario_data.get('nombre_rol', 'Desconocido')
            
            print(f"  ✓ Nombre: {usuario_data['nombre_usuario']}")
            print(f"  ✓ Rol: {rol_real}")
            print(f"  ✓ Nivel de permisos: {nivel_real}")
            
            # Verificar que el nivel sea el esperado
            if nivel_real == nivel_esperado and rol_real == rol_esperado:
                print(f"  ✅ CORRECTO: Nivel y rol coinciden")
            else:
                print(f"  ❌ ERROR: Se esperaba nivel {nivel_esperado} ({rol_esperado}), obtuvo {nivel_real} ({rol_real})")
        else:
            print(f"  ❌ FALLO: No se pudo autenticar")
    
    print("\n" + "="*60)


def mostrar_matriz_permisos():
    """Muestra la matriz de permisos por rol"""
    print("\n📋 MATRIZ DE PERMISOS POR ROL")
    print("="*60)
    
    permisos = {
        "Empleado (Nivel 3)": [
            "✓ Ver Proyectos (solo lectura)",
            "✓ Evaluar calidad del aire",
            "✓ Cambiar su propia contraseña",
            "✗ Gestionar Departamentos",
            "✗ Gestionar Proyectos (crear/editar/eliminar)",
            "✗ Gestionar Empleados",
            "✗ Gestión de Usuarios",
            "✗ Gestión de Roles"
        ],
        "Gerente (Nivel 7)": [
            "✓ Ver Proyectos (completo)",
            "✓ Gestionar Departamentos",
            "✓ Gestionar Proyectos (crear/editar/eliminar)",
            "✓ Gestionar Empleados",
            "✓ Evaluar calidad del aire",
            "✓ Cambiar su propia contraseña",
            "✗ Gestión de Usuarios",
            "✗ Gestión de Roles"
        ],
        "Administrador (Nivel 10)": [
            "✓ Ver Proyectos (completo)",
            "✓ Gestionar Departamentos",
            "✓ Gestionar Proyectos",
            "✓ Gestionar Empleados",
            "✓ Gestión de Usuarios",
            "✓ Gestión de Roles",
            "✓ Evaluar calidad del aire",
            "✓ Cambiar su propia contraseña"
        ]
    }
    
    for rol, perms in permisos.items():
        print(f"\n{rol}:")
        for p in perms:
            print(f"  {p}")
    
    print("\n" + "="*60)


def main():
    print("\n🧪 PRUEBA DE CONTROL DE ACCESO BASADO EN ROLES (RBAC)")
    print("="*60)
    
    # Crear usuarios de prueba
    if not crear_usuarios_prueba():
        return
    
    # Probar autenticación
    probar_autenticacion_roles()
    
    # Mostrar matriz de permisos
    mostrar_matriz_permisos()
    
    print("\n📝 INSTRUCCIONES DE PRUEBA MANUAL:")
    print("="*60)
    print("\n1. Ejecute la aplicación principal:")
    print("   python main.py")
    print("\n2. Inicie sesión con cada usuario:")
    print("   • empleado_test / empleado123")
    print("   • gerente_test / gerente123")
    print("   • admin / admin123")
    print("\n3. Verifique que cada usuario:")
    print("   • Solo vea las opciones de menú permitidas para su rol")
    print("   • Reciba error al intentar acceder a opciones restringidas")
    print("   • Tenga el nivel de acceso correcto según la matriz mostrada")
    print("\n✅ PRUEBAS AUTOMATIZADAS COMPLETADAS")
    print("="*60)


if __name__ == "__main__":
    main()
