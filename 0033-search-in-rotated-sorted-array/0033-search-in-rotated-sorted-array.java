// If we know the start, we can assign left and right specific values to start.
class Solution {
    public int search(int[] nums, int target) {
        if(nums == null || nums.length == 0) return -1;
        int l = 0, r = nums.length-1, m = 0;
        // Find out the index of the smallest element.
        while(l < r) {
            m = (l + r) / 2;
            if(nums[m] > nums[r]) {
                l = m + 1;
            }else {
                r = m;
            }
        }

        // Since we now know the start, find out if the target is to left or right of start in the array.
        int s = l;
        l = 0; r = nums.length - 1;
        if(target >= nums[s] && target <= nums[r]) {
            l = s;
        }else {
            r = s;
        }
        // The regular search
        while(l <= r) {
            m = (l + r) / 2;
            if(nums[m] == target) return m;
            else if(nums[m] > target) r = m - 1;
            else l = m + 1;
        }

        return -1;
    }
}