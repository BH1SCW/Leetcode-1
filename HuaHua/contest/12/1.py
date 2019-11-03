class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        is_final = False
        while not is_final:
            is_final = True
            new = arr[:]
            for i, n in enumerate(arr):
                if i == 0 or i == len(arr) - 1: continue
                if arr[i - 1] < n and n > arr[i + 1]:
                    new[i] -= 1
                    is_final = False
                elif arr[i - 1] > n and n < arr[i + 1]:
                    new[i] += 1
                    is_final = False
            arr = new
        return arr

