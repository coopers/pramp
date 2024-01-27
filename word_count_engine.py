from collections import OrderedDict

def word_count_engine(document):
    word_counts = OrderedDict()
    strs = document.split()
    for s in strs:
        letters = [ch.lower() for ch in s if ch.isalpha()]
        if letters:
            word = ''.join(letters)
            word_counts[word] = word_counts.get(word, 0) + 1

    max_count = max(word_counts.values()) + 1
    buckets = [[] for _ in range(max_count)]
    while word_counts:
        word, count = word_counts.popitem(last=False)
        buckets[count].append(word)

    return [[word, str(count)] for count in reversed(range(max_count)) for word in buckets[count]]

input = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
output = [
    ["practice", "3"],
    ["perfect", "2"],
    ["makes", "1"],
    ["youll", "1"],
    ["only", "1"], 
    ["get", "1"],
    ["by", "1"],
    ["just", "1"]
]

assert word_count_engine(input) == output