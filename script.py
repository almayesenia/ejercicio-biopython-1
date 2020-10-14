from Bio.Seq import Seq
from Bio.SeqFeatures import SeqFeatures
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
def summarize_contents(filename.gbk):
	ejercicio = SeqIO.read("filenames.gbk", "genbank")
	print(ejercicio)
