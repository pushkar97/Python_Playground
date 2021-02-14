def countingSort(unsortedList):
    count = [0] * (max(unsortedList) + 1)
    for num in unsortedList:
        count[num] += 1

    for num in range(1, len(count)):
        count[num] += count[num -1]
    
    output = [0] * len(unsortedList)
    for num in unsortedList:
        output[count[num - 1]] = num
        count[num - 1] +=1
    return output

if __name__ == "__main__":
    print(f'countingSort : {countingSort([9, 3, 5, 9, 3, 1, 4])}')
    