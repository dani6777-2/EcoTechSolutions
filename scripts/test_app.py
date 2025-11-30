"""Script de prueba rápida de la aplicación"""
from aplicacion.services import DepartamentoService, ProyectoService, EmpleadoService
from dominio.models import Departamento, Proyecto
import uuid

print("=== Prueba de Aplicación EcoTech ===\n")

# Test Departamentos
print("1. Creando departamento de prueba...")
dept_service = DepartamentoService()
dept = Departamento(
    id=str(uuid.uuid4()),
    nombre="Tecnología",
    descripcion="Departamento de TI"
)
dept_service.crear(dept)

print("\n2. Listando departamentos:")
for d in dept_service.listar_todos():
    print(f"   {d}")

print("\n3. Buscando por nombre 'Tecno':")
for d in dept_service.buscar_por_nombre("Tecno"):
    print(f"   {d}")

# Test Proyectos
print("\n4. Creando proyecto de prueba...")
proj_service = ProyectoService()
proj = Proyecto(
    id=str(uuid.uuid4()),
    nombre="Sistema ERP",
    descripcion="Implementación de ERP",
    fecha_inicio="2025-01-01",
    fecha_fin="2025-12-31"
)
proj_service.crear(proj)

print("\n5. Listando proyectos:")
for p in proj_service.listar_todos():
    print(f"   {p}")

print("\n✓ Todas las pruebas completadas exitosamente!")
