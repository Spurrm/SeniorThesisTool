from Bio import SeqIO
from Bio.Seq import Seq

myFile_str = raw_input("  Enter File :") #Enter file name to read from
#data_str = open(myFile_str)	#opens file
#data_str.close()	#close file

#my_file = open('Diabetes.fasta')
listt=[]

#for record in SeqIO.parse(my_file,'fasta'):
for record in SeqIO.parse(myFile_str,'fasta'):
    id = record.id
    seq_a = record.seq
    print 'File Name: ', myFile_str #prints the entered files name
    print 'Name: ', id	#prints the name of the DNA sequence
    print 'Size: ', len(seq_a)	#prints the length of the sequence
    print 'Sequence: ', seq_a		#prints out the whole DNA sequence

    RNAfromDNA_str  = seq_a.transcribe() # gives RNA sequence
    #DNAfromRNA_str  = seq.back_transcribe(RNAfromDNA_str) # gives DNA sequence from the RNA conversion
    PROTfromRNA_str = RNAfromDNA_str.translate()


    print " Original DNA  :",seq_a #prints DNA sequence of mut.fasta
    print " RNA from DNA  :",RNAfromDNA_str #prints RNA sequence of mut.fasta
    #print " DNA from RNA  :",DNAfromRNA_str
    print " PROT from RNA :",PROTfromRNA_str #prints the protiens of mut.fasta

    # print Counter(seq)			#counts each of the bases in the DNA sequence
    # 	print Counter(myFile_str(seq))



    myFile_str = raw_input("  Enter File :") #Enter file name to read from
    dna = myFile_str
        #data_str = open(myFile_str)	#opens file
        #data_str.close()
        #for record in SeqIO.parse(my_file,'fasta'):
    for record in SeqIO.parse(myFile_str,'fasta'):

        id = record.id
        seq_b = record.seq
        print 'File Name: ', myFile_str #prints the entered files name
        print 'Name: ', id	#prints the name of the DNA sequence
        print 'Size: ', len(seq_b)	#prints the length of the sequence
        print 'Sequence: ', seq_b	#prints out the whole DNA sequence


    RNAfromDNA_str  = seq_b.transcribe() # gives RNA sequence
    #DNAfromRNA_str  = seq.back_transcribe(RNAfromDNA_str) # gives DNA sequence from the RNA conversion
    PROTfromRNA_str = RNAfromDNA_str.translate() #translating RNA into DNA


    print " Original DNA  :",seq_b #prints wild.fasta sequence
    print " RNA from DNA  :",RNAfromDNA_str #prints the RNA of wild.fasta sequence
    #print " DNA from RNA  :",DNAfromRNA_str
    print " PROT from RNA :",PROTfromRNA_str #prints the protiens of wild.fasta sequence



    # note: a method to compare two entered sequences
    print " This is the compareSequences() method"
    print " seq_a :",seq_a
    print " seq_b :",seq_b

for i in range(len(seq_a)):
    #print " checking: seqA_str, current char: ",i, seqA_str[i]
    if seq_a[i] != seq_b[i]:
        print "\n Sequences are different at position :", i
        print "   seqA_str[i] != ",seq_a[i]
        print "   seqB_str[i] != ",seq_b[i]
