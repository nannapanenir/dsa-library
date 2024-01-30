"""
Moori's voting algorithem :

type : leetcode-169 

The majority element is the element that appears more than ⌊n / 2⌋ times.

Intuition:

Candidate Elimination: Imagine a group of people voting for different candidates. The algorithm focuses on finding the candidate who receives more than half of the votes.
Counterbalancing Votes: It starts with no candidate and a vote count of 0. As it iterates through the elements (votes):
If there's no current candidate (count = 0), it picks the current element as the potential candidate.
If the current element matches the candidate, it gains a vote (count++).
If it doesn't match, it loses a vote (count--).
True Majority Verification: After the first pass, it verifies if the candidate truly has a majority by counting its occurrences in the array.
Winner or No Winner: If the candidate's count is greater than half the array's length, it's the majority element and is returned. Otherwise, no majority element exists, and -1 is returned.
Key Idea:

The algorithm effectively cancels out votes for non-majority elements, leaving the true majority element "standing" in the end.
It achieves linear time complexity (O(n)), making it highly efficient for finding majority elements.

function majorityElement(nums):
    candidate = -1  // Initialize candidate element as unknown
    count = 0      // Initialize vote count to 0

    for i in nums:
        if count == 0:
            candidate = i  // Set new candidate if no current majority
        count += (1 if i == candidate else -1)  // Increment if match, decrement otherwise

    // Verify if candidate is indeed the majority element
    count = 0
    for i in nums:
        if i == candidate:
            count += 1

    return candidate if count > len(nums) // 2 else -1

Input: nums = [3,2,3]
Output: 3
---------------------

Input: nums = [2,2,1,1,1,2,2]
Output: 2

n == nums.length
1 <= n <= 5 * 10^4
-109 <= nums[i] <= 10^9

follow up can we solve this O(1) space complexity 

other possiblity solutions we can try but it costs extra space and time complexity

sol -1 : brute force  using two loops: time complexity will increase for all cases O(n^2)

sol-2: using hasmap's we can count the each candidate occurances, after that we can itterate the using loop then we can find majority element

here the pro's : time complexity will not be increased which is O(n) and we needed extra space for the hashmap, which is of n so the space c will be O(n)


"""
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote=0
        candidate=-1
        for i in nums:
            if vote==0:
                candidate=i
                vote=1
            elif i == candidate:
                vote+=1
            else:
                vote-=1
        count=0
        for i in nums:
            if candidate==i:
                count+=1
        if count> len(nums)//2:

            return candidate
        return -1
        

