


from typing import List


class Solution:
    def longestStrChain(self, words:List[str]):

        # Sorting the words from bigger to smaller
        words.sort(key=lambda w: -len(w))

        word_index = {} #  map word to index

        for i, w in enumerate(words):
            word_index[w] = i

        print(word_index)

        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            
            res = 1

            for j in range(len(words[i])):
                w = words[i]
                pred = w[:j] + w[j+1:]
                if pred in word_index:
                    res = max(res, 1 + dfs(word_index[pred]))
            dp[i] = res

            return res
        #dfs(0)   
        for i in range(len(words)):
            dfs(i)
        
        return max(dp.values())

solution = Solution()
list1 = ["a","b","ba","bca","bda","bdca"]
list2 = ["a","b","ba","baqi"]
print(solution.longestStrChain(list2) )