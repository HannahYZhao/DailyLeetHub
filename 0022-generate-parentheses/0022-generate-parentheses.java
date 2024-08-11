import java.util.ArrayList;
import java.util.List;

public class Solution {

    /**
     * Generates all combinations of well-formed parentheses.
     * 
     * @param n the number of pairs of parentheses
     * @return a list of strings representing all valid parentheses combinations
     */
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        backtrack(result, new StringBuilder(), 0, 0, n);
        return result;
    }

    /**
     * Uses backtracking to generate all valid parentheses combinations.
     * 
     * @param result the list to collect valid parentheses combinations
     * @param sb the current string being built
     * @param open the number of open parentheses used
     * @param close the number of close parentheses used
     * @param max the total number of pairs of parentheses
     */
    private void backtrack(List<String> result, StringBuilder sb, int open, int close, int max) {
        if (sb.length() == max * 2) {
            result.add(sb.toString());
            return;
        }

        if (open < max) {
            sb.append('(');
            backtrack(result, sb, open + 1, close, max);
            sb.deleteCharAt(sb.length() - 1); // backtrack
        }
        
        if (close < open) {
            sb.append(')');
            backtrack(result, sb, open, close + 1, max);
            sb.deleteCharAt(sb.length() - 1); // backtrack
        }
    }
}
