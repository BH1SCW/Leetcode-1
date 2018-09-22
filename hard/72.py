
def minDis(s1, s2, hash):
    """s1 is longer than s2"""
    if (s1 <= s2):
        s1, s2 = s2, s1
    key = s1 + '_' + s2
    if key in hash:
        return hash[key]
    if len(s2) == 0:
        value = len(s1)
        hash[key] = value
        return value
    if len(s1) == 0:
        value = len(s2)
        hash[key] = value
        return value
    if (s1[-1] == s2[-1]):
        value = minDis(s1[:-1], s2[:-1], hash)
        hash[key] = value
        return value
    else:
        value = min(minDis(s1, s2[:-1], hash), minDis(s2, s1[:-1], hash), minDis(s1[:-1], s2[:-1], hash)) + 1
        hash[key] = value
        return value

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        hash = {}
        if len(word1) >= len(word2):
            return minDis(word1, word2, hash)
        else:
            return minDis(word2, word1, hash)



