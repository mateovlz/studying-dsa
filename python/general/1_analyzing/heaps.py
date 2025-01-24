import heapq



class Solution():
    
    def __init__(self, arr):
        self.arr = arr

    #build a minHeap
    def print_min_heap(self):
        heapq.heapify(self.arr)
        print(self.arr)
        print(heapq.heappop(self.arr))
        
    #build a maxHeap
    def print_max_heap(self):
        temp = [val *-1 for val in self.arr]
        heapq.heapify(temp)
        print(temp)
        print(heapq.heappop(temp))


solution = Solution([1,2,3,4,5,6])

solution.print_min_heap()
solution.print_max_heap()