# Guía de Desarrollo - EcoTech Management

## 🎯 Inicio Rápido para Desarrolladores

### Primera vez

```bash
# Clonar y configurar
git clone <repo>
cd EcoTechSolutions

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Levantar base de datos
docker-compose up -d

# Esperar a que MySQL esté listo
sleep 15

# Verificar conexión
python test_db.py

# Ejecutar aplicación
python main.py
```

### Desarrollo diario

```bash
# Activar entorno
source venv/bin/activate

# Asegurar MySQL corriendo
docker-compose up -d

# Desarrollar...
python main.py
```

## 🏗️ Agregar Nueva Funcionalidad

### Ejemplo: Agregar gestión de Clientes

**1. Modelo de Dominio** (`dominio/models.py`)

```python
class Cliente:
    def __init__(self, id: str, nombre: str, email: str, telefono: str = None):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not value or len(value) < 2:
            raise ValueError("Nombre debe tener al menos 2 caracteres")
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
        return f"Cliente(id={self.id}, nombre={self.nombre}, email={self.email})"
```

**2. Repositorio** (`persistencia/repositorios.py`)

```python
class ClienteRepo:
    def crear(self, cliente):
        sql = "INSERT INTO clientes (id, nombre, email, telefono) VALUES (%s, %s, %s, %s)"
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (cliente.id, cliente.nombre, cliente.email, cliente.telefono))
            conn.commit()
        finally:
            conn.close()

    def listar_todos(self):
        sql = "SELECT * FROM clientes"
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
        finally:
            conn.close()

    # ... más métodos CRUD
```

**3. Servicio** (`aplicacion/services.py`)

```python
class ClienteService:
    def __init__(self):
        self.repo = ClienteRepo()

    def crear(self, cliente):
        try:
            self.repo.crear(cliente)
            print("Cliente creado")
        except Exception as e:
            print("Error creando cliente:", e)

    def listar_todos(self):
        return self.repo.listar_todos()

    # ... más métodos
```

**4. Menú** (`presentacion/menus.py`)

```python
class ClientesMenu(MenuBase):
    def mostrar(self):
        print("\n-- Menú Clientes --")
        print("1. Agregar")
        print("2. Mostrar Todos")
        # ... más opciones

    def ejecutar(self):
        while True:
            self.mostrar()
            opcion = self.limpiar_input("Opción: ")
            if opcion == '1':
                # Lógica de agregar
                pass
            # ... más opciones
```

**5. Integrar en Main** (`main.py`)

```python
from aplicacion.services import ClienteService

def main():
    # ... servicios existentes
    servicio_clientes = ClienteService()
    
    menu = MainMenu(
        servicio_dept, 
        servicio_proj, 
        servicio_emp,
        servicio_clientes  # ← Agregar
    )
```

**6. Migración de BD**

```bash
# Opción A: SQL directo
docker exec -it ecotech_mysql mysql -u ecotech_user -pecotech_pass ecotech_management -e "
CREATE TABLE clientes (
    id VARCHAR(50) PRIMARY KEY,
    nombre VARCHAR(200) NOT NULL,
    email VARCHAR(150) NOT NULL,
    telefono VARCHAR(20)
);"

# Opción B: Migración con Alembic
# 1. Agregar modelo a models_sqlalchemy.py
# 2. alembic revision --autogenerate -m "Agregar tabla clientes"
# 3. alembic upgrade head
```

## 🗄️ Trabajar con Migraciones

### Modificar Esquema de Tabla Existente

```bash
# 1. Modificar modelo en persistencia/models_sqlalchemy.py
# Ejemplo: agregar campo 'presupuesto' a Departamento

# 2. Generar migración
alembic revision --autogenerate -m "Agregar presupuesto a departamentos"

# 3. Revisar migración generada en alembic/versions/

# 4. Aplicar
alembic upgrade head

# 5. Verificar
python -c "from persistencia.db import Database; conn = Database.get_connection(); cur = conn.cursor(); cur.execute('DESC departamentos'); print(cur.fetchall())"
```

### Revertir Cambios

```bash
# Ver historial
alembic history

# Revertir última migración
alembic downgrade -1

# Revertir a versión específica
alembic downgrade <revision>

# Revertir todo
alembic downgrade base
```

## 🧪 Testing

### Test Unitario de Modelo

```python
# tests/test_models.py
import pytest
from dominio.models import Departamento

def test_departamento_valido():
    dept = Departamento(id="123", nombre="TI", descripcion="Tech")
    assert dept.nombre == "TI"

def test_departamento_nombre_invalido():
    with pytest.raises(ValueError):
        dept = Departamento(id="123", nombre="", descripcion="Tech")
```

### Test de Integración

```python
# tests/test_integration.py
from aplicacion.services import DepartamentoService
from dominio.models import Departamento
import uuid

def test_crear_y_listar_departamento():
    service = DepartamentoService()
    dept_id = str(uuid.uuid4())
    dept = Departamento(id=dept_id, nombre="Test Dept", descripcion="Test")
    
    service.crear(dept)
    departamentos = service.listar_todos()
    
    assert any(d['id'] == dept_id for d in departamentos)
```

## 🐛 Debugging

### Logs de MySQL

```bash
# Tiempo real
docker-compose logs -f mysql

# Últimas 50 líneas
docker-compose logs --tail=50 mysql
```

### Ejecutar Queries Directo

```bash
# Desde terminal
docker exec -it ecotech_mysql mysql -u ecotech_user -pecotech_pass ecotech_management

# Luego dentro de MySQL
mysql> SHOW TABLES;
mysql> SELECT * FROM departamentos;
mysql> DESC empleados;
```

### Python Interactive

```bash
source venv/bin/activate
python

>>> from persistencia.db import Database
>>> conn = Database.get_connection()
>>> cur = conn.cursor()
>>> cur.execute("SELECT * FROM departamentos")
>>> print(cur.fetchall())
```

## 📝 Convenciones de Código

### Naming

- **Clases**: PascalCase (`DepartamentoService`)
- **Funciones/métodos**: snake_case (`listar_todos`)
- **Constantes**: UPPER_SNAKE_CASE (`DB_HOST`)
- **Privados**: prefijo `_` (`_nombre`)

### Estructura de Archivos

```
modulo/
├── __init__.py      # Exportaciones públicas
├── models.py        # Modelos de datos
├── services.py      # Lógica de negocio
└── utils.py         # Utilidades
```

### Docstrings

```python
def crear_departamento(self, departamento):
    """
    Crea un nuevo departamento en la base de datos.
    
    Args:
        departamento (Departamento): Instancia del modelo Departamento
        
    Returns:
        None
        
    Raises:
        ValueError: Si los datos son inválidos
        DatabaseError: Si falla la inserción
    """
    pass
```

## 🚀 Deployment

### Preparar para Producción

```bash
# 1. Actualizar .env con credenciales seguras
DB_PASSWORD=<contraseña_fuerte>

# 2. Backup de datos
docker exec ecotech_mysql mysqldump -u ecotech_user -pecotech_pass ecotech_management > backup.sql

# 3. Aplicar migraciones
alembic upgrade head

# 4. Ejecutar aplicación
python main.py
```

### Backup y Restore

```bash
# Backup
docker exec ecotech_mysql mysqldump -u ecotech_user -pecotech_pass ecotech_management > backup_$(date +%Y%m%d).sql

# Restore
docker exec -i ecotech_mysql mysql -u ecotech_user -pecotech_pass ecotech_management < backup.sql
```

## 📚 Recursos

- [Python POO](https://docs.python.org/3/tutorial/classes.html)
- [Docker Compose](https://docs.docker.com/compose/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [PyMySQL](https://pymysql.readthedocs.io/)
- [SQL Injection Prevention](https://owasp.org/www-community/attacks/SQL_Injection)
