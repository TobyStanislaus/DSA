def binarySearch(arr,target):
  hi=len(arr)-1
  lo=0

  while hi!=lo:
    if arr[(hi+lo)//2]==target:
      return (hi+lo)//2
    elif arr[(hi+lo)//2]>target:
      hi=((hi+lo)//2)-1
    elif arr[(hi+lo)//2]<target:
      lo=((hi+lo)//2)+1

print(binarySearch([1,2,3,4,5,6],5))