/**
 The very naive and simple solution is sorting the all points by their distance to
 the origin point directly, then get the top k closest points. We can use the sort
 function and the code is very short.
 Advantages: short, intuitive and easy to implement
 Disadvantages: Not every efficient and have to know all of the points, and it's unable
 to deal with real-time case, it is an off-line solution
 */
 class Solution {
    public int[][] kClosest(int[][] points, int k) {
        Arrays.sort(points, (p1, p2) -> p1[0] * p1[0] + p1[1] * p1[1] - p2[0] * p2[0] - p2[1] * p2[1]);
        return Arrays.copyOfRange(points, 0, k);
    }
}