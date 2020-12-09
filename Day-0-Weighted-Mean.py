def getWeightedMean(arrayList,weights):
  denominator = sum(weights)
  sumWeight = 0
  for i in range(len(arrayList)):
    sumWeight += arrayList[i]*weights[i]
  return sumWeight/denominator

n = int(input())
arr = list(map(int, input().split()))
weights = list(map(int, input().split()))

weightedMean = getWeightedMean(arr,weights)
print('%.1f' % weightedMean)
