#!/bin/python3

import os
from bashfuncs import *
from motiffunc import *
from motiflist import *


def whichanalysisfunc(taxon, oneseq = 'no',first='no'):
    if oneseq == 'no':
        clusterfunc(taxon)
        analysisall = input("Would you like to perform all analyses on the data? (yes/no):")
        while analysisall.upper() != "YES" and analysisall.upper() != "NO":
            print("Answer not yes or no value")
            analysisall = input("Would you like to perform all analyses on the data? (yes/no):")
        if analysisall.upper() == "YES":
            plotconfunc(taxon)
            aligninfofunc(taxon)
            prettyplotfunc(taxon)
            #Generating seperate motif files for all of the entries
            motiffunc(taxon)
            #Pulling the
            motiflist(taxon)
        if analysisall.upper() == "NO":
            analysis1 = input("Would you like to perform conservation analysis on the sequences? (yes/no):")
            while analysis1.upper() != "YES" and analysis1.upper() != "NO":
                print("Answer not yes or no value")
                analysis1 = input("Would you like to perform conservation analysis on the sequences? (yes/no):")
            if analysis1.upper() == "YES":
                aligninfofunc(taxon)
            analysis4 = input("Would you like to view alignment iformation on the sequences? (yes/no):")
            while analysis4.upper() != "YES" and analysis1.upper() != "NO":
                print("Answer not yes or no value")
                analysis4 = input("Would you like to view alignment iformation on the sequences? (yes/no):")
            if analysis4.upper() == "YES":
                aligninfofunc(taxon)
            analysis2 = input("Would you like to see a pretty plot of alignments for the sequences? (yes/no):")
            while analysis2.upper() != "YES" and analysis2.upper() != "NO":
                print("Answer not yes or no value")
                analysis2 = input("Would you like to see a pretty plot of alignments for the sequences? (yes/no):")
            if analysis2.upper() == "YES":
                prettyplotfunc(taxon)
            analysis3 = input("Would you like to scan for PROSITE motifs in the sequences? (yes/no):")
            while analysis3.upper() != "YES" and analysis3.upper() != "NO":
                print("Answer not yes or no value")
                analysis3 = input("Would you like to scan for PROSITE motifs in the sequences? (yes/no):")
            if analysis1.upper() == "YES":
                #Generating seperate motif files for all of the entries
                motiffunc(taxon)
                #Pulling the
                motiflist(taxon)
    if oneseq == 'yes' and first == 'no':
        stillmotif = input("Would you still like to perform motif analysis on your single selected sequence? (yes/no):")
        while stillmotif.upper() != "YES" and analysis1.upper() != "NO":
            print("Answer not yes or no value")
            stillmotif = input("Would you still like to perform motif analysis on your single selected sequence? (yes/no):")
        if stillmotif.upper() == "YES":
            #Generating seperate motif files for all of the entries
            motiffunc(taxon)
            #Pulling the
            motiflist(taxon)
    if oneseq == 'yes' and first == 'yes':
        #Generating seperate motif files for all of the entries
        motiffunc(taxon)
        #Pulling the
        motiflist(taxon)
        print("Motif analysis is complete and is the only analysis available for one sequence")
        print("now exiting program")
        exit()











#

