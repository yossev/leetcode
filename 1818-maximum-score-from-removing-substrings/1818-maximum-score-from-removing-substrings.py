class Solution(object):
    def maximumGain(self, s, x, y):
        def remove_pairs(s, first, second, gain):
            stack = []
            total_gain = 0
            for char in s:
                if char == second and stack and stack[-1] == first:
                    stack.pop()
                    total_gain += gain
                else:
                    stack.append(char)
            return ''.join(stack), total_gain
        
        if x > y:
            remaining_string, gain_ab = remove_pairs(s, 'a', 'b', x)
            final_string, gain_ba = remove_pairs(remaining_string, 'b', 'a', y)
        else:
            remaining_string, gain_ba = remove_pairs(s, 'b', 'a', y)
            final_string, gain_ab = remove_pairs(remaining_string, 'a', 'b', x)
        
        return gain_ab + gain_ba

# Simply remove the pairs with the higher priority first