// Time complexity: O(1). Since all operations are performed directly on the stack and do not depend on the stack's size.
// Space complexity: O(n). Where n is the number of elements pushed onto the stack. 
class MinStack {
    private Stack<Pair<Integer, Integer>> stack;

    public MinStack() {
        stack = new Stack<>();
    }

    public void push(int val) {
        if (stack.isEmpty()) {
            stack.push(new Pair<>(val, val));
        } else {
            int min = Math.min(stack.peek().getValue(), val);
            stack.push(new Pair<>(val, min));
        }
    }

    public void pop() {
        if (!stack.isEmpty()) {
            stack.pop();
        }
    }

    public int top() {
        if (stack.isEmpty()) {
            return 0;
        }
        return stack.peek().getKey();
    }

    public int getMin() {
        if (stack.isEmpty()) {
            return 0;
        }
        return stack.peek().getValue();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */