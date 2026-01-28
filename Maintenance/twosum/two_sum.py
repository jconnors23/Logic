class Solution:
    def twoSum(self, nums, target):
        lookup = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in lookup:
                return [lookup[diff], i]
            else:
                lookup[nums[i]] = i
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