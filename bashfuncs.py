#!/bin/python3

import os

def clusterfunc(taxon):
    clustercommand = "clustalo -i "+taxon+".fa -threads=16 -t protein --outfmt=msf -o "+taxon+"align.msf"
    os.system(clustercommand)

def plotconfunc(taxon):
    #This makes the conservation plot
    plotconcommand = "plotcon -sformat msf "+taxon+"align.msf -winsize 4 -graph cps -goutfile "+taxon+"_plotcon"
    displaycommand = "display "+taxon+"_plotcon.ps"
    os.system(plotconcommand)
    os.system(displaycommand)

def aligninfofunc(taxon):
    #This generates a file with the alignment info for each protein
    infocommand = "infoalign "+taxon+"align.msf -outfile "+taxon+"_aligninfo.txt -only -heading -name -seqlength -idcount -simcount -diffcount -change"
    displaycommand = "head -10 "+taxon+"_aligninfo.txt"
    os.system(infocommand)
    os.system(displaycommand)

def prettyplotfunc(taxon):
    #pretty plot shows the alignments visually
    prettycommand = "prettyplot "+taxon+"align.msf -sformat1 msf -docolour -graph cps -goutfile "+taxon+"_prettyplot"
    os.system(prettycommand)
    displaycommand = "display "+taxon+"_prettyplot.ps"
    os.system(displaycommand)

