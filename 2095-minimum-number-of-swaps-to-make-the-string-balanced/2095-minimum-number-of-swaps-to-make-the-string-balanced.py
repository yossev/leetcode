class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []

        unbalanced = 0

        for char in s:
            if char == "[":
                stack.append(char)
            elif char == "]":
                if stack:
                    stack.pop()
                else:
                    unbalanced+=1

        return (unbalanced + 1) // 2

        

