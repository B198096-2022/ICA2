#!bin/bash/python3

#These are all of the modules I will need
import os
import shutil
import requests
import pandas as pd
#Asking the user to input the taxonid and protien name
taxon = input("Enter desired taxonid:") #txid4890
proteinfam = input("Enter desired protein name:") #pyruvate dehydrogenase
#I am then generating my esearch command that will be stored in a varaible
#It is an esearch wihin the protein database
#Specifying the taxonid and protein name based on the user input
#I specified not partial to remove any entires that are protein fragments
#I then used efectch to grab the sequence data for each of these protein entries
#Within efetch I also specified to output the data into a file in msf format for the next step
#This output file is named based on the taxonid
searchcommand = "esearch -db protein -query '"+taxon+"[Organism:exp] AND "+proteinfam+"[Protein Name] NOT Partial' | efetch -format fasta > "+taxon+".fa"
print(searchcommand)
#Now using os.system to run the searchcommand in bash
os.system(searchcommand)

import clusterplot
