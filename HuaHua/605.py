class Solution:
    # 这题就是greedy的，我加了padding，看起来很简单，但是居然错了三次。。。padding加错了，然后判断的条件也错了
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0


