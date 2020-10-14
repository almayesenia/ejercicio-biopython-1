#creacion de script
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os
def summarize_contents(filename):
	SeqRec = SeqIO.read(filenames, "genbank")
	print("Name: ", record.name)
	print("Path: ",os.path.dirname(filename))
	records = list(SeqIO.parse(filename,"genbank"))
	print("Num_record = %i records" %len(records))
	for seq_record in SeqIO.parse(filename,"genbank"):
		print("ID :",record.id)

	
sunnarize_contents(filename)
