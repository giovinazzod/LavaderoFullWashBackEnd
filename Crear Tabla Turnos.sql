CREATE TABLE turnos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    nombre_persona VARCHAR(100) NOT NULL,
    telefono_persona VARCHAR(20) NOT NULL,
    mail_persona VARCHAR(100) NOT NULL,
    patente_vehiculo VARCHAR(20) NOT NULL,
    servicio_descripcion VARCHAR(100) NOT NULL,
    servicio_costo DECIMAL(10, 2) NOT NULL,
    UNIQUE (fecha, hora)
);