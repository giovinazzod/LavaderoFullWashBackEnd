from app.database import get_db

class Turno:
    #Constructor
    def __init__(self,id=None,fecha=None,hora=None,nombre_persona=None,telefono_persona=None,mail_persona=None,patente_vehiculo=None,servicio_descripcion=None,servicio_costo=None):
        self.id=id
        self.fecha=fecha
        self.hora=hora
        self.nombre_persona=nombre_persona
        self.telefono_persona=telefono_persona
        self.mail_persona=mail_persona
        self.patente_vehiculo=patente_vehiculo
        self.servicio_descripcion=servicio_descripcion
        self.servicio_costo=servicio_costo

    def serialize(self):
        return {
            "id": self.id,
            #"fecha": self.fecha,
            "fecha": str(self.fecha), #Convierto de timedelta a string para poder convertir directamente a JSON
            #"hora": self.hora,
            "hora": str(self.hora),  #Convierto de timedelta a string para poder convertir directamente a JSON
            "nombre_persona": self.nombre_persona,
            "telefono_persona": self.telefono_persona,
            "mail_persona": self.mail_persona,
            "patente_vehiculo": self.patente_vehiculo,
            "servicio_descripcion": self.servicio_descripcion,
            "servicio_costo": self.servicio_costo
        }

#Métodos
    @staticmethod #me permite usar el metodo sin instanciar el objeto previamente
    def getTurnos():
        db = get_db()
        cursor = db.cursor() #encargado de ejecutar sentencias SQL
        query = "SELECT * FROM Turnos"
        cursor.execute(query)
        rows = cursor.fetchall() #Devuelve lista de tuplas con los reultados

        turnos = [Turno(id=row[0],fecha=row[1],hora=row[2],nombre_persona=row[3],telefono_persona=row[4],mail_persona=row[5],patente_vehiculo=row[6],servicio_descripcion=row[7],servicio_costo=row[8]) for row in rows]

        cursor.close()

        ## Uso el método serialize() para convertir los objetos Turno a diccionarios porque si no me daba error el método getTurnos()
        turnos_serialized = [turno.serialize() for turno in turnos]
        return turnos_serialized

    @staticmethod
    def get_by_id(id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM turnos WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            #return Movie(id_movie=row[0], title=row[1], director=row[2], release_date=row[3], banner=row[4])
            return Turno(id=row[0],fecha=row[1],hora=row[2],nombre_persona=row[3],telefono_persona=row[4],mail_persona=row[5],patente_vehiculo=row[6],servicio_descripcion=row[7],servicio_costo=row[8])

        return None