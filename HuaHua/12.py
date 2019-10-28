import itertools
import bisect
class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        for i, j in itertools.product((4, 9), range(3)):
            dic[i * 10 ** j] = dic[10 ** j] + dic[(i + 1) * 10 ** j]
        ans = ''
        keys = sorted(dic.keys())
        while num:
            v = keys[bisect.bisect(keys, num) - 1] # 有熟悉了一下biset的用法，除此之外没什么特别的了，要小心一点就是了，看了一下分布，大部分人还是比我快的
            ans += dic[v]
            num -= v
        return ans


