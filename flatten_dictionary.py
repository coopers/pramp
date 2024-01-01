def flatten_dictionary(d):
    res = {}
    helper('', d, res)
    return res

def helper(prefix, d, res):
    for k, v in d.items():
        k = prefix or k if not prefix or not k else prefix + '.' + k
        if isinstance(v, dict):
            helper(k, v, res)
        else:
            res[k] = v

assert flatten_dictionary(
    {
        "Key1" : "1",
        "Key2" : {
            "a" : "2",
            "b" : "3",
            "c" : {
                "d" : "3",
                "e" : {
                    "" : "1"
                }
            }
        }
    }
) == {
    "Key1" : "1",
    "Key2.a" : "2",
    "Key2.b" : "3",
    "Key2.c.d" : "3",
    "Key2.c.e" : "1"
}
