#creacion de script
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
def summarize_contents(filename):
	ejercicio = SeqIO.read(filenames, "genbank")
	ejercicio_r = SeqRecord(ejercicio)
	print(ejercicio)
sunnarize_contents(filename)
