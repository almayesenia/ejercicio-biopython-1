import unittest
import script

#Creacion de clase
class Prueba(unittest.TestCase):
	def test_summarize_contents(self):
		s = summarize_contents("data/AF323668.gbk")
		self.assertEqual("output", s)

		s = summarize_contents("data/NC_002703.gbk")
                self.assertEqual("output", s)  

		s = summarize_contents("data/ls_orchid.gbk")
                self.assertEqual("output", s)  

		s = summarize_contents("data/ls_orchid.fasta")
                self.assertEqual("output", s)

		s = summarize_contents("data/m_cold.fasta")
                self.assertEqual("output", s)

		s = summarize_contents("data/opuntia.fasta")
                self.assertEqual("output", s)  
