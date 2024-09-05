def icecreamParlor(m, arr):
    print(arr, m)
    
    pair_left = []
    # Write your code here
    """for num in range(len(arr)):
        for num2 in range(len(arr)):
            if(arr[num] + arr[num2] == m and num != num2):
                pair_left.append(num+1)"""
    price_map = {}      
    for i, price in enumerate(arr):
        print(i,price )
        complement = m - price
        
        if complement in price_map:
            return [price_map[complement] + 1, i + 1]
        
        price_map[price] = i

    #return pair_left
        
# [1, 4, 5, 3, 2] 4
# [2, 2, 4, 3] 4        