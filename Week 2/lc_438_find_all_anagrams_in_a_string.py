from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []

        s_count = Counter()
        # Initialize character count for p
        p_count = Counter(p)
        # "abc" -> {'a': 1, 'b': 1, 'c': 1}

        result = []

        for i in range(ns):
            # Add a letter on the right side of the window
            s_count[s[i]] += 1

            # Remove a letter from the left side of the window
            if i >= np:
                # Remove the key entirely if it is going to be 0 after
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    s_count[s[i - np]] -= 1
            # We have a match for anagrams
            if p_count == s_count:
                # Append the index to results
                result.append(i - np + 1)
        return result