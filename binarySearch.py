def binary_search(list, value):
    try:
        mid_point = len(list) // 2
        if list[mid_point] == value:
            return mid_point
        elif(list[mid_point] < value):
            return mid_point + 1 + binary_search(list[mid_point + 1:], value)
        elif(list[mid_point] > value):
            return binary_search(list[:mid_point], value)
    except Exception as e:
        return -1
    

if(__name__ == '__main__'):
    myList = sorted([1,4,3,6])
    print(myList)
    value = 6
    print(binary_search(myList, value))