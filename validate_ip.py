def validateIP(ip):
    strs = ip.split('.')
    if len(strs) != 4:
        return False

    return all(
        s != '' and
        all(ch.isdigit() for ch in s) and
        0 <= int(s) <= 255
        for s in strs
    )

assert validateIP('192.168.0.1') == True
assert validateIP('0.0.0.0') == True
assert validateIP('123.24.59.99') == True
assert validateIP('192.168.123.456') == False