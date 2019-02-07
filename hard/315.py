def countSmaller(nums):
    count = [0] * len(nums)
    enums = list(enumerate(nums))
    def sort(enums):
        mid = len(enums) // 2
        if mid:
            left, right = sort(enums[:mid]), sort(enums[mid:])
            for i in range(len(enums) - 1, -1, -1):
                if not right or left and left[-1][1] > right[-1][1]:
                    count[left[-1][0]] += len(right)
                    enums[i] = left.pop()
                else:
                    enums[i] = right.pop()
        return enums
    sort(enums)
    return count

if __name__ == '__main__':
    nums = [5, 2, 6, 1]
    print(countSmaller(nums))
