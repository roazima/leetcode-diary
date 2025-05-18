# R Azima
# Time Complexity
# space complexity

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if (char in '({['):
                stack.append(char)
            elif (char in ')}]'):
                if not stack:
                    return False
                top = stack.pop()
                if char == ')' and top != '(':
                    return False
                if char == '}' and top != '{':
                    return False
                if char == ']' and top != '[':
                    return False
        return len(stack) == 0
    

if __name__ == "__main__":
    test_cases = [
        ("()"),
        ("()[]{}"),
        ("(]"),
        ("([])") 
    ]

    solver = Solution()
    for s in test_cases:
        result = solver.isValid(s)
        print(f"Input: '{s}' → Output: {result}")

      
