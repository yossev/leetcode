class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        # string length after removing all 'AB' and 'CD' from the string

        stack = [] 


        for curr in s:
            if not stack:
                stack.append(curr)
                continue

            if curr == "B" and stack[-1] == "A":
                stack.pop()
            elif curr  == "D" and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(curr)

        return len(stack)