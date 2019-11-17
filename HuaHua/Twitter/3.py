from __future__ import annotations
def getEventsOrder(team1, team2, events1, events2):
    order = {'G':0, 'Y':1, 'R':2, 'S':3}
    def parse(event, team):
        events = event.split()
        for i, t in enumerate(events):
            if t[0].isdigit():
                time = float(t.replace("+", "."))
                p = order[events[i + 1]]
                first_player = events[:i]
                second_player = ''
                if p == 3:
                    second_player = events[i + 2:]
                return time, p, team, first_player, second_player
    events = [(parse(e, team1), e) for e in events1]
    events += [(parse(e, team2), e) for e in events2]
    events = sorted(events)
    # i = j = 0
    # ans = []
    # while i < len(events1) and j < len(events2):
    #     if events1[i][0] <= events2[j][0]:
    #         ans.append(team1 + " " + events1[i][1])
    #         i += 1
    #     else:
    #         ans.append(team2 + " " + events2[j][1])
    #         j += 1
    # if i < len(events1):
    #     ans.extend([team1 + " " + e[1] for e in events1[i:]])
    # elif j < len(events2):
    #     ans.extend([team2 + " " + e[1] for e in events2[j:]])
    return [e[0][2] + " " + e[1] for e in events]


if __name__ == '__main__':
    team1 = "EDC"
    events1 = ['Name1 12 G', 'FirstName LastName 43 Y']
    team2 = "CDE"
    events2 = ['Name3 45+1 S SubName', 'Name4 46 G']
    print(getEventsOrder(team1, team2, events1, events2))
