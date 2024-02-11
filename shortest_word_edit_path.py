from collections import defaultdict

def get_transforms(word):
    return ["%s*%s" % (word[:i], word[i + 1:]) for i in range(len(word))]

def shortestWordEditPath(source, target, words):
    words = set(words)
    if target not in words:
        return -1

    transformToWords = defaultdict(set)
    for word in words:
        for transform in get_transforms(word):
            transformToWords[transform].add(word)

    count = 0
    words = set([source])
    while words:
        if target in words:
            return count

        count += 1
        transforms = {transform
                        for word in words
                        for transform in get_transforms(word)
                        if transform in transformToWords}

        words = {word
                    for transform in transforms
                    for word in transformToWords[transform]}

        for transform in transforms:
            del transformToWords[transform]

    return -1

source = "bit"
target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
output = 5
assert shortestWordEditPath(source, target, words) == output

source = "no"
target = "go"
words = ["to"]
output = -1
assert shortestWordEditPath(source, target, words) == output