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
        print(e)
    

if(__name__ == '__main__'):
    myList = sorted('I Love Coding')
    print(myList)
    value = 'L'
    print(binary_search(myList, value))