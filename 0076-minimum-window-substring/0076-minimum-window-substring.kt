class Solution {
    fun minWindow(s: String, t: String): String {
        val freq = IntArray(128) { 0 }
        t.forEach { freq[it.toInt()]++ }

        var res = ""
        var count = t.length
        var l = 0
        var r = 0

        while (r < s.length) {
            if (freq[s[r].toInt()]-- > 0) count--

            while (count == 0) {
                if (res.isEmpty() || r - l + 1 < res.length) {
                    res = s.substring(l, r + 1)
                }
                freq[s[l].toInt()]++
                if (freq[s[l++].toInt()] > 0) count++
            }
            r++
        }
        return res
    }
}
