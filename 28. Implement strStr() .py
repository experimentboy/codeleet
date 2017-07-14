class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) >= len(needle):
            if len(haystack) == len(needle):
                out = haystack.find(needle)
            else:
                out = haystack.find(needle)
        else:
            out = -1
        return out
