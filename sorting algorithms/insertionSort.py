def insertionSort(unsortedList):
    for i in range(1, len(unsortedList)):
        j = i
        while(j > 0 and unsortedList[j] < unsortedList[j - 1]):
            unsortedList[j], unsortedList[j - 1] = unsortedList[j - 1], unsortedList[j]
            j = j - 1
    return unsortedList

if __name__ == "__main__":
    print(f'insertionSort : {insertionSort([5, 3, 9, 1, 4])}')

