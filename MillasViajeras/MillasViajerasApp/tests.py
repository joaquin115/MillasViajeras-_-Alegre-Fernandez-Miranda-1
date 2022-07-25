import datetime
from urllib import request
from django.test import TestCase

from .models import Publicaciones, Comentario
# Create your tests here.

class PublicacionesTest(TestCase):

    def setUp(self):
        Publicaciones.objects.create(pais="Argentina", titulo="Paseando por Recoleta", descripcion="Gran viaje por Argentina", fecha_viaje=datetime.datetime.today())

    def test_publicacion_pais(self):
        publicacion = Publicaciones.objects.get(pais="Argentina")
        self.assertEqual(publicacion.titulo, "Paseando por Recoleta")

    def test_publicacion_descripcion(self):
        publicacion = Publicaciones.objects.get(titulo="Paseando por Recoleta")
        self.assertEqual(publicacion.descripcion, "Gran viaje por Argentina")

class ComentarioTest(TestCase):

    def setUp(self):
        Comentario.objects.create(comentario="Buen viaje", autor=request.Request.user, fecha=datetime.datetime.today())

    def comentario_autor(self):
        comentario = comentario.objects.get(comentario="Buen viaje")
        self.assertEqual(comentario.fecha, datetime.datetime.now())