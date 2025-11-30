-- Script de creación de base de datos para EcoTech Solutions
-- MySQL Version 8.0+

CREATE DATABASE IF NOT EXISTS ecotech_management;
USE ecotech_management;

-- Tabla de roles
CREATE TABLE roles (
    id VARCHAR(50) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    descripcion TEXT,
    nivel_permisos INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT TRUE,
    
    INDEX idx_roles_nombre (nombre),
    INDEX idx_roles_permisos (nivel_permisos)
);

-- Tabla de permisos
CREATE TABLE permisos (
    id VARCHAR(50) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    descripcion TEXT,
    modulo VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    INDEX idx_permisos_nombre (nombre),
    INDEX idx_permisos_modulo (modulo)
);

-- Tabla de relación roles-permisos
CREATE TABLE rol_permisos (
    id VARCHAR(50) PRIMARY KEY,
    rol_id VARCHAR(50) NOT NULL,
    permiso_id VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    INDEX idx_rol_permisos_rol (rol_id),
    INDEX idx_rol_permisos_permiso (permiso_id),
    UNIQUE INDEX uk_rol_permiso (rol_id, permiso_id),
    
    FOREIGN KEY (rol_id) REFERENCES roles(id) ON DELETE CASCADE,
    FOREIGN KEY (permiso_id) REFERENCES permisos(id) ON DELETE CASCADE
);

-- Tabla de usuarios
CREATE TABLE usuarios (
    id VARCHAR(50) PRIMARY KEY,
    nombre_usuario VARCHAR(100) NOT NULL UNIQUE,
    contrasena_cifrada VARCHAR(255) NOT NULL,
    salt VARCHAR(255) NOT NULL,
    rol_id VARCHAR(50) NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ultimo_login TIMESTAMP NULL,
    activo BOOLEAN DEFAULT TRUE,
    
    INDEX idx_usuarios_nombre (nombre_usuario),
    INDEX idx_usuarios_rol (rol_id),
    
    FOREIGN KEY (rol_id) REFERENCES roles(id)
);

-- Tabla de departamentos
CREATE TABLE departamentos (
    id VARCHAR(50) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    descripcion TEXT,
    gerente_id VARCHAR(50) NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT TRUE,
    
    INDEX idx_departamentos_nombre (nombre),
    INDEX idx_departamentos_gerente (gerente_id)
);

-- Tabla de empleados
CREATE TABLE empleados (
    id VARCHAR(50) PRIMARY KEY,
    usuario_id VARCHAR(50) NOT NULL UNIQUE,
    nombre VARCHAR(200) NOT NULL,
    direccion TEXT,
    telefono VARCHAR(20),
    email VARCHAR(150) NOT NULL,
    fecha_inicio_contrato DATE NOT NULL,
    salario DECIMAL(10,2),
    departamento_id VARCHAR(50) NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    INDEX idx_empleados_usuario (usuario_id),
    INDEX idx_empleados_email (email),
    INDEX idx_empleados_departamento (departamento_id),
    
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
);

-- Ahora actualizamos la foreign key de gerente_id en departamentos
ALTER TABLE departamentos 
ADD CONSTRAINT fk_departamentos_gerente 
FOREIGN KEY (gerente_id) REFERENCES empleados(id);

-- Tabla de proyectos
CREATE TABLE proyectos (
    id VARCHAR(50) PRIMARY KEY,
    nombre VARCHAR(200) NOT NULL,
    descripcion TEXT,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT TRUE,
    
    INDEX idx_proyectos_nombre (nombre),
    INDEX idx_proyectos_fecha_inicio (fecha_inicio)
);

-- Tabla de relación empleado-proyecto
CREATE TABLE empleado_proyecto (
    id VARCHAR(50) PRIMARY KEY,
    empleado_id VARCHAR(50) NOT NULL,
    proyecto_id VARCHAR(50) NOT NULL,
    fecha_asignacion DATE DEFAULT (CURRENT_DATE),
    fecha_desasignacion DATE NULL,
    activo BOOLEAN DEFAULT TRUE,
    
    INDEX idx_emp_proy_empleado (empleado_id),
    INDEX idx_emp_proy_proyecto (proyecto_id),
    UNIQUE INDEX uk_empleado_proyecto_activo (empleado_id, proyecto_id, activo),
    
    FOREIGN KEY (empleado_id) REFERENCES empleados(id),
    FOREIGN KEY (proyecto_id) REFERENCES proyectos(id)
);

-- Tabla de registros de tiempo
CREATE TABLE registros_tiempo (
    id VARCHAR(50) PRIMARY KEY,
    empleado_id VARCHAR(50) NOT NULL,
    proyecto_id VARCHAR(50) NOT NULL,
    fecha DATE NOT NULL,
    horas_trabajadas DECIMAL(4,2) NOT NULL,
    descripcion_tareas TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    aprobado BOOLEAN DEFAULT FALSE,
    aprobado_por VARCHAR(50) NULL,
    
    INDEX idx_registros_empleado (empleado_id),
    INDEX idx_registros_proyecto (proyecto_id),
    INDEX idx_registros_fecha (fecha),
    INDEX idx_registros_empleado_fecha (empleado_id, fecha),
    
    FOREIGN KEY (empleado_id) REFERENCES empleados(id),
    FOREIGN KEY (proyecto_id) REFERENCES proyectos(id),
    FOREIGN KEY (aprobado_por) REFERENCES usuarios(id),
    
    CONSTRAINT chk_horas_trabajadas CHECK (horas_trabajadas > 0 AND horas_trabajadas <= 24)
);

-- Tabla de informes
CREATE TABLE informes (
    id VARCHAR(50) PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    tipo_informe VARCHAR(50) NOT NULL,
    formato VARCHAR(10) DEFAULT 'pdf',
    contenido JSON,
    generado_por VARCHAR(50) NOT NULL,
    fecha_generacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ruta_archivo VARCHAR(500),
    
    INDEX idx_informes_tipo (tipo_informe),
    INDEX idx_informes_generado_por (generado_por),
    INDEX idx_informes_fecha (fecha_generacion),
    
    FOREIGN KEY (generado_por) REFERENCES usuarios(id)
);

-- Tabla de logs de auditoría
CREATE TABLE logs_auditoria (
    id VARCHAR(50) PRIMARY KEY,
    usuario_id VARCHAR(50) NOT NULL,
    accion VARCHAR(100) NOT NULL,
    tabla_afectada VARCHAR(100),
    registro_id VARCHAR(50),
    datos_anteriores JSON,
    datos_nuevos JSON,
    fecha_evento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ip_address VARCHAR(45),
    
    INDEX idx_logs_usuario (usuario_id),
    INDEX idx_logs_tabla (tabla_afectada),
    INDEX idx_logs_fecha (fecha_evento),
    
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- Tabla de administradores RH (especialización)
CREATE TABLE administradores_rh (
    id VARCHAR(50) PRIMARY KEY,
    usuario_id VARCHAR(50) NOT NULL UNIQUE,
    nivel_acceso INT DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    INDEX idx_admin_rh_usuario (usuario_id),
    
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);
