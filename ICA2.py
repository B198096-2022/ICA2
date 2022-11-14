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

import extract

#Using grep to make a file of fa headers for all of the samples by pulling lines with ">"
#Then using awk to pull every line that doesn't have ">", which will be the sequences
#And inserting a "_" in the place of the fa header line to be used to split later
headercommand = "grep '>' "+taxon+".fa > headers.txt"
seqscommand = "awk '/^>/ { print '_'; next; }; {print; }' "+taxon+".fa > seqs.txt"
os.system(headercommand)
os.system(seqscommand)
#Opening the headers.txt file
with open("headers.txt") as file:
    headers = file.read()
#Opening the seqs.txt file
with open("seqs.txt") as file:
    seqs = file.read()

#Now using the headers and seqs files I am splitting them into lists
#I need to split up the seqs with split, then rejoin, putting a space between the seqs,
#Then split again based on the space
#this is not very elegant but it solved other problems I was having and it works
#so I'm sticking with it
seqlist1 = seqs.split("\n\n")
seqstr = " \n".join(seqlist1)
seqlist = seqstr.split(" ")
headerlist = headers.split("\n")
#Now this just scans and ensures that there are no blank spaces
#At the beginning or end of the lists that could offset the two lists
if seqlist[0] == '':
    seqlist = seqlist[1:] #This DOES cut off first empty space

if seqlist[-1] == '':
    seqlist = seqlist[0:-1] #This does nothing

if headerlist[0] == '':
    headerlist = headerlist[1:] #This does nothing

if headerlist[-1] == '':
    headerlist = headerlist[0:-1] #This cuts off the final empty space

#Now I am making a dictionary with all of the sequences. Defining the length of the dict
dictlen = len(seqlist)

#Now I can making a dictionary, and for all numbers in the range of dictlen
#I am looping through and adding the headerlist enrty for that position as the key and
#seqlist entry for that position position as the value
seqdict = {}
seqdict[headerlist[0]] = seqlist[0]
for i in range(dictlen):
    seqdict[headerlist[i]] = seqlist[i]
