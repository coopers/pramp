from collections import defaultdict, deque

def get_transforms(word):
    return ["%s*%s" % (word[:i], word[i + 1:]) for i in range(len(word))]

def shortestWordEditPath(source, target, words):
    remaining = set(words)
    if target not in remaining:
        return -1

    transformToWords = defaultdict(set)
    for word in remaining:
        for transform in get_transforms(word):
            transformToWords[transform].add(word)

    count = 0
    words = deque([source])
    while words:
        for _ in range(len(words)):
            word = words.popleft()
            if word == target:
                return count

            for transform in get_transforms(word):
                if transform in transformToWords:
                    for next_word in transformToWords[transform]:
                        if next_word in remaining:
                            words.append(next_word)
                            remaining.remove(next_word)
                    
                    del transformToWords[transform]

        count += 1

    return -1