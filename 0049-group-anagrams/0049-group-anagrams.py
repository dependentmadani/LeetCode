class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_strs = []
        result = []
        for i in strs:
            new_strs.append(''.join(sorted(i)))
        i = 0
        while (i < len(strs)):
            val = []
            tmp = i
            for f in result:
                if (strs[tmp] in f):
                    i += 1
                    break
            if (tmp != i):
                tmp = i
                continue
            val.append(strs[tmp])
            for j in range(tmp + 1, len(strs)):
                if (new_strs[tmp] == new_strs[j]):
                    val.append(strs[j])
            result.append(sorted(val))
            i += 1
            while (i < len(strs) and new_strs[tmp] == new_strs[i]):
                i += 1
        return result
