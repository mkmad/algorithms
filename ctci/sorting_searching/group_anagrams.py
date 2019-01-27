class Anagrams(object):

    """
    Write a method to sort an array of strings so that all the
    anagrams are next to each other

    Sol:

    using a hash table which maps from the sorted version of a
    word to a list of its anagrams. So, for example, acre will
    map to the list {acre, race, care}. Once we've grouped
    all the words into these lists by anagram, we can then put
    them back into the array.

    """