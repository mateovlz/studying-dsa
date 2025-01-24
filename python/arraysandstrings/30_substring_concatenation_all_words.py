from collections import defaultdict
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        # Step 1: Initialize variables
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        count_words = defaultdict(int)
        for word in words:
            count_words[word] += 1
        
        # Step 2: Sliding window search
        ans = []
        for i in range(word_len):
            left = i
            right = i
            window = defaultdict(int)
            have = 0
            
            while right + word_len <= len(s):
                # Add the next word to the window
                word = s[right:right + word_len]
                right += word_len
                print(word)
                if word in count_words:
                    window[word] += 1
                    if window[word] == count_words[word]:
                        have += 1
                    elif window[word] > count_words[word]:
                        # Too many occurrences of the word, shrink the window
                        while window[word] > count_words[word]:
                            left_word = s[left:left + word_len]
                            left += word_len
                            if window[left_word] == count_words[left_word]:
                                have -= 1
                            window[left_word] -= 1
                
                else:
                    # Invalid word, reset the window
                    window = defaultdict(int)
                    have = 0
                    left = right
                
                # Check if all words are matched
                if have == len(count_words):
                    ans.append(left)
                    
        return ans
