#creacion de script
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os

filename = "/mnt/c/Users/USUARIO/Desktop/3Semestre/Bioinformatica/biopython-notebook/notebooks/data/ls_orchid.gbk"
listaOs = []
def summarize_contents(filename):
	listaOs = os.path.split(filename)
	print("file :", listaOs[1])
	all_records = []
	record = list(SeqIO.parse(filename,"genbank"))
	print("Path: ",os.path.dirname(filename))
	print("Num_record = %i records" %len(record))
	print("\n")
	for seq_r in SeqIO.parse(filename,"genbank"):
		all_records.append(seq_r.name)
		print("Nombre: ",seq_r.name)
		print("ID :",seq_r.id)
		print("Descripcion: ", seq_r.description)
		print("Seq :", seq_r.seq	
sunnarize_contents(filename)
