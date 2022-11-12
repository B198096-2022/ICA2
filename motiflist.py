#!/bin/python3
#This function will print a list of the motifs found given the genus/species/taxon label 
#I'll implement it into the pipeline later :)
def motiflist(label):
    for filename in os.listdir("{}_patmatmotifs".format(label)):
        with open("./{}_patmatmotifs/".format(label)+filename) as file:
            motifs = ''
            for line in file:
                if "Motif:" in line:
                    motif = line
                    motifs = motifs +"  "+motif
            if motifs == '':
                motifs = "no motifs found\n"
            print(filename)
            print(motifs)
