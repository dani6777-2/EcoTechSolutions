"""
Cliente para APIs públicas relacionadas con datos ambientales.
Integrado para enriquecer proyectos con información ecológica.
"""
import os
import requests
from typing import Optional, Dict, Any


class EcoAPIClient:
    """
    Cliente para consumir APIs públicas de datos ambientales.
    Por defecto usa OpenWeatherMap Air Pollution API (gratuita).
    """
    
    BASE_URL = "http://api.openweathermap.org/data/2.5"
    
    def __init__(self, api_key: Optional[str] = None, timeout: int = 10):
        """
        Inicializa el cliente de API.
        
        Args:
            api_key: Clave de API de OpenWeatherMap. Si no se provee, busca en variable de entorno API_KEY
            timeout: Timeout en segundos para las peticiones HTTP
        """
        self.api_key = api_key or os.getenv("API_KEY")
        self.timeout = timeout
        
        if not self.api_key:
            raise ValueError(
                "API_KEY no configurada. Debe proporcionar api_key o definir variable de entorno API_KEY"
            )
    
    def obtener_calidad_aire(self, lat: float, lon: float) -> Optional[Dict[str, Any]]:
        """
        Obtiene la calidad del aire para una ubicación específica.
        
        Args:
            lat: Latitud de la ubicación
            lon: Longitud de la ubicación
            
        Returns:
            Diccionario con información de calidad del aire o None si hay error
            
        Ejemplo de respuesta:
            {
                'aqi': 2,  # Índice de calidad del aire (1=Bueno, 2=Aceptable, 3=Moderado, 4=Pobre, 5=Muy pobre)
                'co': 250.34,
                'no': 0.01,
                'no2': 15.46,
                'o3': 68.66,
                'so2': 0.64,
                'pm2_5': 8.16,
                'pm10': 9.43,
                'nh3': 0.52
            }
        """
        try:
            url = f"{self.BASE_URL}/air_pollution"
            params = {
                'lat': lat,
                'lon': lon,
                'appid': self.api_key
            }
            
            response = requests.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            
            data = response.json()
            
            # Parsear la respuesta
            if 'list' in data and len(data['list']) > 0:
                componentes = data['list'][0]['components']
                aqi = data['list'][0]['main']['aqi']
                
                return {
                    'aqi': aqi,
                    'co': componentes.get('co'),
                    'no': componentes.get('no'),
                    'no2': componentes.get('no2'),
                    'o3': componentes.get('o3'),
                    'so2': componentes.get('so2'),
                    'pm2_5': componentes.get('pm2_5'),
                    'pm10': componentes.get('pm10'),
                    'nh3': componentes.get('nh3')
                }
            
            return None
            
        except requests.exceptions.Timeout:
            print(f"Error: Timeout al consultar API (>{self.timeout}s)")
            return None
        except requests.exceptions.ConnectionError:
            print("Error: No se pudo conectar a la API. Verifique su conexión a internet.")
            return None
        except requests.exceptions.HTTPError as e:
            print(f"Error HTTP {e.response.status_code}: {e.response.text}")
            return None
        except Exception as e:
            print(f"Error inesperado al consultar API: {str(e)}")
            return None
    
    def obtener_coordenadas_ciudad(self, ciudad: str, pais: str = "CL") -> Optional[Dict[str, float]]:
        """
        Obtiene las coordenadas geográficas de una ciudad usando Geocoding API.
        
        Args:
            ciudad: Nombre de la ciudad
            pais: Código de país ISO 3166 (por defecto CL para Chile)
            
        Returns:
            Diccionario con 'lat' y 'lon' o None si no se encuentra
        """
        try:
            url = f"{self.BASE_URL.replace('data/2.5', 'geo/1.0')}/direct"
            params = {
                'q': f"{ciudad},{pais}",
                'limit': 1,
                'appid': self.api_key
            }
            
            response = requests.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            
            data = response.json()
            
            if data and len(data) > 0:
                return {
                    'lat': data[0]['lat'],
                    'lon': data[0]['lon']
                }
            
            print(f"No se encontraron coordenadas para '{ciudad}, {pais}'")
            return None
            
        except Exception as e:
            print(f"Error al obtener coordenadas: {str(e)}")
            return None
    
    def obtener_calidad_aire_ciudad(self, ciudad: str, pais: str = "CL") -> Optional[Dict[str, Any]]:
        """
        Obtiene la calidad del aire para una ciudad (combina geocoding + air pollution).
        
        Args:
            ciudad: Nombre de la ciudad
            pais: Código de país ISO 3166
            
        Returns:
            Diccionario con información de calidad del aire o None si hay error
        """
        coords = self.obtener_coordenadas_ciudad(ciudad, pais)
        
        if not coords:
            return None
        
        return self.obtener_calidad_aire(coords['lat'], coords['lon'])
    
    @staticmethod
    def interpretar_aqi(aqi: int) -> str:
        """
        Interpreta el índice de calidad del aire (AQI).
        
        Args:
            aqi: Índice de calidad del aire (1-5)
            
        Returns:
            Descripción textual del índice
        """
        interpretaciones = {
            1: "Bueno",
            2: "Aceptable",
            3: "Moderado",
            4: "Pobre",
            5: "Muy Pobre"
        }
        return interpretaciones.get(aqi, "Desconocido")
    
    @staticmethod
    def formato_reporte_calidad_aire(datos: Dict[str, Any]) -> str:
        """
        Formatea los datos de calidad del aire en un reporte legible.
        
        Args:
            datos: Diccionario con datos de calidad del aire
            
        Returns:
            String con reporte formateado
        """
        if not datos:
            return "No hay datos disponibles"
        
        aqi = datos.get('aqi', 0)
        interpretacion = EcoAPIClient.interpretar_aqi(aqi)
        
        reporte = f"""
╔═══════════════════════════════════════╗
║   REPORTE DE CALIDAD DEL AIRE         ║
╚═══════════════════════════════════════╝

Índice de Calidad (AQI): {aqi}/5 - {interpretacion}

Contaminantes (μg/m³):
  • CO (Monóxido de carbono):  {datos.get('co', 'N/A')}
  • NO₂ (Dióxido de nitrógeno): {datos.get('no2', 'N/A')}
  • O₃ (Ozono):                 {datos.get('o3', 'N/A')}
  • SO₂ (Dióxido de azufre):    {datos.get('so2', 'N/A')}
  • PM2.5 (Partículas finas):   {datos.get('pm2_5', 'N/A')}
  • PM10 (Partículas):          {datos.get('pm10', 'N/A')}
  • NH₃ (Amoníaco):             {datos.get('nh3', 'N/A')}

{"⚠️  Precaución recomendada" if aqi >= 4 else "✓ Condiciones aceptables"}
"""
        return reporte
