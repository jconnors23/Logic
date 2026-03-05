class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        vals = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        if (len(s) <= 1) or vals.get(s[0]) is not None: return False
        for i in range(len(s)):
            if not vals.get(s[i]): # if curr char not key in vals i.e. curr char is an opener
                stack.append(s[i])
            else:
                if len(stack) == 0: return False
                elif stack[len(stack) -1] != vals.get(s[i]): # if the top of stack i.e. most recent opener does not correspond to the current closer char
                    return False
                else:
                    stack.pop()
        return len(stack) == 0

if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        ( ("()"), True), 
        ( ("()[]{}"), True), 
        ( ("(]"), False), 
        ("([])", True),
        ("([)]", False),
        ("(", False),
        ("){", False),
        ("((", False),
        ("(){}}{", False)

    ]

    
for inputs, expected in test_cases:
    actual = sol.isValid(*inputs) if isinstance(inputs, list) else sol.isValid(inputs)
        
    if actual == expected:
        print(f"✅ Pass | Result: {actual}")
    else:
        print(f"❌ Fail | Expected: {expected}, Got: {actual}")