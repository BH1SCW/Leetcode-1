from __future__ import annotations

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        tree = {}
        for region in regions:
            parent = region[0]
            tree[parent] = region[1:]
        self.ans = None
        def find_child(root):
            if self.ans: return set()
            ans = set()
            if root == region1 or root == region2:
                ans.add(root)
            for c in tree.get(root, []):
                ans = ans | find_child(c)
            if len(ans) == 2:
                self.ans = root
                return set()
            return ans
        for r in tree:
            find_child(r)
            if self.ans: return self.ans



if __name__ == '__main__':
    sol = Solution()
    regions = [["Earth", "North America", "South America"], ["North America", "United States", "Canada"],
               ["United States", "New York", "Boston"], ["Canada", "Ontario", "Quebec"], ["South America", "Brazil"]]
    region1 = "Quebec"
    region2 = "New York"
    print(sol.findSmallestRegion(regions, region1, region2))

