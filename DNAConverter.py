def strandtwo(nucleotide):
    strand = ""
    if nucleotide == "A":
        strand += "T"
    elif nucleotide == "C":
        strand += "G"
    elif nucleotide == "G":
        strand += "C"
    elif nucleotide == "T":
        strand += "A"
    return strand


def dnamrna(nucleotide):
    strand = ""
    if nucleotide == "A":
        strand += "A"
    elif nucleotide == "C":
        strand += "C"
    elif nucleotide == "G":
        strand += "G"
    elif nucleotide == "T":
        strand += "U"
    return strand


def dnatrna(nucleotide):
    strand = ""
    if nucleotide == "A":
        strand += "U"
    elif nucleotide == "C":
        strand += "G"
    elif nucleotide == "G":
        strand += "C"
    elif nucleotide == "T":
        strand += "A"
    return strand


def trnamrna(nucleotide):
    strand = ""
    if nucleotide == "U":
        strand += "A"
    elif nucleotide == "C":
        strand += "G"
    elif nucleotide == "G":
        strand += "C"
    elif nucleotide == "A":
        strand += "U"
    return strand


def trnadna(nucleotide):
    strand = ""
    if nucleotide == "A":
        strand += "T"
    elif nucleotide == "C":
        strand += "G"
    elif nucleotide == "G":
        strand += "C"
    elif nucleotide == "U":
        strand += "A"
    return strand


def trnadnatwo(nucleotide):
    strand = ""
    if nucleotide == "A":
        strand += "A"
    elif nucleotide == "C":
        strand += "C"
    elif nucleotide == "G":
        strand += "G"
    elif nucleotide == "U":
        strand += "T"
    return strand


def mrnadna(nucleotide):
    strand = ""
    if nucleotide == "A":
        strand += "A"
    elif nucleotide == "C":
        strand += "C"
    elif nucleotide == "G":
        strand += "G"
    elif nucleotide == "U":
        strand += "T"
    return strand


def mrnatrna(nucleotide):
    strand = ""
    if nucleotide == "A":
        strand += "U"
    elif nucleotide == "C":
        strand += "G"
    elif nucleotide == "G":
        strand += "C"
    elif nucleotide == "U":
        strand += "A"
    return strand


def mrnadnatwo(nucleotide):
    strand = ""
    if nucleotide == "A":
        strand += "T"
    elif nucleotide == "C":
        strand += "G"
    elif nucleotide == "G":
        strand += "C"
    elif nucleotide == "U":
        strand += "A"
    return strand


choice = input("What type of data will you be converting?\n1 - DNA\n2 - mRNA\n3 - tRNA\nEnter a number(1-3):")
strand = ""
mrna = ""
trna = ""
dna = ""
while True:
    if choice == '1':
        dna = input("Enter the DNA strand you'd like to convert(no dashes):").upper().strip()

        for nucleotide in dna:
            strand += strandtwo(nucleotide)
            mrna += dnamrna(nucleotide)
            trna += dnatrna(nucleotide)

        print("Your original DNA strand: " + dna)
        print("2nd strand of DNA: " + strand)
        print("mRNA strand: " + mrna)
        print("tRNA strand: " + trna)
        break

    elif choice == '2':
        mrna = input("Enter the mRNA strand you'd like to convert(no dashes):").upper().strip()

        for nucleotide in mrna:
            dna += mrnadna(nucleotide)
            strand += mrnadnatwo(nucleotide)
            trna += mrnatrna(nucleotide)

        print("DNA strand: " + dna)
        print("2nd strand of DNA: " + strand)
        print("Your original mRNA strand: " + mrna)
        print("tRNA strand: " + trna)
        break

    elif choice == '3':
        trna = input("Enter the tRNA strand you'd like to convert(no dashes):").upper().strip()

        for nucleotide in trna:
            mrna += trnamrna(nucleotide)
            dna += trnadna(nucleotide)
            strand += trnadnatwo(nucleotide)

        print("DNA strand: " + dna)
        print("2nd strand of DNA: " + strand)
        print("mRNA strand: " + mrna)
        print("Your original tRNA strand: " + trna)
        break

    else:
        choice = input("Not a valid entry. Try again.\nWhat type of data will you be converting(1-3)?\n1 - DNA\n2 - mRNA\n3 - tRNA"
              "\nEnter a number(1-3):")


