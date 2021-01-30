class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def addWord(word: str):
            if word not in wordId:
                nonlocal nodeNum
                wordId[word] = nodeNum
                nodeNum += 1

        def addEdge(word: str):
            addWord(word)
            id1 = wordId[word]
            chars = list(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = "*"
                newWord = "".join(chars)
                addWord(newWord)
                id2 = wordId[newWord]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp

        wordId = dict()
        edge = collections.defaultdict(list)
        nodeNum = 0

        for word in wordList:
            addEdge(word)

        addEdge(beginWord)
        if endWord not in wordId:
            return 0

        dis = [float("inf")] * nodeNum
        beginId, endId = wordId[beginWord], wordId[endWord]
        dis[beginId] = 0

        que = collections.deque([beginId])
        while que:
            x = que.popleft()
            if x == endId:
                return dis[endId] // 2 + 1
            for it in edge[x]:
                if dis[it] == float("inf"):
                    dis[it] = dis[x] + 1
                    que.append(it)

        return 0


from typing import List
from collections import deque
import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # word_set = set(wordList)
        # if endWord not in word_set or len(word_set)==0:
        #     return 0
        # if beginWord in word_set:
        #     word_set.remove(beginWord)
        # word_len = len(beginWord)
        # queue = deque()
        # queue.append(beginWord)

        # visited = set()
        # visited.add(beginWord)

        # step = 1

        # while queue:
        #     current_size = len(queue)
        #     for i in range(current_size):
        #         word = queue.popleft()
        #         word_list = list(word)
        #         for j in range(word_len):
        #             original_char = word_list[j]
        #             for k in string.ascii_lowercase:
        #                 word_list[j] = k
        #                 next_word = ''.join(word_list)
        #                 if next_word in word_set:
        #                     if next_word==endWord:
        #                         return step+1
        #                     if next_word not in visited:
        #                         visited.add(next_word)
        #                         queue.append(next_word)
        #             word_list[j] = original_char
        #     step+=1
        # return 0


        word_set = set(wordList)
        if len(word_set)==0 or endWord not in word_set:
            return 0
        begin_visit = set()
        begin_visit.add(beginWord)
        end_visit = set()
        end_visit.add(endWord)
        visited = set()
        visited.add(beginWord)
        visited.add(endWord)
        step = 1
        word_len = len(beginWord)

        while begin_visit:
            if len(begin_visit)>len(end_visit):
                begin_visit, end_visit = end_visit, begin_visit
            next_level_visit = set()
            for word in begin_visit:
                word_list = list(word)
                for j in range(word_len):
                    original_char = word_list[j]
                    for k in string.ascii_lowercase:
                        word_list[j] = k
                        next_word = ''.join(word_list)
                        if next_word in word_set:
                            if next_word in end_visit:
                                return step+1
                            if next_word not in visited:
                                visited.add(next_word)
                                next_level_visit.add(next_word)
                    word_list[j] = original_char
            step+=1
            begin_visit = next_level_visit
        return 0
