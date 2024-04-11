#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        arr.sort()
        s1=arr[0]
        s2=arr[n-1]
        size1=len(s1)
        size2=len(s2)
        i=0
        j=0
        ans=[]
        string=""
        while i<size1 and j<size2:
            if s1[i]==s2[j]:
                ans.append(s1[i])
            else:
                break
            i+=1 
            j+=1
        if len(ans)==0:
            return -1
        else:
            for ele in ans:
                string+=ele
            return string# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends