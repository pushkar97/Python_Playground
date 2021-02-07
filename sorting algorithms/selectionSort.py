def selectionSort(unsortedList):
    for i in range(0, len(unsortedList)):
        min = i
        for j  in range(i + 1, len(unsortedList)):
            min = j if unsortedList[min] > unsortedList[j] else min
        unsortedList[i], unsortedList[min] = unsortedList[min], unsortedList[i]
    return unsortedList

if __name__ == "__main__":
    print(f'selectionSort : {selectionSort([5, 3, 9, 1, 4])}')
