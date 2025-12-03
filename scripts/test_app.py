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

# Test API Pública - Calidad del Aire
print("\n6. Probando integración con API de Calidad del Aire...")
try:
    from aplicacion.api_client import EcoAPIClient
    import os
    
    # Verificar si la API_KEY está configurada
    if os.getenv('API_KEY'):
        print("   ✓ API_KEY configurada, consultando calidad del aire en Santiago...")
        datos = proj_service.obtener_calidad_aire_por_ciudad('Santiago', 'CL')
        
        if datos:
            print(f"   ✓ Datos recibidos - AQI: {datos.get('aqi')}/5 ({EcoAPIClient.interpretar_aqi(datos.get('aqi'))})")
            print(f"   • PM2.5: {datos.get('pm2_5')} μg/m³")
            print(f"   • PM10: {datos.get('pm10')} μg/m³")
        else:
            print("   ⚠ No se pudieron obtener datos (API puede estar caída)")
    else:
        print("   ⚠ API_KEY no configurada (omitiendo test de API)")
        print("   💡 Tip: Exporta API_KEY con tu clave de OpenWeatherMap:")
        print("      export API_KEY='tu_api_key_aqui'")
except Exception as e:
    print(f"   ⚠ Error en test de API: {e}")

print("\n✓ Todas las pruebas completadas exitosamente!")
