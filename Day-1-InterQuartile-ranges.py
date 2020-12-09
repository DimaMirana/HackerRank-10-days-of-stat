def getInterquartileRange(number,arrayList):
  middle = float(number/2)
  if number % 2 != 0:
    median = arrayList[int(middle - 0.5)]
  else:
    median = float((arrayList[int(middle)] + arrayList[int(middle)-1])/2)
  return float(median)

n = int(input())
x = list(map(int,input().split()))
f = list(map(int,input().split()))
data = []
for i in range(len(x)):
  data += [x[i]]*f[i]
arr = sorted(data)
n = len(arr)
q2 = getInterquartileRange(n,arr)
q1 = getInterquartileRange(int(n/2),arr[:int(n/2)])
if n%2 == 0:
  q3 = getInterquartileRange(int(n/2),arr[int(n/2):])
else:
  q3 = getInterquartileRange(int(n/2),arr[int(n/2)+1:])
print('%.1f'%(q3-q1))
