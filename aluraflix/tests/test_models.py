from django.test import TestCase
from aluraflix.models import Programa


class ProgramaModelTestCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo = 'Titulo Teste 1',
            data_lancamento = '2000-01-01'
        )

    def test_verifica_atributos_do_programa(self):
        self.assertEqual(self.programa.titulo,'Titulo Teste 1')
        self.assertEqual(self.programa.tipo,'F')
        self.assertEqual(self.programa.data_lancamento,'2000-01-01')
        self.assertEqual(self.programa.likes, 0)
        self.assertEqual(self.programa.dislikes, 0)




