class Solution {
    public int coinChange(int[] coins, int amount) {
        if(amount < 1) return 0;
        return helper(coins, amount, new int[amount]);
    }

    private int helper(int[] coins, int rem, int[] count) {
        // rem: remaining coins after the last step;
        // count[rem]: minimum number if coins to sum up to rem
        if(rem < 0) return - 1;
        if(rem == 0) return 0; 
        if(count[rem - 1] != 0) return count[rem - 1];
        int min = Integer.MAX_VALUE;
        for(int coin : coins) {
            int res = helper(coins, rem-coin, count);
            if(res >= 0 && res < min)
                min = 1 + res;
        }
        count[rem - 1] = (min == Integer.MAX_VALUE) ? -1 :min;
        return count[rem-1];
    }
}