
import heapq

# find the kth largest element in the array


def findKLargest1(arr, k):
    #arr.sort()
    #print(arr)
    min_heap = []
    for num in arr:
        heapq.heappush(min_heap, -1*num)
        #if len(min_heap):

    ans = float("-inf") 
    for i in range(k):
        ans = heapq.heappop(min_heap)

    return abs(ans)

def findKLargest(arr, k):
    #arr.sort()
    #print(arr)
    min_heap = []

    for num in arr:
        heapq.heappush(min_heap, num)
        #before = min_heap[:]
        if len(min_heap) > k:
            heapq.heappop(min_heap)
        #print(min_heap, before)


    return min_heap[0]

def findKSmallest(arr, k):
    #arr.sort()
    #print(arr)
    min_heap = []

    for num in arr:
        heapq.heappush(min_heap, -1*num)
        #before = min_heap[:]
        if len(min_heap) > k:
            heapq.heappop(min_heap)
        #print(min_heap, before)


    return abs(min_heap[0])

#print(findKSmallest([2,3,4,2,6,7,3,5,9], 2))


##Lets make a string balancer

"""
    "(()()" -> "()()"

    "(()()"

    stack
    [ ( ]
    [ ( ] if stacl[0] == validator[(] // ) pop stack if not add it [ (, ( ] 
    [ (, ( ]  " " "   )  remove it 
    [ ( ]   

"""

def balacing_string1(s):
    val = {
        "(" : ")",
        ")" : "("
    }
    stack = []
    unbalance  = set()

    for i, c in enumerate(s,1):
        top_c, top_i = stack[-1] if stack else (0,0)
        print(top_c)
        if c == ")" and top_c == val[c]:
            stack.pop()
            if top_i in unbalance:
                unbalance.remove(top_i)
            #print(lc, c)
        else:
            stack.append((c, i))
            unbalance.add(i) 
    ans = []
    for i, c in enumerate(s):
        if i not in unbalance:
            ans.append(c)
            
    print(stack, unbalance, "".join(ans))


def balacing_string(s):

    stack = []
    ans = list(s)

    for i, c in enumerate(s):
        
        if  c == ")":
            if stack:
                stack.pop()
            else:
                ans[i]= ''
        else:
            stack.append(i)

    while stack:
        ans[stack.pop()] = ''
            
    print("".join(ans))

balacing_string("(()()")
balacing_string("(())()")
balacing_string("()))()()")
balacing_string("))(()())))")
balacing_string("()()()")
balacing_string("()()(")
balacing_string("()())")