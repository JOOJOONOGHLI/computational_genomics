"""
This is a short progrmaming assignment to help you get familiar with the Python
programming language! If you are comfortable with writing code to solve these,
then you should be able to complete the rest of the assignments in this course
without too much difficulty.

We have provided a few functions for you to fill in with your implementation.
For each, please see the docstring (within triple quotes) for a detailed
explanantion of what to do. The docstring also contains doctests preceded by
triple carrots >>>. These are examples of expected outputs for the function.
These doctests are automatically run in the main() function; you can feel free
to add more tests yourself. For reference, each of these can be implemented in
less than 20 lines of code without importing libraries (even built-in ones).
Some of these may have easily-searchable solutions online, or may be correctly
auto-completed by Github Copilot, but we encourage you to take this opportunity
and try to implement them yourself to get an idea of whether or not you are
ready to complete the rest of the assignments in this course.

For this assignment, you are not allowed to import any non-standard libraries.
For example, you may not use numpy, pandas, biotite, or biopython. You may use
standard libraries such as collections and math.
"""


def mean_or_median(x):
    """
    This function should take in a list of numbers (i.e., an 'array' x), and
    compute the output according to the following rules:
    * If the list of numbers is empty, return 0.
    * If the length of the list is odd, return the median of the list.
    * If the length of the list is even, return the mean of the list.

    >>> mean_or_median([3, 1, 2])
    2
    >>> mean_or_median([1, 2, 3, 4])
    2.5
    >>> mean_or_median([])
    0
    >>> mean_or_median([5, 2, 1, 3, 4])
    3
    >>> mean_or_median([99])
    99
    """
    sorted_list = sorted(x)
    length = len(x)
    if length == 0:
        return 0
    if length % 2 == 1:
        med_index = length//2
        return sorted_list[med_index]
    if length%2 == 0:
        sum = 0
        for elem in sorted_list:
            sum += elem
        return sum/length
        


def cosine_sim(x, y):
    """
    This function should take in two lists of numbers x and y and return the
    cosine similarity (https://en.wikipedia.org/wiki/Cosine_similarity). Cosine
    similarity is a measure of similarity between two vectors and is calculated
    by taking the dot product of the two vectors and dividing it by the product
    of the magnitudes of the two vectors.

    Note: this function is much easier to implement (and faster to run) when
    using external libraries such as numpy. However, for this assignment, you
    should use standard Python.

    >>> cosine_sim([1, 2, 3], [2, 4, 6])
    1.0
    >>> cosine_sim([1, 0], [0, 1])
    0.0
    >>> cosine_sim([4, 0, 4], [0, 9, 0])
    0.0
    >>> cosine_sim([1, 2, 3], [1, 2, 3])
    1.0
    """
    def dot(x, y):
        dp_sum = 0
        if len(x) == len(y):
            for i in range(len(x)):
                dp_sum += x[i] * y[i]
        return dp_sum
    def magnitude(x):
        sq_sum = 0
        for i in range(len(x)):
            current_q = (x[i])**2
            sq_sum += current_q 
        return sq_sum**(0.5)
    return dot(x,y) / (magnitude(x)*magnitude(y))


def english_to_pig_latin(word):
    """
    The "Pig Latin" language (https://en.wikipedia.org/wiki/Pig_Latin) is a
    modification of the English language where each English word is transformed
    into its Pig Latin equivalent according to two simple rules:
    * If a word starts with one or more consonants, then the initial set of
      (contiguous) consonants is moved to the end of the word, followed by the
      suffix "ay". For example, the word "friends" becomes" "iendsfray".
    * If a word starts with one or more vowels, then the suffix "ay" is added.
      For example, the word "apple" becomes "appleay".
    This function translates a single word from English to Pig Latin according
    to these rules. The output should be lower case, regardless of the casing
    of the input. If the input string is empty, return an empty string. You are
    not expected to handle the case where multiple words are given as input, or
    the case where the word includes punctuation.

    >>> english_to_pig_latin("apple")
    'appleay'
    >>> english_to_pig_latin("friends")
    'iendsfray'
    >>> english_to_pig_latin("hello")
    'ellohay'
    >>> english_to_pig_latin("world")
    'orldway'
    >>> english_to_pig_latin("hmm")
    'hmmay'
    """
    def first_to_last(word):
        word_copy = word
        first_letter = word_copy[0]
        remaining = word_copy[1:]
        return remaining + first_letter
    def isVowel(letter):
        if letter == 'a':
            return True
        if letter == 'e':
            return True
        if letter == 'i':
            return True
        if letter == 'o':
            return True
        if letter == 'u':
            return True
        else:
            return False
    word_copy = word.lower()
    if word_copy == '':
        return ''
    if isVowel(word_copy[0]):
        return word_copy + 'ay'
    for i in range(len(word)):
        if not isVowel(word[i]):
            word_copy = first_to_last(word_copy)
        elif isVowel(word[i]):
            break
    return word_copy + 'ay'


    


def is_anagram(x, y):
    """
    This function should take in two strings x and y and return whether they are
    anagrams of each other (i.e., returning boolean literals True or False). Two
    words are anagrams if they contain the same letters in the same quantities
    but potentially with a different ordering. Ignore casing when determing this.

    >>> is_anagram('abc', 'cba')
    True
    >>> is_anagram('abc', 'abc')
    True
    >>> is_anagram('abc', 'ab')
    False
    >>> is_anagram('aaaz', 'azaa')
    True
    """
    dict1 = {}
    dict2 = {}
    x = x.lower()
    y = y.lower()
    for i in range(len(x)):
        if x[i] in dict1:
            dict1[x[i]] += 1
        else:
            dict1[x[i]] = 1
    for i in range(len(y)):
        if y[i] in dict2:
            dict2[y[i]] += 1
        else:
            dict2[y[i]] = 1
    if dict1 == dict2:
        return True
    else:
        return False


def reverse_complement(s):
    """
    This function should take in a string s and return the reverse complement of
    that string. This code should be agnostic of the casing of the input - i.e.,
    the inputs 'AcGG' and 'acGg' should both return 'CCGT'. However, if the input
    contains characters that are not in the canonical alphabet of DNA bases, then
    it should raise an error (it does not matter what error is raised).

    This is intended to give you a bit of practice with string manipulations in
    Python.

    >>> reverse_complement('ACGT')
    'ACGT'
    >>> reverse_complement('AAAA')
    'TTTT'
    >>> reverse_complement("GCAGT")
    'ACTGC'
    """
    result = ''
    def assign_letter(letter):
        if letter == 'a' or letter == 'A':
            return 'T'
        elif letter == 't' or letter == 'T':
            return 'A'
        elif letter == 'g' or letter == 'G':
            return 'C'
        elif letter == 'c' or letter == 'C':
            return 'G'
    for i in range(len(s)-1, -1, -1):
        result += assign_letter(s[i])
    return result



def is_balanced_brackets(s):
    """
    Consider the bracket notation over the alphabet '(', ')', and '-'. In this
    scheme, we define a balanced string to be one where every opening bracket
    corresponds to a closing bracket. For example, the string '(()())' is a
    correctly balanced string. The string '(()' is not balanced, as there is no
    closing bracket for the opening bracket at the start of a string. The string
    ')(' is also not balanced.

    This function should take in a string s and return whether or not it is a
    correctly balanced string (i.e., returning boolean literals True or False).

    >>> is_balanced_brackets('')
    True
    >>> is_balanced_brackets('()')
    True
    >>> is_balanced_brackets('()()')
    True
    >>> is_balanced_brackets('(())')
    True
    >>> is_balanced_brackets('(()())')
    True
    >>> is_balanced_brackets('(()')
    False
    >>> is_balanced_brackets(')(')
    False
    """
    current_total = 0
    for i in range(len(s)):
        if s[i] == '(':
            current_total += 1
        elif s[i] == ')':
            current_total -= 1
        if current_total < 0:
            return False
    if current_total == 0:
        return True
    elif current_total > 0:
        return False




def main():
    """Runs the doctests (as indicated by >>> in docstrings)"""
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    main()