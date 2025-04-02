class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curNum = 0
        curString = ""

        for c in s:
            if c == '[':
                stack.append(curString) # Save curString and curNum into stack
                stack.append(curNum)
                curString = '' # reset curString and curNum
                curNum = 0
            elif c == ']':
                num = stack.pop() # We are done with this section, start generating
                prevString = stack.pop()
                curString = prevString + num*curString # add curString n times to prev
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString