def validateIP(ip):
    if not (6 < len(ip) < 16):
        return False
    
    strs = ip.split('.')
    if len(strs) != 4:
        return False

    return all(
        s != '' and
        (len(s) == 1 or s[0] != '0') and
        s.isdigit() and
        0 <= int(s) <= 255
        for s in strs
    )

assert validateIP('192.168.0.1') == True
assert validateIP('0.0.0.0') == True
assert validateIP('123.24.59.99') == True
assert validateIP('192.168.123.456') == False
assert validateIP('0.00.0.0') == False
assert validateIP('.00.0.0') == False