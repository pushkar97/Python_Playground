# Problem : Find a subarray with maximum sum from the given array 
#
# solution -> 
# kadane's algorithm
# local sum is the max sum subarray to the current index, 
# thus if current index value is greater than current index value + previous subarray (previous local sum)
# the subarray start index is reset to current index
# for each such subarray we will update max sum if it's sum is more than current max sum
def maxSum(list):
    maxSum = localMax = list[0]
    for num in list[1:]:
        localMax = max(num, localMax + num)
        maxSum = max(maxSum, localMax)
    return maxSum


if __name__ == "__main__":
    print(f"maxSum : {maxSum([1,-2,3,4,-5])}")