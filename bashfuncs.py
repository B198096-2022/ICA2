#!/bin/python3

def clusterfunc(taxon):
    import os
    clustercommand = "clustalo -i "+taxon+".fa -threads=16 -t protein --outfmt=msf -o "+taxon+"align.msf"
    os.system(clustercommand)

def plotconfunc(taxon):
    #This makes the conservation plot
    import os
    plotconcommand = "plotcon -sformat msf "+taxon+"align.msf -winsize 4 -graph cps -goutfile "+taxon+"_plotcon"
    os.system(plotconcommand)

def aligninfofunc(taxon):
    #This generates a file with the alignment info for each protein
    import os
    infocommand = "infoalign "+taxon+"align.msf -outfile "+taxon+"_aligninfo.txt -only -heading -name -seqlength -idcount -simcount -diffcount -change"
    os.system(infocommand)

def prettyplotfunc(taxon):
    #pretty plot shows the alignments visually
    import os
    prettycommand = "prettyplot "+taxon+"align.msf -sformat1 msf -docolour -graph cps -goutfile "+taxon+"_prettyplot"
    os.system(prettycommand)

