class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        s = ["a"]

        while len(s) < k:
            ns = []
            for c in s:
                ns.append(chr(ord(c)+1))
            s.extend(ns)
        return s[k-1]

            
