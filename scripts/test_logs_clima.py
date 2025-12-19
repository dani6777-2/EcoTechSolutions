"""
Script de prueba para sistema de logs de clima
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aplicacion.services import ProyectoService
from dominio.models import LogClima
import uuid


def test_guardar_log():
    """Test: Guardar log de clima"""
    print("=" * 60)
    print("TEST: Guardar log de clima")
    print("=" * 60)
    
    service = ProyectoService()
    
    # Simular un log de clima
    log = LogClima(
        id=str(uuid.uuid4()),
        ciudad="Santiago",
        pais="CL",
        aqi=2,
        co=250.34,
        no2=15.46,
        o3=68.66,
        so2=0.64,
        pm2_5=8.16,
        pm10=9.43,
        nh3=0.52,
        latitud=-33.4489,
        longitud=-70.6693
    )
    
    try:
        service.log_clima_repo.crear(log)
        print("✓ Log guardado exitosamente")
    except Exception as e:
        print(f"✗ Error: {e}")


def test_listar_logs():
    """Test: Listar todos los logs"""
    print("\n" + "=" * 60)
    print("TEST: Listar logs de clima")
    print("=" * 60)
    
    service = ProyectoService()
    
    try:
        logs = service.listar_logs_clima(limit=10)
        print(f"\n✓ Se encontraron {len(logs)} logs:\n")
        
        for idx, log in enumerate(logs, 1):
            print(f"{idx}. {log.get('ciudad')}, {log.get('pais')} - AQI: {log.get('aqi')}/5")
            print(f"   Fecha: {log.get('fecha_consulta')}")
            print()
    except Exception as e:
        print(f"✗ Error: {e}")


def test_logs_por_ciudad():
    """Test: Listar logs por ciudad"""
    print("\n" + "=" * 60)
    print("TEST: Logs por ciudad")
    print("=" * 60)
    
    service = ProyectoService()
    
    try:
        logs = service.listar_logs_por_ciudad("Santiago", limit=10)
        print(f"\n✓ Se encontraron {len(logs)} logs para Santiago:\n")
        
        for idx, log in enumerate(logs, 1):
            print(f"{idx}. AQI: {log.get('aqi')}/5 - PM2.5: {log.get('pm2_5')} μg/m³")
            print(f"   Fecha: {log.get('fecha_consulta')}")
    except Exception as e:
        print(f"✗ Error: {e}")


def test_estadisticas_ciudad():
    """Test: Estadísticas por ciudad"""
    print("\n" + "=" * 60)
    print("TEST: Estadísticas de ciudad")
    print("=" * 60)
    
    service = ProyectoService()
    
    try:
        stats = service.obtener_estadisticas_ciudad("Santiago")
        if stats:
            print("\n✓ Estadísticas de Santiago:")
            print(f"   Total consultas: {stats.get('total_consultas')}")
            print(f"   AQI promedio: {stats.get('aqi_promedio', 0):.2f}/5")
            print(f"   AQI máximo: {stats.get('aqi_maximo')}/5")
            print(f"   AQI mínimo: {stats.get('aqi_minimo')}/5")
            print(f"   PM2.5 promedio: {stats.get('pm2_5_promedio', 0):.2f} μg/m³")
            print(f"   PM10 promedio: {stats.get('pm10_promedio', 0):.2f} μg/m³")
            print(f"   Última consulta: {stats.get('ultima_consulta')}")
        else:
            print("✗ No hay estadísticas disponibles")
    except Exception as e:
        print(f"✗ Error: {e}")


def test_ciudades_consultadas():
    """Test: Lista de ciudades consultadas"""
    print("\n" + "=" * 60)
    print("TEST: Ciudades consultadas")
    print("=" * 60)
    
    service = ProyectoService()
    
    try:
        ciudades = service.listar_ciudades_consultadas()
        print(f"\n✓ Ciudades consultadas ({len(ciudades)}):\n")
        
        for idx, ciudad in enumerate(ciudades, 1):
            print(f"{idx}. {ciudad.get('ciudad')}, {ciudad.get('pais')} - {ciudad.get('consultas')} consultas")
    except Exception as e:
        print(f"✗ Error: {e}")


def test_integracion_api():
    """Test: Integración completa con API (guarda log automáticamente)"""
    print("\n" + "=" * 60)
    print("TEST: Integración API + Guardado de Log")
    print("=" * 60)
    
    service = ProyectoService()
    
    try:
        # Esto debe consultar la API y guardar el log automáticamente
        datos = service.obtener_calidad_aire_por_ciudad(
            "Valparaiso", 
            "CL",
            usuario_id="test-user-id",
            guardar_log=True
        )
        
        if datos:
            print("✓ Consulta exitosa a la API")
            print(f"   Ciudad: Valparaíso, CL")
            print(f"   AQI: {datos.get('aqi')}/5")
            print(f"   PM2.5: {datos.get('pm2_5')} μg/m³")
            print("\n✓ Log guardado automáticamente en la base de datos")
        else:
            print("✗ No se pudo obtener datos de la API")
            print("   (Verifica API_KEY en .env)")
    except Exception as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    print("\n🌱 ECOTECH SOLUTIONS - TEST DE LOGS DE CLIMA\n")
    
    # Ejecutar tests
    test_guardar_log()
    test_listar_logs()
    test_logs_por_ciudad()
    test_estadisticas_ciudad()
    test_ciudades_consultadas()
    test_integracion_api()
    
    print("\n" + "=" * 60)
    print("TESTS COMPLETADOS")
    print("=" * 60 + "\n")
