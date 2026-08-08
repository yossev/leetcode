class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        temp_l = s[0]
        temp_r = s[len(s) - 1]
        l = 0
        r = len(s) - 1

        while (l < r):
            s[r] = temp_l
            s[l] = temp_r
            l+=1
            r-=1
            temp_l = s[l]
            temp_r = s[r]
        return s