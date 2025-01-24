"""
68. Text Justification
Solved
Hard
Topics
Companies
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
 

Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
"""

"""
Assumptions:
- each line should have maxwidth characters is the strings are not enough add ' '
- distribute the white spaces ' ' evenly IF the number of spaces doesnt divide evenly
assing MORE spaces to the LEFT than on the RIGHT
- the last line should be LEFT justified not adding extra spaces between the words
- if a word is too big and is alone in a line should be left aligned
"""
#words = ["This", "is", "an", "example", "of", "text", "justification."]
"""        1

    word lenght. plus 1 space
 1      4             5
 2      2             3
 3.     2             3

        8             10  

        16 - 8 = 8
    11 + 7 > maxWdith .
"""
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        n = len(words)
        i = 0
        len_chars = 0
        temp = []
        while i < n:
            if len_chars < maxWidth:
                temp.append(words[i])
                len_chars += len(words[i])
            
            #lets analyze if we should wrapped our line or continue
            if i + 1 < n:
                #               white spaces  len next word
                if len_chars + len(temp) + len(words[i+1]) > maxWidth:
                    spaces_to_fill = len(temp) - 1
                    white_spaces = maxWidth - len_chars 

                    if len(temp) == 1:
                        white_spaces = maxWidth - (len_chars + len(temp) -1)
                        ans.append(" ".join(temp) + (" "*white_spaces))
                    else:
                        ws = (white_spaces//max(spaces_to_fill,1) )
                        remind = white_spaces%max(spaces_to_fill,1)
                        for j in range(len(temp)-1):
                            #distribute white spaces even
                            temp[j] += " "* ws
                            #distribute white spaces uneven
                            if remind:
                                temp[j] += " "
                                remind -= 1
                        ans.append("".join(temp))

                    # we should wrapped the line
                    temp = []
                    len_chars = 0

            #this means we are at the end line
            else:
                white_spaces = maxWidth - (len_chars + len(temp) -1)
                ans.append(" ".join(temp) + (" "*white_spaces))

            i += 1
        return ans

