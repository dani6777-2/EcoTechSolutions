"""Test del sistema de autenticación"""
from aplicacion.auth_services import AuthService

print("=== Test de Autenticación ===\n")

auth_service = AuthService()

# Test 1: Login exitoso
print("Test 1: Login con credenciales correctas")
usuario = auth_service.autenticar("admin", "admin123")
if usuario:
    print(f"  Usuario ID: {usuario['id']}")
    print(f"  Rol ID: {usuario['rol_id']}")
    print(f"  Activo: {usuario['activo']}")

# Test 2: Login con contraseña incorrecta
print("\nTest 2: Login con contraseña incorrecta")
usuario = auth_service.autenticar("admin", "wrongpassword")

# Test 3: Login con usuario inexistente
print("\nTest 3: Login con usuario inexistente")
usuario = auth_service.autenticar("noexiste", "password")

print("\n✓ Tests completados")
