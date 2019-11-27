from __future__ import annotations
from collections import Counter
# 这题还挺有意思的
def root(x, n):
  Err = 0.001
  l, h = 0, x
  trunc = lambda x: float("{0:.{1}f}".format(x, 3))
  while h - l > Err:
    # m = trunc((l + h) / 2)
    m = round((l + h) / 2, 3)
    if m == l: return m
    value = m ** n - x
    if value > 0:
      h = m
    else:
      l = m
  return l

class Solution:
    def favoriteGenres(self, user_songs:dict, song_genres:dict) -> dict:
        count = {}
        styles = {s: genre for genre, songs in song_genres.items() for s in songs}
        for user, songs in user_songs.items():
            style = [styles[s] for s in songs if s in styles]
            c = Counter(style)
            nc = {}
            for style, f in c.items():
                nc.setdefault(f, []).append(style)
            count[user] = nc
        ans = {}
        for user, c in count.items():
            if not c: continue
            m = max(c.keys())
            ans[user] = c[m]
        return ans

if __name__ == '__main__':
    print(root(3, 2))
    print(root(9, 2))
    sol = Solution()
    userSongs = {"David": ["song1", "song2", "song3", "song4", "song8"], "Emma": ["song5", "song6", "song7"]}
    songGenres = {
        "Rock": ["song1", "song3"],
        "Dubstep": ["song7"],
        "Techno": ["song2", "song4"],
        "Pop": ["song5", "song6"],
        "Jazz": ["song8", "song9"]}
    print(sol.favoriteGenres(userSongs, songGenres))
    userSongs = {"David": ["song1", "song2"], "Emma": ["song3", "song4"]}
    songGenres = {}
    print(sol.favoriteGenres(userSongs, songGenres))


