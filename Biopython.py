
#FUNCTION NAME: ParseFastaFile
#PARAMETERS: 1 (File Name -a string of the name of a fasta sequence file)
#PURPOSE: The function should:
#           (1) Use Biopython to parse a fasta file with multiple sequences.
#           (2) Make a dictionary: The keys will be the gi number 
#               and the values the sequences.
#
#RETURN VALUES: The dictionary with ALL the entries.

#== FUNCTION 1 ==
from Bio import SeqIO

def ParseFastaFile(fs):
    records = {}
    for seq_record in SeqIO.parse(fs, "fasta"):
        gi_number=seq_record.id.split("|")
        sequence=seq_record.seq
        records[gi_number[1]]=sequence

    return records

#output = ParseFastaFile(ls_orchid.fasta)
#print output

#---------------------------------------------------------------------------------
#FUNCTION NAME: GetGenbankInfo
#PARAMETERS: 1 (File Name -a string of the name of a GenBank sequence file)
#PURPOSE: The function should:
#           (1) Use Biopython to parse the GenBank file with multiple sequences.
#           (2) Make a dictionary -
#                   (i)  The key will be the record.id
#                   (ii) The value will be a LIST with two items:
#                       1. the description
#                       2. the sequence

#== FUNCTION 2 ==
from Bio import SeqIO

def ParseGenbankFile(fs):
    d_genbank = {}
    for seq_record in SeqIO.parse(fs, "genbank"):
        d_genbank[seq_record.id] =[seq_record.description]

    return d_genbank

#output2=ParseGenbankFile(ls_orchid.gbk)
#print output2

#---------------------------------------------------------------------------------
#FUNCTION NAME: TranscribeTranslate
#PARAMETERS: 1 (A list of sequence nmers)
#PURPOSE: The function should:
#           (1) Iterate through the LIST of DNA sequence nmers. You make them up.
#           (2) Using Biopython, it should transcribe and then translate each sequence.
#           (3) These amino acid sequences should be stored in a list.
  
#RETURN VALUES: A LIST of all the amino acid sequences (strings)


#== FUNCTION 3 ==
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

def TranscribeTranslate(nmer_list):
    protein = []
    for i in range(0,len(nmer_list)):
        coding_strand = Seq(nmer_list[i], generic_dna)
        m_rna = coding_strand.transcribe()
        prot = m_rna.translate()
        protein.append(prot)
    
    return protein

#output = TranscribeTranslate(['ATGGCCATTGTA','ATGGGCCGC','TGAAAGGGTGCCCGATAG'])
#print output

#---------------------------------------------------------------------------------
#FUNCTION NAME: FetchGenbankFile
#PARAMETERS: 1 (A string - Pubmed ID number)
#PURPOSE: The function should:
#           (1) Get the genbank file as text from the nucleotide database.
#           (2) Write it to a file. (See below)
#RETURN VALUES: 1 (True)

#== FUNCTION 4 ==
from Bio import Entrez
from Bio import SeqIO
    
def FetchGenbankFile(pubmedID):
    fin = open("%s.gbk.txt" %pubmedID,'w')
    Entrez.mail = "dnyanada27@yahoo.co.in"
    handle = Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id="%s" %pubmedID)
    seq_record = SeqIO.read(handle, "gb")
    handle.close()
    fin.write("%s" %seq_record)
    fin.close()
    

    return 1
#print FetchGenbankFile('186972394')



