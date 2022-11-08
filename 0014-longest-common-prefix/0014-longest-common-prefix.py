class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        no_good = 0
        
        for i in range(len(min(strs, key=len))):
            for j in range(len(strs)):
                if (strs[j][i] != strs[0][i]):
                    no_good = 1
            if (no_good == 0):
                prefix += strs[0][i]
            else:
                break
        return prefix