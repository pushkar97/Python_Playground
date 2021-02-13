def quickSort(unsortedList):
    length = len(unsortedList)
    if length <= 1 : return unsortedList

    pivot = unsortedList[-1]

    i = 0
    j = length - 2
    while i <= j:
        while j >= 0 and unsortedList[j] >= pivot:
            j-=1
        while i <= j and unsortedList[i] < pivot:
            i+=1
        if i < j:
            unsortedList[i], unsortedList[j] = unsortedList[j], unsortedList[i]
        else:
            unsortedList[i], unsortedList[-1] = unsortedList[-1], unsortedList[i]
    leftHalf = quickSort(unsortedList[:i])
    rightHalf = quickSort(unsortedList[i+1:])
    return leftHalf + [pivot] + rightHalf

if __name__ == "__main__":
    print(f'quickSort : {quickSort([9, 3, 5, 1, 4])}')
        