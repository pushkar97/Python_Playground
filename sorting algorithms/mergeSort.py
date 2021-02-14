def mergeSort(unsortedList):
    if len(unsortedList) == 1 : return unsortedList

    firstHalf = unsortedList[:len(unsortedList)//2]
    secondHalf = unsortedList[len(unsortedList)//2:]

    firstHalf = mergeSort(firstHalf)
    secondHalf = mergeSort(secondHalf)
    
    i = j = 0
    output = []
    while i < len(firstHalf) and j < len(secondHalf):
        if firstHalf[i] < secondHalf[j]:
            output.append(firstHalf[i])
            i += 1
        else:
            output.append(secondHalf[j])
            j += 1
    return output + firstHalf[i:len(firstHalf)] + secondHalf[j:len(secondHalf)]

if __name__ == "__main__":
    print(f'mergeSort : {mergeSort([9, 3, 5, 1, 4])}')