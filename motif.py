#!/bin/python3
#This code splits up the protein seqiences into fasta headers and sequences
#Puts a "_" to deliminate the sequences
#Open the files in python then split them into a list
#Then put them into a dict with header as key and seq as value
grep ">" txid4890.prot.fa > headers.txt
awk '/^>/ { print "_"; next; }; {print; }' txid4890.prot.fa > seqs.txt

with open("headers.txt") as file:
    headers = file.read()

with open("seqs.txt") as file:
    seqs = file.read()

seqclean = seqs.replace("\n", "")
seqlist = seqclean.split("_")
headerlist = headers.split("\n")
if seqlist[0] == '':
    seqlist = seqlist[1:]

if seqlist[-1] == '':
    seqlist = seqlist[0:-2]

if headerlist[0] == '':
    headerlist = headerlist[1:]

if headerlist[-1] == '':
    headerlist = headerlist[0:-2]

dictlen = len(seqlist)

seqdict = {}
seqdict[headerlist[0]] = seqlist[0]
for i in range(dictlen):
    seqdict[headerlist[i]] = seqlist[i]

#Make a test dictionary with the first sequence
testdict = {}
testdict[headerlist[0]] = seqlist[0]
testdict[headerlist[1]] = seqlist[1]

#Making individual fasta files works better!

for head, seq in testdict.items():
    fasta = name+ os.linesep +seq
    headline = head.split()
    code = (headline[0])
    code = code[1:-3]
    with open("{}.fa".format(code),"w") as my_file:
         my_file.write(fasta)
    command = "patmatmotifs -full -sequence "+code+".fa -sprotein1 YES -sformat1 fasta -outfile "+code+".patmatmotifs"
    os.system(command)
