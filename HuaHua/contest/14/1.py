from __future__ import annotations
class Solution(object):
    def toHexspeak(self, num):
        """
        :type num: str
        :rtype: str
        """
        letters = ["A", "B", "C", "D", "E", "F", "I", "O"]
        ans = hex(int(num))[2:]
        ans = ans.replace('1', 'I')
        ans = ans.replace('0', 'O')
        ans = [ch.upper() for ch in ans]
        for ch in ans:
            if not ch in letters: return "Error"
        return "".join(ans)




if __name__ == '__main__':
    sol = Solution()
    num = "257"
    print(sol.toHexspeak(num))
    num = "3"
    print(sol.toHexspeak(num))
