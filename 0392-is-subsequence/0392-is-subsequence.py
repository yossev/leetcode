class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)> len(t):
             return False
        if len(s)==0:
            return True

        curr=0

        for i in range(len(t)):
            if s[curr] == t[i]:
                curr+=1
            if curr==len(s):
                return True
        return False
            
            
        