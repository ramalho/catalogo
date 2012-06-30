from __future__ import unicode_literals

from django.test import TestCase

from .domain import Publicacao
from .models import Experimento

class SimpleTest(TestCase):
	def testar_instancia_Publicacao(self):
		titulo = 'O Alienista'
		pub = Publicacao(titulo=titulo)
		self.assertEqual(pub.titulo, titulo)

	def testar_instancia_Experimento(self):
		nome = 'Experimento #1'
		exp = Experimento(nome=nome)
		self.assertEqual(exp.nome, nome)
		exp.save()

