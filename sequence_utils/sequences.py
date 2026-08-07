def gc_content(sequence):
    """Return GC content as a percentage."""

    sequence = sequence.upper()

    gc = sequence.count("G") + sequence.count("C")

    return gc / len(sequence) * 100


def reverse_complement(sequence):
    """Return the reverse complement of a DNA sequence."""

    complement = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C",
    }

    return "".join(complement[base] for base in sequence[::-1])


def find_kmers(sequence, k):
    """Return all k-mers of length k."""

    return [
        sequence[i:i+k]
        for i in range(len(sequence) - k)
    ]
