def flatten_dictionary(dictionary):
    res = {}
    helper('', dictionary, res)
    return res

def helper(prev, dictionary, res):
    for k, v in dictionary.items():
        key = prev or k if not prev or not k else prev + '.' + k
        if isinstance(v, dict):
            helper(key, v, res)
        else:
            res[key] = v