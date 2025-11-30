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
