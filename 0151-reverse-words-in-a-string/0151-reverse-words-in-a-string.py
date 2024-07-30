class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()  # Split the string into words
        reversed_words = words[::-1]  # Reverse the list of words
        reversed_sentence = ' '.join(reversed_words)  # Join the reversed list back into a string
        return reversed_sentence