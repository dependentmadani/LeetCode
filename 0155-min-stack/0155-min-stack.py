class MinStack:

    def __init__(self):
        self.values = []

    def push(self, val: int) -> None:
        self.values.append(val)

    def pop(self) -> None:
        self.values.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return min(self.values)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
