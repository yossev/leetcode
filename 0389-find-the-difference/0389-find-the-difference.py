class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_sum = sum(ord(x) for x in s)
        t_sum = sum(ord(z) for z in t)

        # Return the ASCII Difference as a char ( Since each value has its own ascii value)
        return chr(t_sum - s_sum)