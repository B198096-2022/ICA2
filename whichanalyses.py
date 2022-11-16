#!/bin/python3

def whichanalysisfunc(taxon):
    clusterfunc(taxon)
    analysisall = input("Would you like to perform all analyses on the data? (yes/no):")
    while analysisall.upper() != "YES" and analysisall.upper() != "NO":
        print("Answer not yes or no value")
        analysisall = input("Would you like to perform all analyses on the data? (yes/no):")
    if analysisall.upper() == "YES":
        from bashfuncs import *
        plotconfunc(taxon)
        aligninfofunc(taxon)
        prettyplotfunc(taxon)
        #Generating seperate motif files for all of the entries
        from motiffunc import *
        motiffunc(taxon)
        #Pulling the
        from motiflist import *
        motiflist(taxon)
    if analysisall.upper() == "NO":
        from bashfuncs import *
        analysis1 = input("Would you like to perform conservation analysis on the sequences? (yes/no):")
        analysis2 = input("Would you like to see a pretty plot of alignments for the sequences? (yes/no):")
        analysis3 = input("Would you like to scan for PROSITE motifs in the sequences? (yes/no):")
        while analysis1.upper() != "YES" and analysis1.upper() != "NO":
            print("Answer not yes or no value")
            analysis1 = input("Would you like to perform conservation analysis on the sequences? (yes/no):")
        while analysis2.upper() != "YES" and analysis2.upper() != "NO":
            print("Answer not yes or no value")
            analysis2 = input("Would you like to see a pretty plot of alignments for the sequences? (yes/no):")
        while analysis3.upper() != "YES" and analysis3.upper() != "NO":
            print("Answer not yes or no value")
            analysis3 = input("Would you like to scan for PROSITE motifs in the sequences? (yes/no):")
        if analysis1.upper() == "YES":
            plotconfunc(taxon)
            aligninfofunc(taxon)
        if analysis2.upper() == "YES":
            prettyplotfunc(taxon)
        if analysis1.upper() == "YES":
            #Generating seperate motif files for all of the entries
            from motiffunc import *
            motiffunc(taxon)
            #Pulling the
            from motiflist import *
            motiflist(taxon)

