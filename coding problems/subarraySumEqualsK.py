# Problem : Find a count subarrays from given array whose sum equals to given number
# input will be an array and a number

# solution 1 : brute force solution O(n^2)
def solution1(list, num):
    output = 0
    for startIndex in range(len(list)) :
        for endIndex in range(startIndex + 1, len(list) + 1) :
             if sum(list[startIndex : endIndex]) == num :
                 output += 1
    return output

# solution 2 : 
def solution2(list, num):
    sumMap = {0:1}
    output = 0
    for i in range(len(list)):
        if sumMap.get(sum(list[: i + 1]) - num):
            output += 1
        sumMap[sum(list[: i + 1])] = 1
    return output

if __name__ == "__main__":
    print(f"subarray count with sum given to number : {solution1([1,-2,3,4,-5], 2)}")