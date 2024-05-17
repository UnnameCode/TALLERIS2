import sqlite3

class Agenda:
    def __init__(self):
        self.conexion = sqlite3.connect('agenda.db')
        self.cursor = self.conexion.cursor()

        # Crear la tabla 'eventos' si no existe
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS eventos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                fecha TEXT NOT NULL,
                hora TEXT NOT NULL,
                descripcion TEXT,
                ubicacion TEXT
            )
        """)

    def agregar_evento(self, nombre, fecha, hora, descripcion, ubicacion):
        self.cursor.execute("""
            INSERT INTO eventos (nombre, fecha, hora, descripcion, ubicacion)
            VALUES (?, ?, ?, ?, ?)
        """, (nombre, fecha, hora, descripcion, ubicacion))
        self.conexion.commit()

    def ver_eventos(self):
        self.cursor.execute("""
            SELECT * FROM eventos ORDER BY fecha, hora
        """)
        eventos = self.cursor.fetchall()
        return eventos

    def editar_evento(self, id_evento, nombre, fecha, hora, descripcion, ubicacion):
        self.cursor.execute("""
            UPDATE eventos
            SET nombre = ?, fecha = ?, hora = ?, descripcion = ?, ubicacion = ?
            WHERE id = ?
        """, (nombre, fecha, hora, descripcion, ubicacion, id_evento))
        self.conexion.commit()

    def eliminar_evento(self, id_evento):
        self.cursor.execute("""
            DELETE FROM eventos WHERE id = ?
        """, (id_evento,))
        self.conexion.commit()

    def buscar_eventos(self, criterio):
        # Implementar la búsqueda de eventos por criterio (nombre, fecha, hora o descripción)
        pass

if __name__ == '__main__':
    agenda = Agenda()

    # Ejemplo de uso
    agenda.agregar_evento("Reunión de trabajo", "2024-05-20", "10:00:00", "Discusión del proyecto X", "Oficina central")
    agenda.agregar_evento("Consulta médica", "2024-05-25", "15:30:00", "Revisión general", "Clínica Sanidad")

    eventos = agenda.ver_eventos()
    for evento in eventos:
        print(f"{evento[1]} - {evento[2]} ({evento[3]})")