def countReq(filename):
    repeated = {}
    with open("req_" + filename, 'w') as o:
        with open(filename) as f:
            for line in f:
                l = line.strip().split()
                date = l[3][1:]
                if date in repeated and not repeated[date]:
                    repeated[date] += 1
                    o.write(date + '\n')
                else:
                    repeated[date] = 0

def countReqInc(filename):
    prev = ""
    with open("req_" + filename, 'w') as o:
        with open(filename) as f:
            for line in f:
                l = line.strip().split()
                cur = l[3][1:]
                if cur == prev:



if __name__ == '__main__':
    filename = "input001.txt"
    countReq(filename)
