def maxSubarraySum(arr, n) :
    current_sum=0
    best_sum=float('-inf')
    for i in range(n):
        current_sum+=arr[i]
        if current_sum <0:
            current_sum=0
        if best_sum < current_sum :
            best_sum=current_sum
    return best_sum

arr=[-7 ,-8 ,-16 ,-4 ,-8 ,-5 ,-7 ,-11 ,-10 ,-12 ,-4 ,-6 ,-4 ,-16, -10 ]
print(maxSubarraySum(arr,len(arr)))