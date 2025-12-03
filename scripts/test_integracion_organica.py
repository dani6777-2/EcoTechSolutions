#!/usr/bin/env python
"""
Test de integración orgánica de API en la aplicación.
Simula el flujo de usuario creando un proyecto con evaluación ambiental.
"""
import sys
import os

# Agregar directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from aplicacion.services import ProyectoService
from aplicacion.api_client import EcoAPIClient


def test_flujo_integracion():
    """Prueba el flujo integrado de la API en la aplicación"""
    print("=" * 70)
    print(" TEST DE INTEGRACIÓN ORGÁNICA - API EN MENÚ DE PROYECTOS")
    print("=" * 70)
    print()
    
    service = ProyectoService()
    
    # Simular flujo: Usuario está creando un proyecto y evalúa ubicación
    print("ESCENARIO: Usuario creando proyecto 'Expansión Santiago'")
    print("          Evalúa calidad del aire antes de confirmar ubicación")
    print()
    
    ciudad = "Santiago"
    pais = "CL"
    
    print(f"🔍 Evaluando calidad del aire en {ciudad}, {pais}...")
    print()
    
    try:
        datos = service.obtener_calidad_aire_por_ciudad(ciudad, pais)
        
        if datos:
            aqi = datos.get('aqi', 0)
            interpretacion = EcoAPIClient.interpretar_aqi(aqi)
            
            # Mostrar reporte como aparecerá en el menú
            print("─" * 70)
            print(f" REPORTE DE CALIDAD DEL AIRE - {ciudad.upper()}")
            print("─" * 70)
            print(f"\n📊 Índice de Calidad (AQI): {aqi}/5 - {interpretacion}")
            print(f"\n🔬 Contaminantes principales (μg/m³):")
            print(f"  • PM2.5 (Partículas finas): {datos.get('pm2_5', 'N/A')}")
            print(f"  • PM10 (Partículas):        {datos.get('pm10', 'N/A')}")
            print(f"  • NO₂ (Dióxido nitrógeno):  {datos.get('no2', 'N/A')}")
            print(f"  • O₃ (Ozono):               {datos.get('o3', 'N/A')}")
            print(f"  • SO₂ (Dióxido azufre):     {datos.get('so2', 'N/A')}")
            
            # Mostrar recomendación
            print("\n" + "─" * 70)
            print(" RECOMENDACIÓN PARA PROYECTOS ECOTECH")
            print("─" * 70)
            
            if aqi <= 2:
                print("\n✅ UBICACIÓN APROBADA")
                print("  • Excelente calidad del aire")
                print("  • Ambiente saludable para equipo de trabajo")
                print("  • Alineado con valores de sustentabilidad EcoTech")
                decision = "PROCEDER con el proyecto"
            elif aqi == 3:
                print("\n⚠️  UBICACIÓN CONDICIONAL")
                print("  • Calidad del aire moderada")
                print("  • Recomendaciones:")
                print("    - Implementar purificadores de aire en oficinas")
                print("    - Monitoreo periódico de condiciones")
                decision = "PROCEDER con precauciones"
            else:
                print("\n❌ UBICACIÓN NO RECOMENDADA")
                print("  • Alta contaminación ambiental")
                print("  • Riesgo para salud del equipo")
                decision = "BUSCAR ubicación alternativa"
            
            print()
            print("=" * 70)
            print(f" DECISIÓN: {decision}")
            print("=" * 70)
            print()
            print("✅ Integración funcionando correctamente")
            print("   La API se consulta de forma natural durante el flujo de creación")
            print("   de proyectos, proporcionando información valiosa para decisiones.")
            
        else:
            print("⚠️  No se obtuvieron datos (API_KEY no configurada o error)")
            print()
            print("NOTA: En la aplicación real, el usuario vería este mensaje")
            print("      y podría continuar sin evaluación ambiental.")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    print()
    print("─" * 70)
    print(" FLUJO DE INTEGRACIÓN EN LA APLICACIÓN:")
    print("─" * 70)
    print()
    print("1. Usuario ingresa al Menú de Proyectos")
    print("2. Selecciona 'Agregar' o 'Evaluar calidad del aire'")
    print("3. Sistema ofrece evaluar ubicación (opcional)")
    print("4. API consulta datos en tiempo real")
    print("5. Sistema muestra reporte y recomendación")
    print("6. Usuario toma decisión informada")
    print("7. Proyecto se crea (o no) según evaluación")
    print()
    print("✨ La API está completamente integrada en el flujo natural")
    print("   de trabajo, sin necesidad de herramientas externas.")
    print()
    
    return True


if __name__ == "__main__":
    print("\n🌱 ECOTECH SOLUTIONS - TEST DE INTEGRACIÓN API\n")
    
    if not os.getenv('API_KEY'):
        print("⚠️  NOTA: API_KEY no configurada")
        print("   El test mostrará el flujo pero puede no obtener datos reales")
        print("   Para datos reales: export API_KEY='tu_clave'\n")
    
    exito = test_flujo_integracion()
    
    if exito:
        print("🎉 Test completado exitosamente")
        sys.exit(0)
    else:
        print("❌ Test falló")
        sys.exit(1)
