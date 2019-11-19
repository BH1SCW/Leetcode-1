from __future__ import annotations
from collections import Counter
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


