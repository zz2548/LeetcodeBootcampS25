class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True # Out of bound, base case

        # Work from last position to the beginning
        for i in range(len(s) - 1, -1, -1):
            # We will check each word
            for w in wordDict:
                # Do we have enough characters in s?
                # And do we have from position i to i + len(w) the word w
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]: # We can move on to the next index
                    break
        return dp[0] # Stores the result in dp[0]
