#!/bin/python3
def filterfunc(taxon):  #filterfunc('txid4890')
    seqdfnew = seqdf
    lengthfilter = input("would you like to filter by sequence length? (yes/no):")
    while lengthfilter.upper() != 'YES' and lengthfilter.upper() != 'NO':
        print("Answer not yes or no value")
        lengthfilter = input("would you like to filter by sequence length? (yes/no):")
    if lengthfilter.upper() == "YES":
        lengthcriteria = input("would you like to filter by sequence length maximum, minimum, or both?:")
        while lengthcriteria.upper() != 'MAXIMUM' and lengthcriteria.upper() != 'MINIMUM' and lengthcriteria.upper() != 'BOTH':
            print("Answer not one of the options")
            lengthcriteria = input("would you like to filter by sequence length maximum, minimum, or both?")
    if lengthcriteria.upper() == "MAXIMUM":
        seqdfnew = maxfunc()
    if lengthcriteria.upper() == "MINIMUM":
        seqdfnew = minfunc()
    if lengthcriteria.upper() == "BOTH":
        seqdfnew = maxfunc()
        seqdfnew = minfunc(seqdfnew)
    taxfilter = input("Would you like to filter by genera, species, both, or none?:")
    while taxfilter.upper() != 'GENERA' and taxfilter.upper() != 'SPECIES' and taxfilter.upper() != 'BOTH' and taxfilter.upper() != 'NONE':
        print("Answer not one of options: genera, species, both, or none")
        taxfilter = input("Would you like to filter by genera, species, both, or none?:")
    if taxfilter.upper() == 'GENERA':
        generafunc(lengthfilter.upper())
    if taxfilter.upper() == 'SPECIES':
        speciesfunc(lengthfilter.upper())
    if taxfilter.upper() == 'BOTH':
        taxfunc(lengthfilter.upper())
    if taxfilter.upper() == 'NONE':
        onlylengthfunc(lengthfilter.upper())








def maxfunc():
    maxlen = input("Maximum desired sequence length:")
    try:
        maxlen = int(maxlen)
    except ValueError:
        print("maximum length not an integer")
        maxlen = input("Maximum desired sequence length:")
        maxlen = int(maxlen)
    while maxlen > int(seqdf.describe().max()):
        print("Maximum length input is larger than any sequence in your results")
        print("The longest sequence in your results has a length of "+str(int(seqdf.describe().max())))
        maxlen = input("Maximum desired sequence length:")
        try:
            maxlen = int(maxlen)
        except ValueError:
            print("maximum length not an integer")
            maxlen = input("Maximum desired sequence length:")
            maxlen = int(maxlen)
    seqdfnew = seqdf[seqdf['SeqLength'] < maxlen]
    return(seqdfnew)



def minfunc(x):
    minlen = input("Minimum desired sequence length:")
    try:
        minlen = int(minlen)
    except ValueError:
        print("minimum length not an integer")
        minlen = input("Minimum desired sequence length:")
        minlen = int(minlen)
    while minlen < int(seqdf.describe().min()):
        print("Minimum length input is smaller than any sequence in your results")
        print("The shortest sequence in your results has a length of "+str(int(seqdf.describe().min())))
        minlen = input("Minimum desired sequence length:")
        try:
            minlen = int(minlen)
        except ValueError:
            print("minimum length not an integer")
            minlen = input("Minimum desired sequence length:")
            maxlen = int(minlen)
    seqdfnew = x[x['SeqLength'] > minlen]
    return(seqdfnew)



def generafunc(x):
    print(seqdfnew['Genus'].value_counts().to_string())
    print('These are the genera returned by your search')
    generastr = seqdfnew['Genus'].value_counts().to_string()
    print("Which genus or genera would you like to filter for? \n enter desired genera as Genus1 or Genus1,Genus2,GenusN:")
    genusin = input("Desired genus:")  #Penicillium,Wilcoxina
    genusinput = genusin.split(",")
    for genus in genusinput:
        while genus not in generastr:
            print ('Genus input: '+genus+' not in results')
            genusin = input("Desired genus:")
            genusinput = genusin.split(",")
            for genus in genusinput:
                genus = genus
    genuslabel = '_and_'.join(genusinput)
    if x == "YES":
        if lengthcriteria.upper() == "MINIMUM":
            lengthlabel = genuslabel+"_minlen"+str(minlen)
        if lengthcriteria.upper() == "MAXIMUM":
            lengthlabel = genuslabel+"_maxlen"+str(minlen)
        if lengthcriteria.upper() == "BOTH":
            lengthlabel = genuslabel+"_"+str(minlen)+"-"+str(maxlen)
    des_gen_df = seqdfnew[seqdfnew['Genus'].isin(genusinput)]
    des_gen_fa_df = des_gen_df.iloc[:, 3:5]
    des_gen_fa_df.to_csv("{}bad.fa".format(genuslabel), header=None, index=None, sep=' ')
    with open("{}bad.fa".format(genuslabel)) as file:
        new = ''
        for line in file:
            newline = line.replace("\"", '')
            new = new + newline
        with open("{}.fa".format(genuslabel),"w") as my_file:
             my_file.write(new)
    from whichanalyses import *
    whichanalysisfunc(genuslabel)


def speciesfunc(x):
    print(seqdfnew['Species'].value_counts().to_string())
    print('These are the species returned by your search')
    specstr = seqdfnew['Species'].value_counts().to_string()
    print("Which species would you like to filter for? \n enter desired species as Spescies1 or Spescies1,Spescies2,SpesciesN:")
    speciesin = input("Desired species:")  #ucsense
    speciesinput = speciesin.split(",")
    for species in speciesinput:
        while species not in specstr:
            print ('Species input: '+species+' not in results')
            speciesin = input("Desired species:")
            speciesinput = speciesin.split(",")
            for species in speciesinput:
                species = species
    specieslabel = '_and_'.join(speciesinput)
    if x == "YES":
        if lengthcriteria.upper() == "MINIMUM":
            lengthlabel = specieslabel+"_minlen"+str(minlen)
        if lengthcriteria.upper() == "MAXIMUM":
            lengthlabel = specieslabel+"_maxlen"+str(minlen)
        if lengthcriteria.upper() == "BOTH":
            lengthlabel = specieslabel+"_"+str(minlen)+"-"+str(maxlen)
    des_spec_df = seqdfnew[seqdfnew['Species'].isin(speciesinput)]
    des_spec_fa_df = des_spec_df.iloc[:, 3:5]
    des_spec_fa_df.to_csv("{}bad.fa".format(specieslabel), header=None, index=None, sep=' ')
    with open("{}bad.fa".format(specieslabel)) as file:
        new = ''
        for line in file:
            newline = line.replace("\"", '')
            new = new + newline
        with open("{}.fa".format(specieslabel),"w") as my_file:
             my_file.write(new)
    from whichanalyses import *
    whichanalysisfunc(specieslabel)


def taxfunc(x):
    print(seqdfnew['Taxon'].value_counts().to_string())
    print('These are the taxa returned by your search')
    taxstr = seqdfnew['Taxon'].value_counts().to_string()
    print("Which taxa would you like to filter for? \n enter desired taxa as Genus1 Spescies1 or Genus1 Spescies1,Genus2 Spescies2,GenusN SpesciesN:")
    print("For example, to filter for Penicillium brasilianum and Penicillium ucsense")
    print("Enter Penicillium brasilianum,Penicillium ucsense")
    taxin = input("Desired taxa:")
    taxinput = taxin.split(",")
    for taxa in taxinput:
        while taxa not in taxstr:
            print ('Taxa input: '+taxa+' not in results')
            taxin = input("Desired taxa:")
            taxinput = taxin.split(",")
            for taxa in taxinput:
                taxa = taxa
    taxlabel_intermediate = '_and_'.join(taxinput)
    taxlabel = taxlabel_intermediate.replace(' ', '-')
    if x == "YES":
        if lengthcriteria.upper() == "MINIMUM":
            lengthlabel = taxlabel+"_minlen"+str(minlen)
        if lengthcriteria.upper() == "MAXIMUM":
            lengthlabel = taxlabel+"_maxlen"+str(minlen)
        if lengthcriteria.upper() == "BOTH":
            lengthlabel = taxlabel+"_"+str(minlen)+"-"+str(maxlen)
    des_tax_df = seqdfnew[seqdfnew['Taxon'].isin(taxinput)]
    des_tax_fa_df = des_tax_df.iloc[:, 3:5]
    des_tax_fa_df.to_csv("{}bad.fa".format(taxlabel), header=None, index=None, sep=' ')
    with open("{}bad.fa".format(taxlabel)) as file:
        new = ''
        for line in file:
            newline = line.replace("\"", '')
            new = new + newline
        with open("{}.fa".format(taxlabel),"w") as my_file:
             my_file.write(new)
    from whichanalyses import *
    whichanalysisfunc(taxlabel)


def onlylengthfunc(x):
    if lengthfilter.upper() == "NO":
        print("You did not specified any filters to apply")
    if x == "YES":
        if lengthcriteria.upper() == "MINIMUM":
            lengthlabel = taxon+"_minlen"+str(minlen)
        if lengthcriteria.upper() == "MAXIMUM":
            lengthlabel = taxon+"_maxlen"+str(minlen)
        if lengthcriteria.upper() == "BOTH":
            lengthlabel = taxon+"_"+str(minlen)+"-"+str(maxlen)
        seqdfnew.to_csv("{}bad.fa".format(lengthlabel), header=None, index=None, sep=' ')
        with open("{}bad.fa".format(lengthlabel)) as file:
            new = ''
            for line in file:
                newline = line.replace("\"", '')
                new = new + newline
            with open("{}.fa".format(lengthlabel),"w") as my_file:
                 my_file.write(new)
        from whichanalyses import *
        whichanalysisfunc(lengthlabel)

