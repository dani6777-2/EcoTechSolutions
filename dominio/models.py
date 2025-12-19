class Departamento:
    def __init__(self, id: str, nombre: str, descripcion: str = None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not value or len(value) < 2:
            raise ValueError("El nombre del departamento es obligatorio y debe tener al menos 2 caracteres")
        self._nombre = value

    def __repr__(self):
        return f"Departamento(id={self.id}, nombre={self.nombre})"


class Proyecto:
    def __init__(self, id: str, nombre: str, descripcion: str = None, fecha_inicio: str = None, fecha_fin: str = None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not value or len(value) < 2:
            raise ValueError("El nombre del proyecto es obligatorio y debe tener al menos 2 caracteres")
        self._nombre = value

    def __repr__(self):
        return f"Proyecto(id={self.id}, nombre={self.nombre})"


class Empleado:
    def __init__(self, id: str, usuario_id: str, nombre: str, email: str, fecha_inicio_contrato: str, salario=None, departamento_id: str = None):
        self.id = id
        self.usuario_id = usuario_id
        self.nombre = nombre
        self.email = email
        self.fecha_inicio_contrato = fecha_inicio_contrato
        self.salario = salario
        self.departamento_id = departamento_id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not value or len(value) < 2:
            raise ValueError("El nombre del empleado es obligatorio y debe tener al menos 2 caracteres")
        self._nombre = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not value or "@" not in value:
            raise ValueError("Email inválido")
        self._email = value

    def __repr__(self):
        return f"Empleado(id={self.id}, nombre={self.nombre}, email={self.email})"


class LogClima:
    """Modelo de dominio para registrar consultas de calidad del aire"""
    
    def __init__(self, id: str, ciudad: str, pais: str, aqi: int, 
                 co: float = None, no2: float = None, o3: float = None, 
                 so2: float = None, pm2_5: float = None, pm10: float = None, 
                 nh3: float = None, usuario_id: str = None, proyecto_id: str = None,
                 latitud: float = None, longitud: float = None):
        self.id = id
        self.ciudad = ciudad
        self.pais = pais
        self.aqi = aqi
        self.co = co
        self.no2 = no2
        self.o3 = o3
        self.so2 = so2
        self.pm2_5 = pm2_5
        self.pm10 = pm10
        self.nh3 = nh3
        self.usuario_id = usuario_id
        self.proyecto_id = proyecto_id
        self.latitud = latitud
        self.longitud = longitud
    
    @property
    def ciudad(self):
        return self._ciudad
    
    @ciudad.setter
    def ciudad(self, value):
        if not value or len(value) < 2:
            raise ValueError("El nombre de la ciudad debe tener al menos 2 caracteres")
        self._ciudad = value
    
    @property
    def aqi(self):
        return self._aqi
    
    @aqi.setter
    def aqi(self, value):
        if not isinstance(value, int) or value < 1 or value > 5:
            raise ValueError("El AQI debe ser un entero entre 1 y 5")
        self._aqi = value
    
    def __repr__(self):
        return f"LogClima(ciudad={self.ciudad}, pais={self.pais}, aqi={self.aqi})"
