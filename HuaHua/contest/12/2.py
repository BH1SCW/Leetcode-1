import bisect


class Leaderboard:
    def __init__(self):
        self.player = {}
        self.score = []

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.player:
            old = self.player[playerId]
            pos = bisect.bisect_left(self.score, old)
            self.score = self.score[:pos] + self.score[pos + 1:]
            self.player[playerId] += score
            bisect.insort(self.score, old + score)
        else:
            self.player[playerId] = score
            bisect.insort(self.score, score)

    def top(self, K: int) -> int:
        return sum(self.score[-K:])

    def reset(self, playerId: int) -> None:
        old = self.player[playerId]
        pos = bisect.bisect_left(self.score, old)
        self.score = self.score[:pos] + self.score[pos + 1:]
        self.player[playerId] = 0
        self.score = [0] + self.score

