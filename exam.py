arr = [10, 3, 8, 15, 6, 12, 2, 18, 7, 1]

def inversion(arr):
    length=len(arr)
    count=0
    for i in range(length-1):
        for j in range(i+1,length):
            if arr[i]>arr[j]:
                count+=1
    return count

result=inversion(arr)
print(result)
