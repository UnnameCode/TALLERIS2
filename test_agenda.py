import unittest
from agenda import Agenda

class TestAgenda(unittest.TestCase):

    def setUp(self):
        self.agenda = Agenda()

    def test_agregar_evento(self):
        self.agenda.agregar_evento("Evento de prueba", "2024-05-22", "12:00:00", "Descripción del evento", "Lugar del evento")

        evento_guardado = self.agenda.ver_eventos()[-1]
        self.assertEqual(evento_guardado[1], "Evento de prueba")
        self.assertEqual(evento_guardado[2], "2024-05-22")
        self.assertEqual(evento_guardado[3], "12:00:00")

    # Implementar pruebas unitarias para las demás funcionalidades (ver, editar, eliminar, buscar eventos)

if __name__ == '__main__':
    unittest.main()