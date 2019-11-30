import string
def ch_to_int(s, seg):
    dic = {}
    # for i, c in enumerate(string.ascii_uppercase):
    #     dic[c] = i + 1
    dic = {c : i + 1 for i, c in enumerate(string.ascii_uppercase)}
    return [[dic[c] for c in word if c in dic] for word in s.split(seg)]

def ch_inc(s, d):
    return "".join([chr(ord(c) + d) for c in s])

if __name__ == '__main__':
    s = "IHK"
    print(ch_inc(s, 3))
    s = "DPJBMDV DQJBMEU DQJBLDU BSHDJFS"
    print(ch_to_int(s, " "))


