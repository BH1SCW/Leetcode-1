import collections, itertools
def findSecretWord(self, wordlist, master):
    n = 0
    while n < 6:
        count = collections.Counter(w1 for w1, w2 in itertools.permutations(wordlist, 2) if self.match(w1, w2) == 0)
        guess = min(wordlist, key=lambda w: count[w])
        n = master.guess(guess)
        wordlist = [w for w in wordlist if self.match(w, guess) == n]

def match(w1, w2):
    return sum([c1 == c2 for c1, c2 in zip(w1, w2)])

if __name__ == '__main__':
    wordlist = ["acckzz", "ccbazz", "eiowzz", "abcczz"]
    wordlist = ["abc", "def", "ghi", "klm"]
    count = collections.Counter(w1 for w1, w2 in itertools.permutations(wordlist, 2) if match(w1, w2) == 0)
    print(count)
    secret = "acckzz"
