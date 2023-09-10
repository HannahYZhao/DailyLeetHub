/**
 * @param {string} s
 * @return {number}
 */
 // Time complexity: O(n) The algorithm traverses the given string only once, where n is the length of the string
 // Space complexity: O(1) The space required to store the map is O(256), which is constant
var lengthOfLongestSubstring = function(s) {
    let ans = 0, l = 0, r = 0;
    let n = s.length;
    // Create a map of size 256 to store the last occurrence of each character in the string, initialized with -1
    let map = new Array(256).fill(-1);
    while(r < n) {
        if(map[s.charCodeAt(r)] != -1) {
            l = Math.max(map[s.charCodeAt(r)] + 1, l);
        }
        map[s.charCodeAt(r)] = r;
        ans = Math.max(ans, r - l + 1);
        r++;
    }
    return ans;
};