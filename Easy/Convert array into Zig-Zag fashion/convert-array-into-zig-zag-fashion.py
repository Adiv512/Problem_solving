#User function Template for python3


class Solution:
    # Program for zig-zag conversion of array
    def zigZag(self, arr, n):
     for i in range(n-1):
            if i % 2 == 0: # case for even index
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
            else: # case for odd index
                if arr[i] < arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys


def isZigzag(arr, n):
    f = 1

    for i in range(1, n):
        if f:
            if arr[i-1] > arr[i]:
                return 0
        else:
            if arr[i-1] < arr[i]:
                return 0
        f = f ^ 1

    return 1

t = int(input())
while t:
    n = int(input())
    arr = [int(x) for x in input().split()]
    ob = Solution()
    ob.zigZag(arr, n)
    check = isZigzag(arr, n)

    if check:
        print("1")
    else:
        print("0")

    t -= 1

sys.exit(0)

# } Driver Code Ends