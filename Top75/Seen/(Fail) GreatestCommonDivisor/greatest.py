from operator import truediv


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
    
        longest = ""
        for i in range(len(str2)):
            portion = len(str2)-i
            partial = str2[0:portion]
            alive = True
            while alive:
                for i in range(len(str1)):
                    if str[i] == 
            if partial in str1:


        return longest

if __name__ == "__main__":
    word1 = "ABCABC"
    word2 = "ABC"
    print(Solution().gcdOfStrings(word1, word2))