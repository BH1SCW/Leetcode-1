import calendar
def adayear(year):
    calendar.setfirstweekday(calendar.SUNDAY)
    first_day = calendar.weekday(year, 10, 1)
    return (2 - first_day) % 7 + 7

    # years = []
    # for i in range(-10000, 10000):
    #     if (calendar.isleap(i)):
    #         years += [i]
    # print(len(years))


if __name__ == '__main__':
    print(adayear(-1))
    # for i in range(7):
    #     print((2 - i) % 7 + 7)
