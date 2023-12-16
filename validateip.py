def validateIP(ip):
    strs = ip.split('.')
    if len(strs) != 4:
        return False

    return all(
        s != '' and
        all(ch.isdigit() for ch in s) and
        (0 <= int(s) <= 255)
        for s in strs
    )