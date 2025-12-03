"""
Script de prueba para la integración con API de datos ambientales.
Demuestra el uso de EcoAPIClient para obtener calidad del aire.
"""
import os
import sys

# Agregar el directorio raíz al path para importar módulos
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from aplicacion.api_client import EcoAPIClient
from aplicacion.services import ProyectoService


def test_api_directa():
    """Prueba directa del cliente API"""
    print("=" * 60)
    print("TEST 1: Cliente API Directo")
    print("=" * 60)
    
    try:
        client = EcoAPIClient()
        print("✓ Cliente API inicializado correctamente\n")
        
        # Test 1: Obtener coordenadas
        print("📍 Obteniendo coordenadas de Santiago, Chile...")
        coords = client.obtener_coordenadas_ciudad('Santiago', 'CL')
        
        if coords:
            print(f"✓ Coordenadas encontradas: Lat {coords['lat']}, Lon {coords['lon']}\n")
            
            # Test 2: Obtener calidad del aire
            print("🌍 Consultando calidad del aire...")
            datos = client.obtener_calidad_aire(coords['lat'], coords['lon'])
            
            if datos:
                print(EcoAPIClient.formato_reporte_calidad_aire(datos))
            else:
                print("❌ No se pudieron obtener datos de calidad del aire")
        else:
            print("❌ No se encontraron coordenadas para la ciudad")
            
    except ValueError as e:
        print(f"\n❌ Error de configuración: {e}")
        print("\n💡 Solución:")
        print("   1. Regístrate en https://openweathermap.org/api")
        print("   2. Obtén tu API key gratuita")
        print("   3. Configura la variable de entorno:")
        print("      export API_KEY='tu_api_key_aqui'")
        print("   4. O agrégala al archivo .env del proyecto")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False
    
    return True


def test_servicio_integrado():
    """Prueba a través del servicio de proyectos"""
    print("\n" + "=" * 60)
    print("TEST 2: Servicio Integrado (ProyectoService)")
    print("=" * 60 + "\n")
    
    try:
        service = ProyectoService()
        
        ciudades = [
            ('Santiago', 'CL'),
            ('Valparaíso', 'CL'),
            ('Concepción', 'CL')
        ]
        
        for ciudad, pais in ciudades:
            print(f"🏙️  Consultando calidad del aire en {ciudad}...")
            datos = service.obtener_calidad_aire_por_ciudad(ciudad, pais)
            
            if datos:
                aqi = datos.get('aqi')
                interpretacion = EcoAPIClient.interpretar_aqi(aqi)
                print(f"   ✓ AQI: {aqi}/5 - {interpretacion}")
                print(f"   • PM2.5: {datos.get('pm2_5')} μg/m³")
                print(f"   • PM10: {datos.get('pm10')} μg/m³")
            else:
                print(f"   ⚠️  No se pudieron obtener datos para {ciudad}")
            print()
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    return True


def test_caso_uso_proyecto():
    """Simula caso de uso: evaluar calidad del aire antes de asignar proyecto"""
    print("=" * 60)
    print("TEST 3: Caso de Uso - Evaluación de Ubicación de Proyecto")
    print("=" * 60 + "\n")
    
    print("Escenario: EcoTech Solutions planea abrir oficina en nueva ciudad")
    print("Necesita evaluar calidad del aire antes de tomar decisión\n")
    
    try:
        service = ProyectoService()
        ciudad_candidata = "Santiago"
        
        print(f"🔍 Evaluando ubicación candidata: {ciudad_candidata}")
        datos = service.obtener_calidad_aire_por_ciudad(ciudad_candidata, 'CL')
        
        if datos:
            aqi = datos.get('aqi')
            print(EcoAPIClient.formato_reporte_calidad_aire(datos))
            
            # Decisión basada en AQI
            if aqi <= 2:
                print("✅ RECOMENDACIÓN: Ubicación APROBADA")
                print("   Calidad del aire es buena para establecer operaciones")
            elif aqi <= 3:
                print("⚠️  RECOMENDACIÓN: Ubicación CONDICIONAL")
                print("   Considerar medidas de purificación de aire en oficinas")
            else:
                print("❌ RECOMENDACIÓN: Ubicación NO RECOMENDADA")
                print("   Buscar ubicación alternativa con mejor calidad de aire")
        else:
            print("❌ No se pudo evaluar la ubicación")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    return True


if __name__ == "__main__":
    print("\n🌱 ECOTECH SOLUTIONS - TEST DE API AMBIENTAL 🌱\n")
    
    # Verificar configuración
    if not os.getenv('API_KEY'):
        print("⚠️  ADVERTENCIA: Variable API_KEY no configurada")
        print("   Los tests pueden fallar sin la clave de API\n")
        print("Configuración rápida:")
        print("  export API_KEY='tu_clave_de_openweathermap'\n")
        
        respuesta = input("¿Deseas continuar de todos modos? (s/n): ").lower()
        if respuesta != 's':
            print("Tests cancelados.")
            sys.exit(0)
        print()
    
    # Ejecutar tests
    resultados = []
    
    resultados.append(("Cliente API Directo", test_api_directa()))
    resultados.append(("Servicio Integrado", test_servicio_integrado()))
    resultados.append(("Caso de Uso Proyecto", test_caso_uso_proyecto()))
    
    # Reporte final
    print("\n" + "=" * 60)
    print("RESUMEN DE TESTS")
    print("=" * 60)
    
    for nombre, resultado in resultados:
        estado = "✅ PASÓ" if resultado else "❌ FALLÓ"
        print(f"{estado} - {nombre}")
    
    total = len(resultados)
    exitosos = sum(1 for _, r in resultados if r)
    
    print(f"\nTotal: {exitosos}/{total} tests exitosos")
    
    if exitosos == total:
        print("\n🎉 ¡Todos los tests pasaron correctamente!")
        sys.exit(0)
    else:
        print("\n⚠️  Algunos tests fallaron. Revisa la configuración.")
        sys.exit(1)
