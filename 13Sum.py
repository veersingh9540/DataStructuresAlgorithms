# Example 2: Given a sorted array of unique integers and a target integer, 
# return true if there exists a pair of numbers that sum to target, false otherwise. 
# This problem is similar to Two Sum. (In Two Sum, the input is not sorted).
# For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.

nums = [1, 2, 4, 6, 8, 9,14, 15]
Target = 13

left = 0
right = len(nums)-1
def sum_count(nums, Target)-> bool:
    left = 0
    right = len(nums) -1
    while left < right: 
        curr_sum = nums[left]+ nums[right]
        if (curr_sum == Target):
            return True
        if (curr_sum> Target):
            right -= 1
        else:
            left +=1
    return False

x = sum_count(nums, Target)
print(x)
