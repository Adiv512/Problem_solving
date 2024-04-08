class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
         vector<int>answer;  
        int m = nums1.size(), n = nums2.size();
        int i = 0, j = 0;
        while(i<m && j<n){
            if(nums1[i] < nums2[j]){
                answer.push_back(nums1[i++]);  
            }
            else{
                answer.push_back(nums2[j++]);
            }
        }
        while(i<m){
            answer.push_back(nums1[i++]);
        }
        while(j<n){
            answer.push_back(nums2[j++]);
        }
        int Size = m+n;
        if(Size % 2 == 1 ){
            return answer[Size/2];
        }
        else{
            int ans1 = answer[Size/2];
            int ans2 = answer[Size/2 - 1];
            return (ans1+ans2)/2.0;
        }
    }
    
};