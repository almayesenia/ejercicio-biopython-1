#creacion de script
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os

filename = "/mnt/c/Users/Epicasso/Desktop/ejercicio-biopython/data/ls_orchid.gbk"

#Creacion de funcion
def summarize_contents(filename):
	listaOs = os.path.split(filename)
	record = list(SeqIO.parse(filename, "genbank"))
	#Creacion de diccionario
	d = {}
	d['File:'] = listaOs[1]
	d['Path:'] = listaOs[0]
	d['Num_records:'] = len(record)
	#Diccionario con listas
	d['Names:'] = []
	d['IDs:'] = []
	d['Descriptions'] = []
	#Registro de records
	for seq_rcd in SeqIO.parse(filename,"genbank"):
		d['Names:'].append(seq_rcd.name)
		d['IDs:'].append(seq_rcd.id)
		d['Descriptions'].append(seq_rcd.description)
	return d
#Imprimir la funcion
if __name__ == "__main__":
	resultados = summarize_contents(filename)
	print(resultados)
