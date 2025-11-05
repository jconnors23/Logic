class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        first = strs[0]
        prefix = ""
        for char in first:
            for word in strs:
                potential = prefix + char
                if char not in word or potential not in word:
                    return prefix 
                for i in range(len(potential)):
                    if potential[i] != word[i]:
                        return prefix
            prefix = potential
        return prefix

if __name__ == "__main__":
    one = ["flower","flow","flight"]
    two = ["aa", "ab"]
    three = ["c","acc","ccc"]
    four = ["abca","aba","aaab"]
    print(Solution().longestCommonPrefix(four))
