def binarySearch(arr,target):
  hi,lo=len(arr)-1,0
  while hi!=lo:
    i=(hi+lo)//2
    if arr[i]==target:
      return i
    elif arr[i]>target:
      hi=i-1
    elif arr[i]<target:
      lo=i+1
  return -1

print(binarySearch([1,2,3,4,5],4))