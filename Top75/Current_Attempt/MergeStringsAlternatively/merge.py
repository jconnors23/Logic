class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        remaining = min(len(word1), len(word2)) # the number of chars we get to add from both strs
        short_one = False # is word 1 the shortest
        tied = False
        if len(word1) < len(word2):
            short_one = True
        elif len(word1) > len(word2):
            short_one = False
        else:
            tied = True
        merged = ""

        for i in range(remaining): # add alternates with remaining capacity
            merged += word1[i]
            merged += word2[i]
        
        if tied: 
            return merged
        elif short_one:
            merged += word2[remaining:] # add remaining chars in longest strings via inclusive slice
        else:
            merged += word1[remaining:]
        return merged

if __name__ == "__main__":
    word1 = "cf"
    word2 = "eee"
    print(Solution().mergeAlternately(word1, word2))