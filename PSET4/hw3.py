"""
For this homework, you will be allowed to use numpy and matplotlib
in addition to all packages in the standard library. You are NOT allowed to use
other packages such as seaborn or pandas.

We recommend that you install these packages in a virtual environment, such as
conda. To do so, first download and install conda from the instructions at:
https://docs.conda.io/projects/conda/en/latest/commands/install.html
Following this, you can create a new environment with the following command:
> conda create -n cs173a python=3.8 numpy=1.23 matplotlib -c anaconda -c conda-forge -c bioconda

After the command finishes, you can activate the environment with:
> conda activate cs173a

This ensures that you are running the same set of packages as the autograder is
running to avoid any possible issues with different package versions.

Alternatively, you can install these packages in your system-wide python using
the following commands:
> pip install numpy
> pip install matplotlib
> pip install biotite
Note that we do not guarantee that you won't run into errors with this method.

Note that some of the function definitions in this file contain type signatures
(requires Python >= 3.5; see https://docs.python.org/3.7/library/typing.html).
These are included to help you understand the expected input and output types.
If you insist on running a version of Python < 3.5, you can remove these type
hints by simply removing the "types" that occur after the ":" character in the
parameter list, and the --> type that occurs after the function definition.
"""
import os, sys
import logging
from typing import List, Tuple  # For type hinting

import numpy as np
from matplotlib import pyplot as plt  # For plotting
import matplotlib.ticker as mticker  # Consider using this for plotting

BASES = "ATCG"
COMPLEMENTS = {"A": "T", "T": "A", "C": "G", "G": "C", "N": "N"}


def read_singular_fasta(filename: str) -> str:
    """
    Assuming a fasta file has only a single entry, read in the sequence
    (without header information). Errors out if there are multiple sequences.

    This is provided for you as a convenience function.
    """
    has_header = False
    lines = []
    for line in open(filename):
        if line.startswith(">"):
            if has_header:
                raise NotImplementedError
            has_header = True
            continue
        lines.append(line.strip())
    retval = "".join(lines)
    assert set(retval) <= set(BASES)
    logging.info(f"Read in {len(retval)} bases from {filename}")
    return retval


def rev_comp(sequence: str):
    """
    Return the reverse complement of the given sequence. This function is
    implemented for you.

    >>> rev_comp("ATCG")
    'CGAT'
    """
    return "".join([COMPLEMENTS[base] for base in sequence[::-1]])


def build_pfm(sequences: List[str]) -> np.ndarray:
    """
    Build a position frequency matrix (PFM) from a list of sequences. You must
    return a numpy array of shape (4, L) where L is the length of the sequences.
    Each row of this array should correspond to the bases ATCG, in that order.
    The numpy array should be of type int to avoid rounding issues with the
    autograder.

    Note that you should NOT yet add a psuedocount to these counts.

    Parameters
    ----------
    sequences : list of str
        A list of sequences of length L

    Returns
    -------
    pfm : numpy.ndarray, shape=(4, L)
        The position frequency matrix of the sequences.

    ** This function will be tested by the autograder **
    """
    for sequence in  sequences:
        


def pfm2ppm(pfm: np.ndarray, pseudocount: float = 0.5) -> np.ndarray:
    """
    Convert a position frequency matrix (PFM) to a position probability matrix
    (PPM). You must return a numpy array of shape (4, L) with the same ordering
    of rows and columns as the input PFM. As before, each row of this array
    should correspond to the bases ATCG, in that order. The numpy array should
    be of type float to avoid rounding issues with the autograder.

    This is where we add a psuedocount to the PFM, of 0.5. The output should NOT
    be log-scaled.

    Parameters
    ----------
    pfm : numpy.ndarray, shape=(4, L)
        The position frequency matrix of the sequences.

    Returns
    -------
    ppm : numpy.ndarray, shape=(4, L)
        The position probability matrix of the sequences.

    ** This function will be tested by the autograder **
    """
    raise NotImplementedError


def score_sequence(sequence: str, ppm: np.ndarray) -> float:
    """
    Score the given sequence and return the float score. The length of the
    sequence should match the number of columns (i.e., L) of the PPM. This
    function only considers this specific ppm applied to the specific
    sequence; do not consider the reverse complement or any frame shifts.

    Parameters
    ----------
    sequence : str, length L
        The DNA sequence to score, of length L
    ppm : numpy.ndarray, shape=(4, L)
        The position probability matrix to use to score

    Returns
    -------
    score : float
        The score of the sequence

    ** This function will be tested by the autgrader **
    """
    raise NotImplementedError


def consensus_seq_from_ppm(ppm: np.ndarray) -> str:
    """
    Given a PPM, return the consensus sequence as a string. Assume that the rows
    of the PPM are arranged in the order ATCG.

    ** This function will NOT be bested by the autograder but will be useful
    for the written part of the homework **
    """
    raise NotImplementedError


def slide_ppm_across_seq(sequence, ppm: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    "slide" the PPM across the sequence, scoring each consecutive subsequence
    in the sequence that matches the length of the given ppm. Do this for both
    the + strand (i.e., the given sequence) and the - strand (i.e., the reverse
    complement of the input). Your return value should be a tuple of arrays
    where the first array corresponds to the scores for the + strand, and the
    second array corresponds to scores for the reverse complement - strand.

    Hint: you can call to score_sequence that you wrote above while
    implementing this.

    Parameters
    ----------
    sequence : str
        The DNA sequence to score, of arbitrary length
    ppm : numpy.ndarray, shape=(4, L)
        The position probability matrix to use to score

    Returns
    -------
    scores : tuple of numpy.ndarray
        A tuple of numpy arrays, where the first array corresponds to the
        scores for the given (positive strand) sequence, and the second array
        corresponds to the scores for the reverse complement.

    ** This function will be tested by the autograder **
    """
    raise NotImplementedError


def plot_scores(
    plus_scores: np.ndarray,
    minus_scores: np.ndarray,
    match_len: int,
    full_seq: str,
    threshold: float = -7.5,
    fname: str = "scores.pdf",
    **kwargs,
):
    """
    Plot the scores for the sequences in the file. The set of arguments
    provided here is merely a suggestion; you may change the inputs/output
    arguments as you see fit, as this function is not subject to the
    autograder.

    ** This function will NOT be graded by the augrader but you will need
    to write it to complete the homework assignment **
    """
    assert threshold <= 0
    assert match_len > 0
    assert np.all(plus_scores <= 0) and np.all(minus_scores <= 0)
    ### YOUR CODE HERE
    raise NotImplementedError


def do_toy_example():
    """
    Do the toy example from the homework handout. If you run this function
    with all your functions correctly implemented, it should reproduce all
    the numbers and plots from the handout.

    ** This function will NOT be graded by the autograder **
    """
    full_seq = "ACCGGTAC"
    toy_sequences = [
        "ACCCG",
        "ACCCT",
        "ACGCA",
        "ATGCT",
        "CCGAT",
        "TCGCT",
    ]
    pfm = build_pfm(toy_sequences)
    ppm = pfm2ppm(pfm)
    logging.info(f"Consensus sequence: {consensus_seq_from_ppm(ppm)}")
    plus_scores, minus_scores = slide_ppm_across_seq(full_seq, ppm)
    # The reference solution chooses to implement the plotting
    # code to take in both arrays of scores; you may choose to
    # implement this differently. Your plotting code will NOT be
    # graded by the autograder, so as long as it can create plots
    # in teh format requested, your specfic API does not matter.
    # Thus, feel free to change this function call below as needed.
    plot_scores(
        plus_scores,
        minus_scores,
        match_len=ppm.shape[1],  # Number of columns
        full_seq=full_seq,
        threshold=-2.7,
    )


def ppm_from_motif_file(fname: str) -> np.ndarray:
    """
    Read in the given filename, which contains a series of sequences
    of equal length. Take the sequences and construct a PPM.

    ** This function will NOT be tested by the autograder but you may find
    it useful to have when running your homework on the input file **
    """


if __name__ == "__main__":
    # You may change any of the code in this chunk (until EOF). The existing
    # code is provided for some cosmetic benefits, and for running doctests

    # So we can call logging.info() without the typical prefix of "INFO:root:" being displayed
    # https://stackoverflow.com/questions/8353594/can-python-log-output-without-inforoot
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    # Sets the print options such that numpy arrays are printed with 2 decimal places
    # https://stackoverflow.com/questions/22222818/how-to-print-numpy-array-with-3-decimal-places
    np.set_printoptions(formatter={"float": lambda x: "{0:0.2f}".format(x)})
    import doctest

    doctest.testmod()
    if len(sys.argv) == 1:
        do_toy_example()
    else:
        pass
