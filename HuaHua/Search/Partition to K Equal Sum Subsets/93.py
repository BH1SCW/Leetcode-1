from __future__ import annotations

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def helper(head, tail, n):
            # invalid search
            if not tail:
                return
            # return
            if n == 0:
                if tail == '0' or tail[0] != '0' and int(tail) <= 255:
                    ans.append(head[1:] + '.' + tail)
                return
            l = 1 if tail[0] == '0' else 3
            # valid search
            for i in range(1, min(len(tail), l) + 1):
                if int(tail[0:i]) <= 255:
                   helper(head + '.' + tail[0:i], tail[i:], n - 1)
        helper("", s, 3)
        return ans

if __name__ == '__main__':
    sol = Solution()
    s = "25525511135"
    s = "0000"
    print(sol.restoreIpAddresses(s))



