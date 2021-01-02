test = "ACAAAACTGAGGGCTTCTATT"
code = input("Bitte die RNA - Sequenz Eingeben:")

newcode = ""

# 
for i in code:
    # T > A
    if (i == "T"):
        newcode = newcode + "A"
    # G > C
    elif (i == "G"):
        newcode = newcode + "C"
    # C > G
    elif (i == "C"):
        newcode = newcode + "G"
    # A > U
    elif (i == "A"):
        newcode = newcode + "U"
    else:
        print("Error")

aminosäure = ""
for i in range(0, len(newcode), 3):
    dreierDNA = newcode[i:i+3]
    if dreierDNA == "AUG":
        aminosäure = aminosäure + "SER" + " "
    elif dreierDNA == "CGC":
        aminosäure = aminosäure + "ARG" + " "
    elif dreierDNA == "UGU":
        aminosäure = aminosäure + "Cys " + " "
    elif dreierDNA == "UUU":
        aminosäure = aminosäure + "Phe " + " "
    elif dreierDNA == "GAC":
        aminosäure = aminosäure + "Asp " + " "
    elif dreierDNA == "UCC":
        aminosäure = aminosäure + "Ser " + " "
    elif dreierDNA == "CGA":
        aminosäure = aminosäure + "Arg " + " "
    elif dreierDNA == "AGA":
        aminosäure = aminosäure + "Arg " + " "
    elif dreierDNA == "UAA":
        aminosäure = aminosäure + "Stopp" + " "
    elif dreierDNA == "GAC ":
        aminosäure = aminosäure + "ARG" + " "
    else:
        break


print("Die Veränderte RNA sequenz:", newcode)
print("Die Aminosäurensequenz:", aminosäure)

        
