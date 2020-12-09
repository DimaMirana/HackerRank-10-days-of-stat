def getMean(listed, number):
    mean = sum(listed) / number
    return mean


def getMedian(listed, number):
    sort = sorted(listed)
    middle = float(number / 2)
    if number % 2 != 0:
        median = sort[int(middle - 0.5)]
    else:
        median = float(sort[int(middle)] + sort[int(middle) - 1]) / 2
    return median


def getMode(listed, number):
    sort = sorted(listed)
    mode = 0
    count, max = 0, 0
    current = 0

    for i in sort:
        if (i == current):
            count += 1
        else:
            count = 1
            current = i
        if (count > max):
            max = count
            mode = i
    return mode


N = int(input())
x = list(map(int, input().split()))
mean = getMean(x, N)
median = getMedian(x, N)
mode = getMode(x, N)
print('%.1f' % mean)
print('%.1f' % median)
print('%.1f' % mode)
