"""
Amazon's AWS provides fast and efficient server solutions.
The developers want to stress-test the quality of the servers' channels. 

They must ensure the following:
• Each of the packets must be sent via a single channel.
• Each of the channels must transfer at least one packet.

The quality of the transfer for a channel is defined by the median of the 
sizes of all the data packets sent through that channel.

Note: The median of an array is the middle element if the array is sorted in non-decreasing order. 
If the number of elements in the array is even, the median is the average of the two middle elements.

Find the maximum possible sum of the qualities of all channels. 
If the answer is a floating-point value, round it to the next higher integer.

Example:
    packets = [1, 2, 3, 4, 5]
    channels = 2
At least one packet has to go through each of the 2 channels. 
One maximal solution is to transfer packets {1. 2, 3, 4) through channel 1 and packet (5) through channel 2.
"""

# 2 channels
# ch1 = [1,2,3,4] = 2+3/2 = 2.5
# ch2 = [5]  = median = 5 
# Maximum 2.5 + 5  = 7.5 = 8

# Difficult part to me understand how to distribute the packets to the channels.

import math

def max_sum_qualities(packets, channels):
    packets.sort()
    n = len(packets)

    channel_groups = []
    k = channels
    # Distribute packets across channels
    for i in range(n-1, -1, -1):
        if k > 0:
            channel_groups.append([packets[i]])
            k -= 1
        else:
            channel_groups[-1].append(packets[i])
    print(channel_groups)
    total_quality = 0

    for i in range(len(channel_groups)):
        channel = channel_groups[i]
        size_channel = len(channel)
        

        if size_channel == 1:
            total_quality += channel[0]
        elif size_channel%2 == 1:
            #odd #impar
            mid = size_channel // 2
            total_quality += channel[mid]
        else:
            #even #par
            left = (size_channel // 2) - 1
            right = (size_channel // 2)
            total_quality += math.ceil((channel[left] + channel[right]) /2)

    return total_quality
"""
print(max_sum_qualities([1,2,3,4,5,6], 2))

print(max_sum_qualities([10, 20, 30, 40, 50, 60], 3))  # Output: 80
print(max_sum_qualities([10], 1))  # Output: 10
print(max_sum_qualities([5, 10, 15, 20], 4))  # Output: 50
print(max_sum_qualities([1, 2, 3], 5))  # Output: 6
print(max_sum_qualities([5, 5, 5, 5, 5], 3))  # Output: 15
print(max_sum_qualities([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))  # Output: 20
print(max_sum_qualities([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))  # Output: 6
print(max_sum_qualities([1, 2, 3, 4], 6))  # Output: 10
"""



"""
You are analyzing the market trends of Amazon stocks. An AWS financial service model returned an array of integers, 
PnL (Profit and Loss), for your portfolio representing that in the ith month, 
you will either gain or lose PnL(i). 
All reported PnL values are positive, representing gains.

As part of the analysis, you will perform the following operation on the PnL array any number of times:
• Choose any month i (0 ≤ 1< n) and multiply PnL[i] by -1

Find the maximum number of months you can afford to face a loss, i.e. have a negative PnL, 
such that the cumulative PnL for each of the n months remains strictly positive i.e. remains greater than O.

Note: The cumulative PnL for the ith month is defined as the sum of Pnl from 
the starting month up to the i month. For example, the cumulative PnL for the 
PnL = (3, -2, 5, -6, 17 is [3, 1, 6, 0, 1).

Example
Consider, n = 4, and PnL = (5, 3, 1, 2)
"""
import heapq

def maxNumberMonthsFlip(pnl):
    #lets build the culmulative 
    culmulative_pnl = [pnl[0]]

    for i in range(1, len(pnl)):
        culmulative_pnl.append(culmulative_pnl[-1] + pnl[i])
    
    culmulative = culmulative_pnl[-1]
    max_flipping = 0
    min_heap = pnl[:]
    heapq.heapify(min_heap)

    #in order to get max flipping we should substract the smallest elements
    while min_heap:
        smalles_pnl = heapq.heappop(min_heap)
        print(culmulative, smalles_pnl)
        if culmulative - smalles_pnl > 0:
            culmulative -= smalles_pnl
            max_flipping += 1
        else:
            break
    return max_flipping


print(maxNumberMonthsFlip([5, 3, 1, 2])) 

