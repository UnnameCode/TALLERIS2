import unittest
from agenda import Agenda

class TestIntegracionAgenda(unittest.TestCase):

    def setUp(self):
        self.agenda = Agenda()

    def test_agregar_evento_y_editar_evento(self):
        self.agenda.agregar_evento("Evento de prueba", "2024-05-22", "12:00:00", "Descripción del evento", "Lugar del evento")

        evento_id = self.agenda.ver_eventos()[-1][0]
        self.agenda.editar_evento(evento_id, "Evento editado", "2024-05-23", "13:00:00", "Descripción actualizada", "Nuevo lugar")

        eventos_actualizados = self.agenda.ver_eventos()
        for evento in eventos_actualizados:
            if evento[0] == evento_id:
                self.assertEqual(evento[1], "Evento editado")
                self.assertEqual(evento[2], "2024-05-23")
                self.assertEqual(evento[3], "13:00:00")
                break

    def test_agregar_evento_y_eliminar_evento(self):
        self.agenda.agregar_evento("Evento de prueba", "2024-05-22", "12:00:00", "Descripción del evento", "Lugar del evento")

        evento_id = self.agenda.ver_eventos()[-1][0]
        self.agenda.eliminar_evento(evento_id)

        eventos_restantes = self.agenda.ver_eventos()
        for evento in eventos_restantes:
            self.assertNotEqual(evento[0], evento_id)

    # Implementar más pruebas de integración para verificar la interacción entre la interfaz de usuario y la base de datos, como:
    # * Buscar eventos y verificar la visualización correcta de los resultados.
    # * Editar eventos desde la interfaz y comprobar que los cambios se reflejan en la base de datos.
    # * Eliminar eventos desde la interfaz y confirmar que se eliminan de la base de datos.

if __name__ == '__main__':
    unittest.main()