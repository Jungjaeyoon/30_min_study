# 1st version
# 스스로 해보기, stack 이란 리스트를 만들고, append, pop, min, index를 사용하여 구현
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
