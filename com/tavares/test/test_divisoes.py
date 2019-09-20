from unittest import TestCase
from com.tavares.divisoes import divisoes


class TestDivisao(TestCase):
	def setUp(self):
		self.divisoes = divisoes()
		
	def test_divisao(self):
		self.assertEqual(self.divisoes.divisao(6, 2), 3, 'Deve ser 3')