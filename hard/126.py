import time

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        s1 = time.time()
        if not beginWord in wordList:
            wordList.append(beginWord)
        if not endWord in wordList:
            return []
        n = len(wordList)
        # print("{} words".format(n))
        beginIndex = wordList.index(beginWord)
        endIndex = wordList.index(endWord)
        # scan the list
        alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        hash_table = {}
        for i in range(n):
            hash_table[wordList[i]] = i
       # build the parent list
       #  print("adjacency matrix: {}".format(time.time() - s1))
        s1 = time.time()
        color = [0 for i in range(n)]
        dis = [-1 for i in range(n)]
        parent = [[] for i in range(n)]
        # start preparation
        WHITE = 0
        BLACK = 1
        GRAY = 2
        RED = 3
        color[beginIndex] = GRAY
        color[endIndex] = RED
        dis[beginIndex] = 0
        dis[endIndex] = 0
        parent[beginIndex].append(-1)
        queue = [beginIndex, endIndex]
        if_search = True
        ind = 0
        while len(queue) != 0:
            u = queue.pop(0)
            adjs = connections(wordList, u, color, alphabet, hash_table)
            for adj in adjs:
                    if color[adj] + color[u] == 5 and if_search:
                        finalDis = dis[adj] + dis[u]
                        if color[adj] == RED:
                            endDis = dis[adj]
                            startDis = dis[u]
                        else:
                            endDis = dis[u]
                            startDis = dis[adj]
                        if_search = False
                        # print("Queue adding ends: {}".format(time.time() - s1))
                    # this place hasn't been reached
                    if color[adj] == WHITE:
                        dis[adj] = dis[u] + 1
                        if color[u] == GRAY:
                            parent[adj].append(u)
                        else:
                            parent[u].append(adj)
                        color[adj] = color[u] # 1 is gray
                        if if_search:
                            queue.append(adj)
                    else:
                        if color[u] == color[adj]:
                            if dis[adj] == dis[u] + 1:
                                if color[u] == GRAY:
                                    parent[adj].append(u)
                                else:
                                    parent[u].append(adj)
                        else:
                            if dis[adj] + dis[u] <= finalDis:
                                if color[u] == GRAY:
                                    parent[adj].append(u)
                                else:
                                    parent[u].append(adj)
                        # print("parent of {0} is {1}".format(wordList[adj], wordList[u]))
            color[u] = BLACK # 3 is black
        # print("BFS: {}".format(time.time() - s1))
        # find all the paths
        s1 = time.time()
        sol = []
        def printPath(stack, root):
            stack.append(root)
            if root == beginIndex:
                path = []
                [path.append(wordList[stack[i]]) for i in range(len(stack) - 1, 0, -1)]
                path.append(endWord)
                sol.append(path)
                stack.pop()
            else:
                for p in parent[root]:
                    printPath(stack, p)
                stack.pop()
        printPath([], endIndex)
        # print("Path Print: {}".format(time.time() - s1))
        # print("{} distance calculations needed".format(ind))
        print(sol)
        return sol

def connections(wordList, i, color, alphabet, hash_table):
    w1 = wordList[i]
    adj = []
    for i in range(len(w1)):
        for a in alphabet:
            w = w1[0:i] + a + w1[i + 1:]
            if w in hash_table and w1 != w:
                if color[hash_table[w]] != 1:
                    adj.append(hash_table[w])
    return adj

if __name__ == "__main__":
    sol = Solution()
    sol = sol.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])
