class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_sorted = ''.join(sorted(s))
        t_sorted = ''.join(sorted(t))

        return s_sorted == t_sorted
        
