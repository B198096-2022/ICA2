#Just defining this function that I will end up using in the pipeline :)
def motiffunc(taxon):
    headercommand = "grep '>' "+taxon+".fa > headers.txt"
    seqscommand = "awk '/^>/ { print '_'; next; }; {print; }' "+taxon+".fa > seqs.txt"
    os.system(headercommand)
    os.system(seqscommand)
    with open("headers.txt") as file:
        headers = file.read()
    with open("seqs.txt") as file:
        seqs = file.read()
    seqlist1 = seqs.split("\n\n")
    seqstr = " \n".join(seqlist1)
    seqlist = seqstr.split(" ")
    headerlist = headers.split("\n")
    if seqlist[0] == '':
        seqlist = seqlist[1:] #This DOES cut off first empty space
    if seqlist[-1] == '':
        seqlist = seqlist[0:-1] #This does nothing
    if headerlist[0] == '':
        headerlist = headerlist[1:] #This does nothing
    if headerlist[-1] == '':
        headerlist = headerlist[0:-1] #This cuts off the final empty space
    dictlen = len(seqlist)
    seqdict = {}
    seqdict[headerlist[0]] = seqlist[0]
    for i in range(dictlen):
        seqdict[headerlist[i]] = seqlist[i]
    #Thinking I'll need to make an actual fasta file and then read in the file
    os.mkdir("./"+taxon+"_patmatmotifs")
    os.mkdir("./"+taxon+"_indifasta")
    for head, seq in seqdict.items():
        fasta = head+seq
        headline = head.split()
        code = (headline[0])
        code = code[1:-2]
        print("Identifying motifs for "+head)
        with open("{}.fa".format(code),"w") as my_file:
             my_file.write(fasta)
        command = "patmatmotifs -full -sequence "+code+".fa -sprotein1 YES -sformat1 fasta -outfile "+code+".patmatmotifs"
        os.system(command)
        shutil.move("./"+code+".patmatmotifs", "./"+taxon+"_patmatmotifs/"+code+".patmatmotifs")
        shutil.move("./"+code+".fa", "./"+taxon+"_indifasta/"+code+".fa")
