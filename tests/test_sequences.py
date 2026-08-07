from sequence_utils.sequences import (
    gc_content,
    reverse_complement,
    find_kmers,
)


def test_gc_content():
    assert gc_content("GCGC") == 100


def test_reverse_complement():
    assert reverse_complement("ATGC") == "GCAT"


def test_find_kmers():
    assert find_kmers("ATGC", 2) == [
        "AT",
        "TG",
        "GC",
    ]
