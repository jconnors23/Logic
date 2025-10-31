class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        first = strs[0]
        prefix = ""
        connected = True
        for char in first:
            for word in strs:
                print(f"word: {word}, char: {char}")
                if char not in word:
                    print(f"reached, char: {char}")
                    connected = False
                    break #conditionality needs adjustment, need to increment to next word
                else: 
                    if not connected:
                        break
            prefix += char
        return prefix

if __name__ == "__main__":
    example = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(example))
