class Solution:
    # 这道题其实挺烦的，但是我自己没写好，高的过于复杂了。后来有很多可以refine的地方。这样虽然复杂度还是差不多的，但是思路清晰简洁很多。
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = [0] * 8
        ki, kj = king[0], king[1]
        dis = lambda i, j: abs(i - ki) + abs(j - kj)
        for q in queens:
            qi, qj = q[0], q[1]
            dx, dy = qi - ki, qj - kj
            if dx * dy > 0 and dx == dy:
                if dx > 0 and ((ans[7] and dis(*q) < dis(*ans[7])) or not ans[7]):
                    ans[7] = q
                    continue
                if dx < 0 and ((ans[0] and dis(*q) < dis(*ans[0])) or not ans[0]):
                    ans[0] = q
                    continue
            elif dx * dy < 0 and dx == - dy:
                if dx > 0 and ((ans[5] and dis(*q) < dis(*ans[5])) or not ans[5]):
                    ans[5] = q
                    continue
                if dx < 0 and ((ans[2] and dis(*q) < dis(*ans[2])) or not ans[2]):
                    ans[2] = q
                    continue
            elif dx == 0:
                if dy > 0 and ((ans[4] and dis(*q) < dis(*ans[4])) or not ans[4]):
                    ans[4] = q
                    continue
                if dy < 0 and ((ans[3] and dis(*q) < dis(*ans[3])) or not ans[3]):
                    ans[3] = q
                    continue
            elif dy == 0: # dy == 0
                if dx > 0 and ((ans[6] and dis(*q) < dis(*ans[6])) or not ans[6]):
                    ans[6] = q
                    continue
                if dx < 0 and ((ans[1] and dis(*q) < dis(*ans[1])) or not ans[1]):
                    ans[1] = q
                    continue
        return [a for a in ans if a]




    def queensAttacktheKing2(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = [0] * 8
        ki, kj = king[0], king[1]
        for q in queens:
            qi, qj = q[0], q[1]
            if ki - qi == kj - qj and qi < ki:
                if ans[0] and ki - qi < ki - ans[0][0] or not ans[0]:
                    ans[0] = q
                    continue
            if ki - qi == kj - qj and qi > ki:
                if ans[7] and qi - ki < ans[7][0] - ki or not ans[7]:
                    ans[7] = q
                    continue
            if ki - qi == qj - kj and qi > ki:
                if ans[2] and qi - ki < ans[2][0] - ki or not ans[2]:
                    ans[2] = q
                    continue
            if ki - qi == qj - kj and qi < ki:
                if ans[5] and ki - qi < ki - ans[5][0] or not ans[5]:
                    ans[5] = q
                    continue
            if kj == qj and qi < ki:
                if ans[1] and ki - qi < ki - ans[1][0] or not ans[1]:
                    ans[1] = q
                    continue
            if kj == qj and qi > ki:
                if ans[6] and qi - ki < ans[6][0] - ki or not ans[6]:
                    ans[6] = q
                    continue
            if ki == qi and qj < kj:
                if ans[3] and kj - qj < kj - ans[3][1] or not ans[3]:
                    ans[3] = q
                    continue
            if ki == qi and qj > kj:
                if ans[4] and qj - kj < ans[4][1] - kj or not ans[4]:
                    ans[4] = q
                    continue
        return [a for a in ans if a]

