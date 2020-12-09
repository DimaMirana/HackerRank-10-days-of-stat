import math
def getStandardDeviation(arrayList,number):
  mean = sum(arrayList)/number

  summation = 0
  for i in range(len(arrayList)):
    summation += ((arrayList[i]-mean) * (arrayList[i]-mean))
  sigma = math.sqrt(summation/number)
  return sigma

n = int(input())
x = list(map(int,input().split()))

standardDeviation = getStandardDeviation(x,n)
print('% .1f' % standardDeviation)
