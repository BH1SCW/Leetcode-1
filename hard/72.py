# def minDis(s1, s2, hash):
#     """s1 is longer than s2"""
#     if (s1 <= s2):
#         s1, s2 = s2, s1
#     key = s1 + '_' + s2
#     if key in hash:
#         return hash[key]
#     if len(s2) == 0:
#         value = len(s1)
#         hash[key] = value
#         return value
#     if len(s1) == 0:
#         value = len(s2)
#         hash[key] = value
#         return value
#     if (s1[-1] == s2[-1]):
#         value = minDis(s1[:-1], s2[:-1], hash)
#         hash[key] = value
#         return value
#     else:
#         value = min(minDis(s1, s2[:-1], hash), minDis(s2, s1[:-1], hash), minDis(s1[:-1], s2[:-1], hash)) + 1
#         hash[key] = value
#         return value
#
# class Solution:
#     def minDistance(self, word1, word2):
#         """
#         :type word1: str
#         :type word2: str
#         :rtype: int
#         """
#         hash = {}
#         if len(word1) >= len(word2):
#             return minDis(word1, word2, hash)
#         else:
#             return minDis(word2, word1, hash)
#
#
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        T = [[0] * (len(word2) + 1) for i in range(len(word1) + 1)]
        # distance for word1[:i] and ""(empty string)
        for i in range(1, len(word1) + 1):
            T[i][0] = i
        # distance for word2[:j] and ""(empty string)
        for j in range(1, len(word2) + 1):
            T[0][j] = j
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                # if two characters are the same, min(do nothing, delete it, insert)
                if word1[i - 1] == word2[j  - 1]:
                    T[i][j] = min(T[i - 1][j - 1], T[i - 1][j] + 1, T[i][j - 1] + 1)
                else:
                    # if two characters are not same, min(delete it, insert, or replace)
                    T[i][j] = min(T[i - 1][j] + 1, T[i][j - 1] + 1, T[i - 1][j - 1] + 1)
        return T[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    s = 'aa'
    p = 'baa'
    print(sol.minDistance(s, p))
