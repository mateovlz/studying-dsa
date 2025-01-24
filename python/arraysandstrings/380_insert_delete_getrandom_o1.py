"""
380. Insert Delete GetRandom O(1)
Solved
Medium
Topics
Companies
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

 

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
 

Constraints:

-231 <= val <= 231 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
"""

#o(n)

import random
class RandomizedSet:

    def __init__(self):
        self.ran_set = []

    def insert(self, val: int) -> bool:
        #o(n)
        if val in self.ran_set:
            return False
        else:
            #o(1)
            self.ran_set.append(val)
            return True
        

    def remove(self, val: int) -> bool:
        #o(n)
        if val in self.ran_set:
            #o(n)
            self.ran_set.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        n = len(self.ran_set)
        if n == 1:
            return self.ran_set[0]
        ran_position = random.randrange(0, n)
        #o(1)
        return self.ran_set[ran_position]
        
# O(1)
import random
class RandomizedSet:

    def __init__(self):
        self.ran_set = []
        self.positions = {}

    def insert(self, val: int) -> bool:
        
        if val in self.positions:
            return False
        else:
            index = len(self.ran_set)
            self.ran_set.append(val)
            self.positions[val] = index
            return True
        

    def remove(self, val: int) -> bool:

        if val in self.positions:
            last_index = len(self.ran_set) - 1
            curr_index = self.positions[val]

            if curr_index != last_index:
                last_val = self.ran_set[last_index]
                self.positions[last_val] = curr_index
                self.ran_set[curr_index] = last_val     

            self.ran_set.pop()
            del self.positions[val]

            return True
        else:
            return False

    def getRandom(self) -> int:
        n = len(self.ran_set)
        if n == 1:
            return self.ran_set[0]
        ran_position = random.randrange(0, n)

        return self.ran_set[ran_position]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()