#!/bin/python3

#motiflist('txid4890_300-500')

#!/bin/python3
#This function will print a list of the motifs found given the genus/species/taxon label
#I'll implement it into the pipeline later :)
def motiflist(label):
    import os
    allmotifs = ''
    for filename in os.listdir("{}_patmatmotifs".format(label)):
        with open("./{}_patmatmotifs/".format(label)+filename) as file:
            motifs = ''
            for line in file:
                if "Motif:" in line:
                    motif = line
                    motifs = motifs +"  "+motif
            if motifs == '':
                motifs = "no motifs found\n"
            accession = filename[:-13]
            print('Accession number: '+accession)
            print(motifs)
            allmotifs = allmotifs + 'Accession number: '+accession+"\n"+motifs+"\n"
    with open("{}_motifs.txt".format(label),"w") as my_file:
        my_file.write(allmotifs)
