"""Modelos SQLAlchemy para migraciones con Alembic"""
from sqlalchemy import Column, String, Text, Integer, DECIMAL, Date, TIMESTAMP, Boolean, ForeignKey, JSON, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Rol(Base):
    __tablename__ = 'roles'
    
    id = Column(String(50), primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)
    descripcion = Column(Text)
    nivel_permisos = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    activo = Column(Boolean, default=True)


class Permiso(Base):
    __tablename__ = 'permisos'
    
    id = Column(String(50), primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)
    descripcion = Column(Text)
    modulo = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())


class RolPermiso(Base):
    __tablename__ = 'rol_permisos'
    
    id = Column(String(50), primary_key=True)
    rol_id = Column(String(50), ForeignKey('roles.id', ondelete='CASCADE'), nullable=False)
    permiso_id = Column(String(50), ForeignKey('permisos.id', ondelete='CASCADE'), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())


class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(String(50), primary_key=True)
    nombre_usuario = Column(String(100), nullable=False, unique=True)
    contrasena_cifrada = Column(String(255), nullable=False)
    salt = Column(String(255), nullable=False)
    rol_id = Column(String(50), ForeignKey('roles.id'), nullable=False)
    fecha_creacion = Column(TIMESTAMP, server_default=func.current_timestamp())
    ultimo_login = Column(TIMESTAMP, nullable=True)
    activo = Column(Boolean, default=True)


class Departamento(Base):
    __tablename__ = 'departamentos'
    
    id = Column(String(50), primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)
    descripcion = Column(Text)
    gerente_id = Column(String(50), ForeignKey('empleados.id'), nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    activo = Column(Boolean, default=True)


class Empleado(Base):
    __tablename__ = 'empleados'
    
    id = Column(String(50), primary_key=True)
    usuario_id = Column(String(50), ForeignKey('usuarios.id'), nullable=False, unique=True)
    nombre = Column(String(200), nullable=False)
    direccion = Column(Text)
    telefono = Column(String(20))
    email = Column(String(150), nullable=False)
    fecha_inicio_contrato = Column(Date, nullable=False)
    salario = Column(DECIMAL(10, 2))
    departamento_id = Column(String(50), ForeignKey('departamentos.id'), nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())


class Proyecto(Base):
    __tablename__ = 'proyectos'
    
    id = Column(String(50), primary_key=True)
    nombre = Column(String(200), nullable=False)
    descripcion = Column(Text)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    activo = Column(Boolean, default=True)


class EmpleadoProyecto(Base):
    __tablename__ = 'empleado_proyecto'
    
    id = Column(String(50), primary_key=True)
    empleado_id = Column(String(50), ForeignKey('empleados.id'), nullable=False)
    proyecto_id = Column(String(50), ForeignKey('proyectos.id'), nullable=False)
    fecha_asignacion = Column(Date, server_default=func.current_date())
    fecha_desasignacion = Column(Date, nullable=True)
    activo = Column(Boolean, default=True)


class RegistroTiempo(Base):
    __tablename__ = 'registros_tiempo'
    
    id = Column(String(50), primary_key=True)
    empleado_id = Column(String(50), ForeignKey('empleados.id'), nullable=False)
    proyecto_id = Column(String(50), ForeignKey('proyectos.id'), nullable=False)
    fecha = Column(Date, nullable=False)
    horas_trabajadas = Column(DECIMAL(4, 2), nullable=False)
    descripcion_tareas = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    aprobado = Column(Boolean, default=False)
    aprobado_por = Column(String(50), ForeignKey('usuarios.id'), nullable=True)


class Informe(Base):
    __tablename__ = 'informes'
    
    id = Column(String(50), primary_key=True)
    titulo = Column(String(200), nullable=False)
    tipo_informe = Column(String(50), nullable=False)
    formato = Column(String(10), default='pdf')
    contenido = Column(JSON)
    generado_por = Column(String(50), ForeignKey('usuarios.id'), nullable=False)
    fecha_generacion = Column(TIMESTAMP, server_default=func.current_timestamp())
    ruta_archivo = Column(String(500))


class LogAuditoria(Base):
    __tablename__ = 'logs_auditoria'
    
    id = Column(String(50), primary_key=True)
    usuario_id = Column(String(50), ForeignKey('usuarios.id'), nullable=False)
    accion = Column(String(100), nullable=False)
    tabla_afectada = Column(String(100))
    registro_id = Column(String(50))
    datos_anteriores = Column(JSON)
    datos_nuevos = Column(JSON)
    fecha_evento = Column(TIMESTAMP, server_default=func.current_timestamp())
    ip_address = Column(String(45))


class AdministradorRH(Base):
    __tablename__ = 'administradores_rh'
    
    id = Column(String(50), primary_key=True)
    usuario_id = Column(String(50), ForeignKey('usuarios.id'), nullable=False, unique=True)
    nivel_acceso = Column(Integer, default=1)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
