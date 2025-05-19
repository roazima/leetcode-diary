class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.x = x
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop(0)

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        while self.stack: 
            return False
        return True

if __name__ == "__main__":
    obj = MyQueue()
    obj.push(10)
    obj.push(20)
    param_2 = obj.pop()
    param_3 = obj.peek()
    print("obj:", obj.peek())
    param_4 = obj.empty()
    print("obj:", obj.empty())



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()