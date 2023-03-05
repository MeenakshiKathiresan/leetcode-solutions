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
        
        # construct adjacency list  with pattern as key - dictionary
        # make pattern of each word 
        
        patterns = {}
        
        wordList.append(beginWord)
        
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '_' + word[i+1:]
                
                if pattern not in patterns:
                    patterns[pattern] = []
                    
                patterns[pattern].append(word)
                
        
        visited = set([beginWord])
        ans = 1
        q = deque([beginWord])
        
        while q:
            
            for j in range(len(q)):
                word = q.popleft()
                
                if word == endWord:
                    return ans
                for i in range(len(word)):
                    pattern = word[:i] + '_' + word[i+1:]
                    for match in patterns[pattern]:
                        if match not in visited:
                            visited.add(match)
                            q.append(match)
                            
            ans+=1
        return 0
                