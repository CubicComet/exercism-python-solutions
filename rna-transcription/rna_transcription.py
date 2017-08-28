DNA = {"A", "C", "T", "G"}

TRANS = {"G": "C", "C":"G", "T":"A", "A":"U"}


def to_rna(dna):
    # Check validity - `difference` returns elements in dna not in DNA
    if set(dna).difference(DNA):
        return ""
    
    return "".join([TRANS[n] for n in dna])
