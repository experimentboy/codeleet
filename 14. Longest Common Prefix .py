class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        from itertools import takewhile,izip
        def equal(x):
            return len(set(x)) == 1
        long = "".join([i[0] for i in takewhile(equal ,izip(*strs))])
        return long
