class Solution:
    def myAtoi(self, s: str) -> int:
        # Remove any leading spaces
        s = s.lstrip()
        if not s: return 0
        i = 0
        sign = 1
        # Read the sign, or if we don't have sign, move on
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i += 1

        # Num will accumulate our result
        num = 0

        # Once we read a non-digit, break
        while i < len(s):
            cur = s[i]
            if not cur.isdigit():
                break
            else:
                num = num * 10 + int(cur)
            i += 1

        # Apply the sign
        num *= sign

        # If number too big or too small, round.
        if num > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif num <= -2 ** 31:
            return -2 ** 31
        return num