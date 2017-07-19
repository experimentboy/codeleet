class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        import re
        capitalized_word = word.capitalize()
        lowercase_only = re.search(r"[A-Z]", word) is None
        uppercase_only = re.search(r"[a-z]", word) is None
        if capitalized_word == word or word.islower(): return True
        else:
            if lowercase_only or uppercase_only : return True
            else: return False 
