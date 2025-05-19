#R Azima
# Loop through tokens and save the ints in a and b.
# Apply the operation on them, put the result back in the stack, and continue.
# Return the result that is saved in stack[0].
# Time Complexity: O(n), going through all values in the tokens list.
# Space Complexity: O(n), in the worst case (all values stored in stack).
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in '+-/*':
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    c = a + b
                    stack.append(c)
                if token == '-':
                    stack.append(a-b)
                if token == '/':
                    stack.append(int(a/b))
                if token == '*':
                    stack.append(a*b)  
            else:
                stack.append(int(token))
            
        return stack[0]

if __name__ == "__main__":
    sol = Solution()

    # Example test case: ["2", "1", "+", "3", "*"] → ((2 + 1) * 3) = 9
    tokens = ["2", "1", "+", "3", "*"]
    result = sol.evalRPN(tokens)
    print("Result:", result)
                        


            
