from collections import deque
def is_valid(p):
    cnt = 0
    for i in p:
        if i == "(":
            cnt += 1
        if i == ")":
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0

def is_paran(c):
    return c == '(' or c ==')'

class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        visted = set()
        q = deque()
        q.appendleft(s)
        res = []
        found = False
        while(q):
            sub = q.popleft()
            if is_valid(sub):
                res.append(sub)
                found = True
            if found:
                continue
            for i in range(len(sub)):
                if is_paran(sub[i]):
                    new = sub[:i] + sub[i + 1:]
                    if not new in visted:
                        visted.add(new)
                        q.append(new)
        return res

if __name__ == '__main__':
    nums = "()())()"
    nums = "(a)())()"
    nums = ")("
    nums = ""
    sol = Solution()
    print(sol.removeInvalidParentheses(nums))







