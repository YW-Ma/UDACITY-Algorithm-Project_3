class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        # is word = the end of the word = "leaf"
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        container = []
        # base case
        if self.is_word:
            container.append(suffix)

        # DFS value processing
        for child in self.children:
            suffixes_for_a_child = self.children[child].suffixes(child)
            for suffix_child in suffixes_for_a_child:
                container.append(suffix + suffix_child)

        return container
'''
      >1
    2
  3|   6|
4|  5|
3\4\5\6都是word结尾，1是输入的字母。
各层的container情况如下：

到达base
[]
[3] --- [6]
[4],[5]

3的suffixes返回后
[]
[3,34,35] --- [6]

2的suffixes返回后
[23,234,235,26]

'''

class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        # Root:
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        
        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]
        
        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        
        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]
        
        return current_node

# Test:
print("Case 1")
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

prefix = "an"
prefixNode = MyTrie.find(prefix)
if prefixNode:
    print('\n'.join(prefixNode.suffixes()))
else:
    print(prefix + " not found")
"""
Expected output:
t
thology
tagonist
tonym
"""

print("Case 2")
prefix = "auto"
prefixNode = MyTrie.find(prefix)
if prefixNode:
    print('\n'.join(prefixNode.suffixes()))
else:
    print(prefix + " not found")
"""
Expected output:
auto not found
"""

print("Case 3")
MyTrie_2 = Trie()
wordList = [
    ""
]
for word in wordList:
    MyTrie_2.insert(word)

prefix = "a"
prefixNode = MyTrie_2.find(prefix)
if prefixNode:
    print('\n'.join(prefixNode.suffixes()))
else:
    print(prefix + " not found")
"""
Expected output:
a not found
"""