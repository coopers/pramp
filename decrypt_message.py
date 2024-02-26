def decrypt(word):  
    MIN_VALUE = ord('a')
    res = []
    step_2 = 1
    for i in range(len(word)):
        value = ord(word[i]) - step_2
        while value < MIN_VALUE:
            value += 26

        res.append(chr(value))
        step_2 += value

    return ''.join(res)

assert decrypt('dnotq') == 'crime'