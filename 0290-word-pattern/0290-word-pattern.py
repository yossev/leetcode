from itertools import zip_longest

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()  # Step 1: Split the string into words
        return (len(set(pattern)) ==   # Step 2: Unique characters in pattern
                len(set(s)) ==        # Step 3: Unique words in s
                len(set(zip_longest(pattern, s))))  # Step 4: Unique character-word pairs
