class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        s = "hello world'
        s.split() -> ["hello", "world"]
        '''
        words = s.split()

        result = ""
        # Combine the words in reverse order
        # Unless it is the last word, add space between words.
        for i in range(len(words)-1, -1, -1):
            if i != 0:
                result = result + words[i] + " "
            else:
                result = result + words[i]
        return result