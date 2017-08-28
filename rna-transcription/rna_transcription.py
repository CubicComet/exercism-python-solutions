TRANS = {"G": "C", "C":"G", "T":"A", "A":"U"}


def to_rna(dna):
    try:
        return "".join([TRANS[n] for n in dna])
    except KeyError:
        return ""


# Old version: it's slightly slower for valid DNA, but slightly faster for invalid DNA

DNA = {"A", "C", "T", "G"}
TRANS = {"G": "C", "C":"G", "T":"A", "A":"U"}


def to_rna_old(dna):
    # Check validity - `difference` returns elements in dna not in DNA
    if set(dna).difference(DNA):
        return ""
    
    return "".join([TRANS[n] for n in dna])
