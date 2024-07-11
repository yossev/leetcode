class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        open_parentheses_indices = collections.deque()
        result = []

        for curr in s:
             if curr == "(":
                open_parentheses_indices.append(len(result))
             elif curr == ")":
                start = open_parentheses_indices.pop()
                result[start:] = result[start:][::-1]
             else:
                result.append(curr)
        return "".join(result)
