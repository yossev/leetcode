class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = deque()

        for ast in asteroids:
            while stack and stack[-1] > 0 > ast:
                if ast > 0:
                    stack.append(ast)
                else:
                    if stack[-1] < -ast:
                        stack.pop()
                        continue
                    elif stack[-1] == -ast:
                        stack.pop()
                    break
            else:
                stack.append(ast)

        return stack
                    