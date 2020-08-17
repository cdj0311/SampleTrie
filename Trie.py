# encoding:utf-8
#############################################
# FileName: SampleTrie.py
# Author: ChenDajun
# CreateTime: 2020-08-17
# Descreption: A sample trie for words search
#############################################

class Trie:
    """
    Trie数组字符串匹配
    """
    def __init__(self):
        self.root = dict()
        self.end = "/"

    def add(self, word):
        """ 从根节点遍历单词,如果不存在则新增,最后加上一个单词结束标志 """
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[self.end] = None

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node: return False
            node = node[c]
        return self.end in node
        

if __name__ == "__main__":
    tree = Trie()
    tree.add(u"腾讯")
    tree.add(u"新浪")
    
    print(tree.search(u"新浪"))
    print(tree.search(u"新闻"))