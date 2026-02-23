from collections import deque

def word_ladder(start, end, word_list):
    word_set = set(word_list)
    
    def bfs(start, end):
        queue = deque([(start, 1)])
        while queue:
            current_word, steps = queue.popleft()
            if current_word == end:
                return steps
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = current_word[:i] + c + current_word[i+1:]
                    if next_word in word_set:
                        queue.append((next_word, steps + 1))
                        word_set.remove(next_word)
        return 0
    
    return bfs(start, end)
    
print(word_ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print(word_ladder("hit", "cog", ["hot","dot","dog","lot","log"]))