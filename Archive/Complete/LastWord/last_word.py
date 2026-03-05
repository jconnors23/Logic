class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index = -1
        count = 0 
        empty = " "
        while s[index] == empty: 
            if len(s) > 0: 
                s = s[:-1]
            else: 
                return 0
        while s[index] != empty:
            if abs(index) == len(s):
                return len(s)
            count+=1 
            index-=1 
        return count 

if __name__ == "__main__":
    example = "fly"
    #example = "f"
    print(Solution().lengthOfLastWord(example))