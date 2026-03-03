class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 1:
            return False
        for i in range(len(s)):
            # print(stack)
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
                continue
            elif s[i] == ')':
                if len(stack) == 0:
                    return False
                if stack[len(stack)-1] != '(':
                    return False
            elif s[i] == '}':
                if len(stack) == 0:
                    return False
                if stack[len(stack)-1] != '{':
                    return False
            elif s[i] == ']':
                if len(stack) == 0:
                    return False
                if stack[len(stack)-1] != '[':
                    return False
            stack.pop()
        if len(stack) == 0:
            return True
        return False

if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        ( ("()"), True), 
        ( ("()[]{}"), True), 
        ( ("(]"), False), 
        ("([])", True),
        ("([)]", False),
        ("(", False),
        ("){", False)
    ]

    
for inputs, expected in test_cases:
    actual = sol.isValid(*inputs) if isinstance(inputs, list) else sol.isValid(inputs)
        
    if actual == expected:
        print(f"✅ Pass | Result: {actual}")
    else:
        print(f"❌ Fail | Expected: {expected}, Got: {actual}")