def findSchedules(workHours, dayHours, pattern):
    num_days, allocated_hours = 0, 0
    for d in pattern:
        if d == '?':
            num_days += 1
        else:
            allocated_hours += int(d)
    ans = []
    def dfs(hours, days, index, path, ans):
        if index == 7:
            if hours == 0:
                ans.append(path)
            return
        if dayHours * days < hours:
            return
        if pattern[index] == '?':
            for h in range(0, min(dayHours + 1, hours + 1)):
                dfs(hours - h, days - 1, index + 1, path + str(h), ans)
        else:
            dfs(hours, days, index + 1, path + pattern[index], ans)
    dfs(workHours - allocated_hours, num_days, 0, '', ans)
    return ans

if __name__ == '__main__':
    work_hours = 24
    day_hours = 4
    pattern = '08??840'
    work_hours = 56
    day_hours = 8
    pattern = '???8???'
    print(findSchedules(work_hours, day_hours, pattern))
