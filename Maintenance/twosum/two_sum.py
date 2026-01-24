class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            temp = nums[i]
            for j in range(len(nums)):
                if temp + nums[j] == target and i != j:
                    indices = [i, j]
                    return indices
        pass

if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        (([2,7,11,15], 9), [0, 1]),
        (([3,2,4], 6), [1, 2]),
        (([3,3], 6), [0, 1]),
        (([0,0], 0), [0, 1]),
    ]
    
    for inputs, expected in test_cases:
        actual = sol.twoSum(*inputs) if isinstance(inputs, tuple) else sol.twoSum(inputs)
            
        if actual == expected:
            print(f"✅ Pass | Result: {actual}")
        else:
            print(f"❌ Fail | Expected: {expected}, Got: {actual}")