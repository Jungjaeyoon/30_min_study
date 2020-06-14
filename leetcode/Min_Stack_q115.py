# 1st version
# 스스로 해보기, stack 이란 리스트를 만들고, append, pop, min, index를 사용하여 구현
"""
class MinStack:

    def __init__(self):
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
"""
""" 
leetcode user adamzjk의 방법
append, pop, top의 경우 단순히 list에 추가, pop만을 사용해도 각 위치에 대한 정보를 알 수 있음.
하지만 minstack()의 경우 해당 stack의 최소값을 찾아야 하는 문제이므로 모든 값을 추가하고 찾아야 하는 문제가 발생
그래서 이 유저의 경우 첫 번째 스택의 값이 추가될 때 부터 해당 값이 최저값인지를 비교하도록 함.
이 경우 minstack() 함수가 몇 번 호출되던 스택에 값이 추가된(push) 횟수만큼 1:1 비교를 하면 됨.
기존 내 방식의 경우 minstack이 호출될 때 마다 전체 리스트에서 최저값을 뽑아내는 계산을 진행하였기 때문에
push 수 * 각 경우 마다의 stack() count 만큼의 계산을 하기 때문에 더 느린 속도를 보임
실제로 릿코드 환경에서 약 7~8 배의 속도 차이를 보임
"""
class MinStack:

    def __init__(self):
        self.stack = [(-1, float('inf'))]

    def push(self, x):
        self.stack.append([x, min(x, self.stack[-1][1])])

    def pop(self):
        if len(self.stack) > 1: self.stack.pop()

    def top(self):
        if len(self.stack) == 1: return None
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]


