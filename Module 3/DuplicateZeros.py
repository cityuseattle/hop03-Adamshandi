def duplicateZeros(arr)-> None:
    i=0
    for i in range(0, len(arr)-1):
        if arr[i]== 0:
            print(arr[i])
            print(arr.pop())
            arr.insert(i+1, 0)
            print(arr)
            i +=1
        i+=1
    print(arr)

arr1=[9, 0, 2, 3, 0, 4, 5, 0]
duplicateZeros(arr1)