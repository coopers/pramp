def decrypt(word):  
    MIN_VALUE = ord('a')
    res = []
    n = 1
    for i in range(len(word)):
        value = ord(word[i]) - n
        if value < MIN_VALUE:
            value += 26

        res.append(chr(value))
        n += value
        n %= 26

    return ''.join(res)

assert decrypt('dnotq') == 'crime'