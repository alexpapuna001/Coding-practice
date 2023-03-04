def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = {}
        for i in strs:
            l = [0]*26
            for j in i:
                l[ord(j)-ord('a')] +=1
            l = tuple(l)
            if l not in ans:
                ans[l] = [i]
            else:
                ans[l].append(i)      
        return ans.values()
                    
print(groupAnagrams(["eat","bussin","tea","tan","ate","nat","bat"]))