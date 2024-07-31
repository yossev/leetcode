from collections import deque

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = deque()

        for char in s:
            stack.append(char)

        result_stack = deque()

        while stack:
            curr = stack.popleft()
            if curr == '*':
                if result_stack:
                    result_stack.pop()
            else:
                result_stack.append(curr)

        return ''.join(result_stack)
