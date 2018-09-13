"""exercism.io RNA-Transcription excercise."""

import string


def to_rna(dna_strand):
    """Translates the characters of an input string from an assumed DNA format,
    to their RNA counterparts"""
    dna_to_rna_table = string.maketrans('GCTA', 'CGAU')

    return dna_strand.translate(dna_to_rna_table)
