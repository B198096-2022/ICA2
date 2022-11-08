#!/bin/python3
import os
taxon = "txid4890"

clustercommand = "clustalo -i "+taxon+".prot.fa -threads=16 -t protein --outfmt=msf -o "+taxon+"align.msf"
os.system(clustercommand)

plotconcommand = "plotcon -sformat msf "+taxon+"align.msf -graph cps" 
os.system(plotconcommand)
