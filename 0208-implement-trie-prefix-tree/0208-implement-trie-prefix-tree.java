// Time complexity: O(m), where m is the length of the string
// Space complexity: O(s), where s is the tital number of characters in all the strings that are inserted into the trie. 
class TrieNode {
    boolean isWord;
    TrieNode[] children;

    public TrieNode() {
        isWord = false;
        children = new TrieNode[26]; 
    }
}
class Trie {
    TrieNode root;

    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode node = root;
        for(char c: word.toCharArray()) {
            int index = c - 'a';
            if(node.children[index] == null) {
                node.children[index] = new TrieNode();
            }
            node = node.children[index];
        }
        node.isWord = true;
    }
    // Interare over each character of the string and traverse the dictinary representing the node of the tries
    public boolean search(String word) {
        TrieNode node = root;
        for(char c: word.toCharArray()) {
            int index = c - 'a';
            // If the character is not present in the dictionary, return false
            if(node.children[index] == null) {
                return false;
            }
            // If reach the end of the string and the last node is marked by the special character, we return true.
            node = node.children[index];
        }
        return node.isWord;
    }
    
    public boolean startsWith(String prefix) {
        TrieNode node = root;
        for(char c: prefix.toCharArray()) {
            int index = c - 'a';
            if(node.children[index] == null) {
                return false;
            }
            node = node.children[index];
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */