from __future__ import annotations

def restock(itemCount, target):
    s = 0
    for i, c in enumerate(itemCount):
        s += c
        if s >= target:
            return s - target
    return target - s

if __name__ == '__main__':
