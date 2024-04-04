function lengthOfLIS(nums: number[]): number {
    let values : Array<number> = [];
    let result = -1;
    for(let i = 0; i < nums.length; i++) {
        values[i] = 1;
        for(let j = 0; j < i; j++) {
            if(nums[i] > nums[j]){
                values[i] = Math.max(values[i], values[j]+1);
            }
        }
        result = Math.max(result, values[i]);
    }
    console.log(values);
    return result;
};