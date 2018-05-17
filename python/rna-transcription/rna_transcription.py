def to_rna(dna_strand):
    dna_to_rna_table = str.maketrans('GCTA', 'CGAU')

    return dna_strand.translate(dna_to_rna_table)
