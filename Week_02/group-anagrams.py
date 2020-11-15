class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        '''
        #排序数组分类
        for i in strs:
            ans[tuple(sorted(i))].append(i)
        return list(ans.values())
        '''
        # 按计数分类
        '''
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())
        '''
        for i in range(len(strs)):
            hash_string = ''.join(sorted(strs[i]))
            ans[hash_string].append(strs[i])
        return list(ans.values())
