from django.test import TestCase
from aluraflix.serializers import ProgramaSerializer
from aluraflix.models import Programa

class SerializerTestCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo = 'Titulo Teste 1',
            data_lancamento = '2000-01-01',
            tipo = 'F',
            likes = 2340,
            dislikes = 40
        )
        self.serializer = ProgramaSerializer(instance=self.programa)
    
    def test_verifica_campos_serializados(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['titulo','tipo','data_lancamento','likes']))
    
    def test_verifica_conteudo_dos_campos_serializados(self):
        data = self.serializer.data
        self.assertEqual(set(data.values()), set([self.programa.titulo, self.programa.data_lancamento, self.programa.tipo, self.programa.likes]))
        

