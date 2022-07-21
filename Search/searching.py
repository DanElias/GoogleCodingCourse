
# binary search iterative

# move left and right until the 
def firstBadVersion(n):
    l = 1
    r = n
    while (l < r):
        


# first bad version leet code - easy

#2226 Maximum Candies Allocated to K Children - leetcode medum


res = 0
for i in range(1, 1000000):
    totalPiles = 0
    for j in range(candies.size)
        pile = candies[j] / i
        totalPiles += pile
    if totalPiles >= k:
        res = max(res, i)
return res

# can be done with binary search

def isPossible(candies, number, k):
    totalPiles = 0
    for i in range(candies.size):
        pile = candies[i] / number
        totalPiles += pile
    return totalPiles >= k

def maximumCandies(candies, k):
    l = 1, r = 10000000
    while (l < r):
        mid = (r-l)/2 + l
        if mid != 0 and isPossible(candies, mid, k):
            l = mid + 1
        else:
            r = mid
    return isPossible(candies, l, k) ? l : l - 1

# you can have an iterative solution and convert it to binary search


