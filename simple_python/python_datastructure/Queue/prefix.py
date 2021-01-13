class Solution:
    def longestCommonPrefix(self, strs):
        #-> str:
        prefix =""
        if len(strs) > 0:     
            for cntr in range(len(strs[0])):
                search = strs[0][cntr]
                i = 0
                for word in strs:
                    try:
                        if word[cntr] == search:
                            i += 1
                    except:
                        pass
                if i == len(strs):
                    prefix = prefix + search
                else:
                    return prefix
            return prefix
        else:
            return prefix
                    

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["aca","cba"]))