class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        # If we have content in the first stack, put it in the second stack for now
        while self.s1:
            self.s2.append(self.s1.pop())
        # Push the item we want into the queue, which will be at the bottomp of the stack, last position in the queue
        self.s1.append(x)
        # Add everything back to s1, which now will be our queue in reverse.
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        # Return first item in queue, this is O(1)
        return self.s1.pop()

    def peek(self) -> int:
        # Peek at first item in queue
        return self.s1[-1]

    def empty(self) -> bool:
        # If s1 is empty then queue is empty.
        return not self.s1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()