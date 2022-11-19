import collections
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList:
            return 0

        similar_words = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for idx in range(len(word)):
                pattern = word[:idx] + "*" + word[idx + 1:]
                similar_words[pattern].append(word)

        visit = {beginWord}
        sol = 1
        q = collections.deque()
        q.append(beginWord)

        while q:
            size = len(q)
            while size:
                size -= 1
                curr_word = q.popleft()
                if curr_word == endWord:
                    return sol
                for idx in range(len(curr_word)):
                    pattern = curr_word[:idx] + "*" + curr_word[idx + 1:]
                    for word in similar_words[pattern]:
                        if word not in visit:
                            visit.add(word)
                            q.append(word)
            sol += 1

        return 0
                    

if __name__ == '__main__':
    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]

    # beginWord = "a"
    # endWord = "c"
    # wordList = ["a", "b", "c"]

    object = Solution()

    print(object.ladderLength(beginWord, endWord, wordList))
