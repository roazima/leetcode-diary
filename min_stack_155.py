class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        min_val = float('inf')
        for value in self.stack:
            if value < min_val:
                min_val = value
        return min_val


if __name__ == "__main__":
    obj = MinStack()
    obj.push(5)
    obj.push(3)
    obj.push(7)
    print("Top:", obj.top())         # Expect 7
    print("Min:", obj.getMin())      # Expect 3
    obj.pop()
    print("Top after pop:", obj.top())  # Expect 3
    print("Min after pop:", obj.getMin())  # Expect 3
