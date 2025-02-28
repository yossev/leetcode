class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        maga_hash =  Counter(magazine)

        for c in ransomNote:
            if c not in maga_hash or maga_hash[c] <= 0:
                return False # We Ran out of letters to give
            maga_hash[c]-=1
        return True  