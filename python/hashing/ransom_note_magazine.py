
"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""

def canConstruct(ransomNote: str, magazine: str) -> bool:
    def countMaps(s:str):
        mapCunts = defaultdict(int)
        for i in range(len(s)):
            mapCunts[s[i]] +=1
        return mapCunts

    ransomCounts = {}
    magazineCounts = {}

    if len(ransomNote) > len(magazine): return False

    ransomCounts = countMaps(ransomNote)
    magazineCounts = countMaps(magazine)

    print(ransomCounts, magazineCounts)

    for char, count in ransomCounts.items():
        magazine_count = magazineCounts[char]
        if magazine_count < count:
            return False
            
    return True