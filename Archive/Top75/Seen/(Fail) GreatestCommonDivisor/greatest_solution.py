# LeetCode 1071: Greatest Common Divisor of Strings
# 
# Problem: For two strings s and t, we say "t divides s" if and only if 
# s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
#
# Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
#
# Example 2:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
#
# Example 3:
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
#
# Constraints:
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Find the greatest common divisor (GCD) string that divides both str1 and str2.
        
        Key Insight: If two strings have a common divisor, then:
        1. str1 + str2 must equal str2 + str1 (they must be composed of the same base pattern)
        2. The GCD string's length equals GCD(len(str1), len(str2))
        3. The GCD string is the prefix of str1 with length = GCD(len(str1), len(str2))
        
        Time Complexity: O(m + n) where m, n are lengths of str1 and str2
        Space Complexity: O(m + n) for string concatenation
        """
        
        # Step 1: Check if strings have a common divisor
        # If str1 + str2 != str2 + str1, they cannot have a common divisor
        # This is because if both strings are composed of the same base pattern,
        # concatenating them in either order should produce the same result
        #
        # Example where strings HAVE a common divisor:
        #   str1 = "ABCABC", str2 = "ABC"
        #   str1 + str2 = "ABCABC" + "ABC" = "ABCABCABC"
        #   str2 + str1 = "ABC" + "ABCABC" = "ABCABCABC"
        #   Since they're equal, both strings share the same base pattern "ABC"
        #
        # Example where strings DON'T have a common divisor:
        #   str1 = "LEET", str2 = "CODE"
        #   str1 + str2 = "LEET" + "CODE" = "LEETCODE"
        #   str2 + str1 = "CODE" + "LEET" = "CODELEET"
        #   Since they're different, no common divisor exists (return "")
        if str1 + str2 != str2 + str1:
            return ""
        
        # Step 2: Find GCD of the lengths using Euclidean algorithm
        # The GCD length will determine the length of our answer string
        #
        # Example: str1 = "ABCABC" (len=6), str2 = "ABC" (len=3)
        #   GCD(6, 3):
        #     GCD(6, 3) -> GCD(3, 6 % 3) = GCD(3, 0)
        #     When b=0, return a=3
        #   So gcd_length = 3
        #
        # Example: str1 = "ABABAB" (len=6), str2 = "ABAB" (len=4)
        #   GCD(6, 4):
        #     GCD(6, 4) -> GCD(4, 6 % 4) = GCD(4, 2)
        #     GCD(4, 2) -> GCD(2, 4 % 2) = GCD(2, 0)
        #     When b=0, return a=2
        #   So gcd_length = 2
        def gcd(a: int, b: int) -> int:
            """
            Calculate GCD using Euclidean algorithm.
            GCD(a, b) = GCD(b, a % b) until b becomes 0
            
            Example trace: GCD(6, 3)
            - GCD(6, 3): a=6, b=3 -> a=3, b=6%3=0
            - GCD(3, 0): b=0, return a=3
            """
            # Base case: when remainder is 0, return the other number
            while b:
                a, b = b, a % b  # Euclidean algorithm: GCD(a, b) = GCD(b, a % b)
            return a
        
        # Calculate GCD of the two string lengths
        # Example: gcd_length = gcd(6, 3) = 3 means our answer will be 3 characters long
        gcd_length = gcd(len(str1), len(str2))
        
        # Step 3: Return the prefix of str1 (or str2) with length = gcd_length
        # This prefix is guaranteed to divide both strings because:
        # - We verified str1 + str2 == str2 + str1 (same base pattern)
        # - The GCD length ensures it divides both string lengths evenly
        # - Therefore, both strings can be formed by repeating this prefix
        #
        # Example 1: str1 = "ABCABC" (len=6), str2 = "ABC" (len=3), gcd_length = 3
        #   str1[:3] = "ABC"
        #   Verify: "ABC" * 2 = "ABCABC" = str1 ✓
        #   Verify: "ABC" * 1 = "ABC" = str2 ✓
        #   Return: "ABC"
        #
        # Example 2: str1 = "ABABAB" (len=6), str2 = "ABAB" (len=4), gcd_length = 2
        #   str1[:2] = "AB"
        #   Verify: "AB" * 3 = "ABABAB" = str1 ✓
        #   Verify: "AB" * 2 = "ABAB" = str2 ✓
        #   Return: "AB"
        #
        # Why the prefix works:
        #   Since str1 + str2 == str2 + str1, both strings share the same repeating pattern.
        #   The GCD length finds the largest substring that can evenly divide both lengths.
        #   Any smaller length would work, but GCD gives us the LARGEST possible divisor.
        return str1[:gcd_length]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1: "ABCABC" and "ABC" -> GCD is "ABC"
    # Explanation: "ABCABC" = "ABC" * 2, "ABC" = "ABC" * 1
    print(solution.gcdOfStrings("ABCABC", "ABC"))  # Expected: "ABC"
    
    # Example 2: "ABABAB" and "ABAB" -> GCD is "AB"
    # Explanation: "ABABAB" = "AB" * 3, "ABAB" = "AB" * 2
    print(solution.gcdOfStrings("ABABAB", "ABAB"))  # Expected: "AB"
    
    # Example 3: "LEET" and "CODE" -> No common divisor
    # Explanation: "LEET" + "CODE" != "CODE" + "LEET" (different patterns)
    print(solution.gcdOfStrings("LEET", "CODE"))  # Expected: ""
