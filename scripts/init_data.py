"""Script para inicializar datos de prueba: rol admin y usuario admin"""
from aplicacion.auth_services import RolService, UsuarioService
from dominio.auth_models import Rol, Usuario
import uuid

print("=== Inicializando datos de prueba ===\n")

# Crear servicios
rol_service = RolService()
usuario_service = UsuarioService()

# 1. Crear rol administrador
print("1. Creando rol Administrador...")
rol_admin = Rol(
    id=str(uuid.uuid4()),
    nombre="Administrador",
    descripcion="Acceso completo al sistema",
    nivel_permisos=10,
    activo=True
)
rol_service.crear_rol(rol_admin)

# 2. Listar roles para obtener el ID real
print("\n2. Obteniendo ID del rol creado...")
roles = rol_service.listar_roles()
rol_admin_data = next((r for r in roles if r['nombre'] == 'Administrador'), None)

if not rol_admin_data:
    print("❌ Error: No se pudo crear el rol administrador")
    exit(1)

print(f"✓ Rol creado con ID: {rol_admin_data['id']}")

# 3. Crear usuario administrador
print("\n3. Creando usuario admin...")
usuario_admin = Usuario(
    id=str(uuid.uuid4()),
    nombre_usuario="admin",
    contrasena_cifrada="",  # Se generará automáticamente
    salt="",  # Se generará automáticamente
    rol_id=rol_admin_data['id'],
    activo=True
)

# Contraseña por defecto: admin123
usuario_service.crear_usuario(usuario_admin, "admin123")

# 4. Crear rol empleado
print("\n4. Creando rol Empleado...")
rol_empleado = Rol(
    id=str(uuid.uuid4()),
    nombre="Empleado",
    descripcion="Acceso básico al sistema",
    nivel_permisos=3,
    activo=True
)
rol_service.crear_rol(rol_empleado)

# 5. Crear rol gerente
print("\n5. Creando rol Gerente...")
rol_gerente = Rol(
    id=str(uuid.uuid4()),
    nombre="Gerente",
    descripcion="Acceso a gestión de proyectos y departamentos",
    nivel_permisos=7,
    activo=True
)
rol_service.crear_rol(rol_gerente)

print("\n" + "="*60)
print("✓ Inicialización completada!")
print("="*60)
print("\nCredenciales de acceso:")
print("  Usuario: admin")
print("  Contraseña: admin123")
print("\nRoles creados:")
print("  • Administrador (nivel 10)")
print("  • Gerente (nivel 7)")
print("  • Empleado (nivel 3)")
print("\n⚠️  IMPORTANTE: Cambiar la contraseña del admin después del primer login")
print("="*60)
