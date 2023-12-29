def flatten_dictionary(d):
    res = {}
    helper('', d, res)
    return res

def helper(prev, d, res):
    for k, v in d.items():
        key = prev or k if not prev or not k else prev + '.' + k
        if isinstance(v, dict):
            helper(key, v, res)
        else:
            res[key] = v