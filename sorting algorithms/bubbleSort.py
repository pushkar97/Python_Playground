def bubbleSort(unsortedList):
    for i in range (0, len(unsortedList) - 1):
        for j in range(0, len(unsortedList) - i - 1):
            if unsortedList[j] > unsortedList [j+1]:
                unsortedList[j], unsortedList [j+1] = unsortedList [j+1], unsortedList[j]
    return unsortedList

if __name__ == "__main__":
    print(f'bubbleSort : {bubbleSort([5, 3, 9, 1, 4])}')