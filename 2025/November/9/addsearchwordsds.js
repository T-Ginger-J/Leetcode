// LeetCode 211: Design Add and Search Words Data Structure
// Explanation:
// 1. Use Trie object with nested maps.
// 2. Add word by inserting nodes sequentially.
// 3. Search using DFS for '.' wildcard support.
// Time Complexity: O(M) addWord, O(N * 26^d) search
// Space Complexity: O(T)

class WordDictionary {
    constructor() {
        this.root = {};
    }

    addWord(word) {
        let node = this.root;
        for (let ch of word) {
            if (!node[ch]) node[ch] = {};
            node = node[ch];
        }
        node.isEnd = true;
    }

    search(word) {
        const dfs = (node, i) => {
            if (i === word.length) return node.isEnd === true;
            const ch = word[i];
            if (ch === '.') {
                for (let key in node)
                    if (key !== 'isEnd' && dfs(node[key], i + 1)) return true;
                return false;
            }
            return node[ch] ? dfs(node[ch], i + 1) : false;
        };
        return dfs(this.root, 0);
    }
}

let obj = new WordDictionary();
obj.addWord("bad");
obj.addWord("dad");
obj.addWord("mad");
console.log(obj.search("pad")); // false
console.log(obj.search("bad")); // true
console.log(obj.search(".ad")); // true
console.log(obj.search("b..")); // true
