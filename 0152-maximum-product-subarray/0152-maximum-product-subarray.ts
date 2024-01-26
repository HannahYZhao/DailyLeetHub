// Time Complexity: O(N)
// Space Complexity: O(1)
function maxProduct(nums: number[]): number {
    let highest = nums[0]
    let lowestSoFar = highest
    let highestSoFar = highest

    for (let i = 1; i < nums.length; i++) {
        const num = nums[i]
        const candidateOne = lowestSoFar * num
        const candidateTwo = highestSoFar * num

        highestSoFar = Math.max(num, candidateOne, candidateTwo)
        lowestSoFar = Math.min(num, candidateOne, candidateTwo)

        highest = Math.max(highestSoFar, highest)
    }

    return highest
};