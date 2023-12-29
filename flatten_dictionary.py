def flatten_dictionary(dictionary):
    res = {}
    helper('', dictionary, res)
    return res

def helper(prev, dictionary, res):
    for k, v in dictionary.items():
        key = getkey(prev, k)
        if isinstance(v, dict):
            helper(key, v, res)
        else:
            res[key] = v

def getkey(prev, curr):
    if prev == '':
        return curr
    if curr == '':
        return prev
    return prev + '.' + curr