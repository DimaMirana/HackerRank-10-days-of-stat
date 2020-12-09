# Enter your code here. Read input from STDIN. Print output to STDOUT
def getQuartiles(number,arrayList):
    sort = sorted(arrayList)
    middle = float(number / 2)
    if number % 2 != 0:
        median = sort[int(middle - 0.5)]
    else:
        median = float(sort[int(middle)] + sort[int(middle) - 1]) / 2
    return int(median)

n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)

if n%2 ==0:
    median2 = getQuartiles(int(n/2),arr[:int(n/2)])
    median3 = getQuartiles(int(n/2),arr[int(n/2):])
else: 
    median2 = getQuartiles(int(n/2), arr[:int(n/2)])
    median3 = getQuartiles(int(n/2), arr[int(n/2)+1:])

median1 = getQuartiles(n,arr)
print(median2)
print(median1)
print(median3)
