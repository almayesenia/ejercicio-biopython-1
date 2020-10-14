#creacion de script
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os
def summarize_contents(filename):
	all_records = []
	SeqRec = list(SeqIO.parse(filename,"genbank"))
	print("Path: ",os.path.dirname(filename))
	print("Num_record = %i records" %len(SeqRec))
	
	for seq_record in SeqIO.parse(filename,"genbank"):
		print("Name: ",seq_record.name)
		print("ID :",SeqRec.id)
	
sunnarize_contents(filename)
