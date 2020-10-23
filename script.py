#creacion de script
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os

filename = "/mnt/c/Users/USUARIO/Desktop/biopython-notebook/notebooks/data/ls_orchid.gbk"

#Creacion de funcion
def summarize_contents(filename):
	listaOs = []
	listaOs = os.path.split(filename)
	Cadena = " "

	#Rutas
	Cadena = ("file :" + listaOs[1] + "\npath: " + listaOs[0])

	#Numero de records
	all_records = []
	record = list(SeqIO.parse(filename,"genbank"))
	Cadena += ("\nNum_record =" + str(len(record)))
	for seq_rcd in SeqIO.parse(filename,"genbank"):
		all_records.append(seq_rcd.name)
		Cadena += ("\nName: " + seq_rcd.name)
		Cadena += ("\nID :"+ str(seq_rcd.id))
		Cadena += ("\nDescription: " + str(seq_rcd.description))
		Cadena += ("\n")
	return Cadena
#Imprimir la funcion
resultados = summarize_contents(filename)
print(resultados)
